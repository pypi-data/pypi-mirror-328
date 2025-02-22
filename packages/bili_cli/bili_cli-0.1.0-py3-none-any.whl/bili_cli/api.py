# Author:
# Description:

import pydantic
import json
import requests
from typing import Type, Union, Optional, Any
from bili_cli import dtos as dto, const
from bili_cli.mod import (
    RequestHistory, RequestModel, ResponseModel, AuthUser
)
from bili_cli.tools import sign_wbi, logger
from bili_cli.config import settings
from bili_cli.base import BaseModel

class APIError(Exception):
    pass

class BaseApi(BaseModel):
    auth: Optional[AuthUser] = pydantic.Field(None, title="身份认证")

    class Config():
        HOST: str
        FIELD_CODE: str = 'code'
        FIELD_MSG: str = 'message'
        COOKIES: dict = {
            'buvid3': 'A156F3B2-6831-D560-3992-CB39ED7A91EB17299infoc',
            'buvid4': 'B6A00BB6-D610-1E5E-814C-56FF9038B16854267-023082216-NVt3p3MOsSa19HMt7h14Ng%3D%3D',
        }
        HEADERS: dict = {
            'User-Agent': const.USER_AGENT,
            'Referer': 'https://www.bilibili.com/',
        }

    @property
    def bili_jct(self):
        """The bili_jct property."""
        if not self.auth:
            return ""
        return self.auth.cookies.bili_jct

    @property
    def log_prefix(self):
        if not self.auth:
            return ""
        return f"{self.auth.name}({self.auth.mid})"

    @classmethod
    def build(cls, auth: AuthUser = None):
        return cls(auth=auth)

    def splice_url(self, path) -> str:
        return self.Config.HOST + path

    def request(
        self, method: str, path: str, *, params: dict = None, data: Any = None, json: Any = None,
        cookies=None, headers=None, res_clz: Type = None
    ):
        _headers = {}
        _headers.update(self.Config.HEADERS)
        if headers:
            _headers.update(headers)

        # 拼装 cookie
        _cookies = {}
        _cookies.update(self.Config.COOKIES)
        if self.auth:
            _cookies.update(self.auth.cookies.dict())
        if cookies:
            _cookies.update(cookies)

        url = self.splice_url(path)
        logger.debug(f"{self.log_prefix} {method} {path}")
        logger.debug(f"{self.log_prefix} Params: {params}")
        logger.debug(f"{self.log_prefix} Json: {json}")
        logger.debug(f"{self.log_prefix} Data: {data}")
        res = requests.request(
                method, url, params=params, data=data, json=json,
                headers=_headers, cookies=_cookies)

        logger.debug(f"{self.log_prefix} Response text: {res.text}")
        h_req = RequestModel()
        h_req.path = path
        h_req.params = params
        h_req.data = data
        h_req.headers = dict(res.request.headers)
        h_req.cookies = dict(res.request._cookies)

        h_res = ResponseModel()
        h_res.data = self.get_response_json(res)
        h_res.text = res.text
        h_res.content = res.content
        h_res.headers = dict(res.headers)
        h_res.cookies = dict(res.cookies)

        h = RequestHistory(request=h_req, response=h_res)
        h.url = res.url
        h.method = method
        h.status_code = res.status_code
        h.save()

        if res_clz:
            return self.build_res(res, res_clz)
        return res

    def get_response_json(self, res: requests.Response) -> dict:
        try:
            return res.json()
        except Exception as e:
            json_begin = '{"code":'
            if res.text.count(json_begin) > 1:
                text = res.text[0:res.text.index(json_begin, 1)]
                return json.loads(text)
            else:
                raise e

    def get(self, path: str, *, params: Union[dict, dto.BaseReqDTO] = None, res_clz: Type = None):
        if isinstance(params, dto.BaseReqDTO):
            params = params.to_req_data()
        return self.request('GET', path, params=params, res_clz=res_clz)

    def post(self, path: str, data: Union[dict, dto.BaseActionDTO], *,
             res_clz: Type = None):
        if isinstance(data, dto.BaseActionDTO):
            data.csrf = self.bili_jct
            data = data.to_req_data()
        else:
            data['csrf'] = self.bili_jct
        params = {"csrf": self.bili_jct}
        return self.request('POST', path, params=params, json=data, res_clz=res_clz)

    def post_form(self, path: str, data: Union[dict, dto.BaseActionDTO],
                  res_clz: Type = None):
        if isinstance(data, dto.BaseActionDTO):
            data.csrf = self.bili_jct
            data = data.to_req_data()
        else:
            data['csrf'] = self.bili_jct
        return self.request('POST', path, data=data, headers={
                "Content-Type": "application/x-www-form-urlencoded"
            }, res_clz=res_clz)

    def build_res(self, res, clz: Type[dto.BaseResDTO]):
        data = self.get_response_json(res)
        code = data.get(self.Config.FIELD_CODE)
        if code == 0:
            d = data.get("data")
            if isinstance(d, dict):
                data.update(d)
        else:
            errmsg = data.get(self.Config.FIELD_MSG)
            msg = f"rqeuest error path: {res.request.path_url}"
            msg = f"{msg} code: {code} message: {errmsg}"
            raise APIError(msg)

        r = clz.build(**data)
        r.response = res
        return r


class Api(BaseApi):

    class Config(BaseApi.Config):
        HOST = "https://api.bilibili.com"

    def get_online(self, cid: int, *, aid: int = 0, bvid: str = '') -> dto.OnlineResDTO:
        if not aid and not bvid:
            raise ValueError("aid or bvid 需要有一个有值")
        params = {"cid": cid}
        if bvid:
            params['bvid'] = bvid
        if aid:
            params['aid'] = aid
        return self.get("/x/player/online/total", params=params, res_clz=dto.OnlineResDTO)

    def get_acc_info(self, mid: int) -> dto.AccInfoResDTO:
        '''用户空间详细信息
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/info.md
        '''
        params = {'mid': mid}
        params = sign_wbi(params, self.auth.wbi.img_key, self.auth.wbi.sub_key)
        return self.get("/x/space/wbi/acc/info", params=params, res_clz=dto.AccInfoResDTO)

    def get_web_inferface_nav(self) -> dto.WebInferfaceNavResDTO:
        '''导航栏用户信息
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/login_info.md
        '''
        return self.get("/x/web-interface/nav", res_clz=dto.WebInferfaceNavResDTO)

    def get_player_url(self, req: dto.PlayerUrlReqDTO) -> dto.PlayerUrlResDTO:
        '''获取视频播放地址
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/videostream_url.md
        '''
        return self.get("/x/player/wbi/playurl", params=req, res_clz=dto.PlayerUrlResDTO)

    def get_archive_info(self, *, bvid: str = None, aid: int = 0) -> dto.ArchiveInfoResDTO:
        '''获取稿件信息
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/info.md
        '''
        params = {"bvid": bvid, "aid": aid}
        return self.get("/x/web-interface/wbi/view", params=params, res_clz=dto.ArchiveInfoResDTO)

    def get_daliy_income(self, days) -> dto.DaliyIncomeResDTO:
        params = {
            "days": days
        }
        return self.get("/x/earnings/up/income/trend", params=params,
                        res_clz=dto.DaliyIncomeResDTO)

    def get_replys(
        self, req: dto.ReplyListReqDTO,
    ) -> dto.ReplyListResDTO:
        params = {
            "order": 1
        }
        params.update(req.model_dump(by_alias=True))
        return self.get(
            "/x/v2/reply/up/fulllist",
            params=params,
            res_clz=dto.ReplyListResDTO
        )

    def reply_like(
        self, req: dto.ReplyLikeReqDTO,
    ) -> dto.BaseResDTO:
        return self.post_form(
            "/x/v2/reply/action",
            data=req,
            res_clz=dto.BaseResDTO
        )

    def reply_top(
        self, req: dto.ReplyLikeReqDTO,
    ) -> dto.BaseResDTO:
        return self.post_form(
            "/x/v2/reply/top",
            data=req,
            res_clz=dto.BaseResDTO
        )

    def reply_add(
        self, req: dto.ReplyAddReqDTO,
    ) -> dto.ReplyAddResDTO:
        return self.post_form(
            "/x/v2/reply/add",
            data=req,
            res_clz=dto.ReplyAddResDTO
        )

    def reply_del(
        self, req: dto.ReplyDelReqDTO,
    ) -> dto.BaseResDTO:
        return self.post_form(
            "/x/v2/reply/del",
            data=req,
            res_clz=dto.BaseResDTO
        )


class MemberApi(BaseApi):

    class Config(BaseApi.Config):
        HOST = "https://member.bilibili.com"

    def get_season(self, id) -> dto.SeasonDetailResDTO:
        return self.get(
            "/x2/creative/web/season", params={"id": id}, res_clz=dto.SeasonDetailResDTO
        )

    def get_seasons(self, req: dto.SeasonListReqDTO) -> dto.SeasonListResDTO:
        params = req.to_req_data()
        res = self.get("/x2/creative/web/seasons", params=params)
        return self.build_res(res, dto.SeasonListResDTO)

    def get_section(self, id) -> dto.SectionDetailResDTO:
        return self.get(
            "/x2/creative/web/season/section",
            params={"id": id},
            res_clz=dto.SectionDetailResDTO
        )

    def get_section_active(self, id) -> dto.SectionActiveResDTO:
        return self.get("/x2/creative/web/season/sections/active",
                        params={"id": id}, res_clz=dto.SectionActiveResDTO)

    def get_archive_videos(self, aid: int) -> dto.ArchiveVideoListResDTO:
        return self.get("/x/web/archive/videos", params={"aid": aid},
                        res_clz=dto.ArchiveVideoListResDTO)

    def get_add_section_archives(
            self, req: dto.ArchiveListReqDTO
    ) -> dto.ArchiveListResDTO:
        params = req.model_dump(by_alias=True)
        return self.get(
            "/x2/creative/web/archives/sp",
            params=params, res_clz=dto.ArchiveListResDTO
        )

    def get_archives(self, req: dto.ArchiveListReqDTO) -> dto.ArchiveListResDTO:
        return self.get(
            "/x/web/archives",
            params=req,
            res_clz=dto.ArchiveListResDTO
        )

    def get_archive_view(self, bvid: str, topic_grey: int = 1
                         ) -> dto.ArchiveVideoListResDTO:
        data = {
            "topic_grey": topic_grey,
            "bvid": bvid
        }
        return self.get("/x/vupre/web/archive/view", params=data, res_clz=dto.ArchiveViewResDTO)

    def archive_edit(self, req: dto.ArchiveEditReqDTO) -> dto.ArchiveEditResDTO:
        res = self.post("/x/vu/web/edit", req, res_clz=dto.ArchiveEditResDTO)
        return res

    def section_add_episodes(
        self, req: dto.SectionEpisodeAddReqDTO
    ) -> dto.BaseResDTO:
        return self.post(
            "/x2/creative/web/season/section/episodes/add", data=req,
            res_clz=dto.BaseResDTO)

    def section_edit(
        self, req: dto.SectionEditReqDTO
    ) -> dto.BaseResDTO:
        req.section.create_time = None
        req.section.update_time = None
        return self.post("/x2/creative/web/season/section/edit",
                         data=req, res_clz=dto.BaseResDTO)

    def section_add(
        self, season_id: int, title: str, type: int = 0
    ) -> dto.BaseResDTO:
        data = {
            "seasonId": season_id,
            "title": title,
            "type": type
        }
        res = self.post(
            "/x2/creative/web/season/section/add", data)
        return self.build_res(res, dto.BaseResDTO)

    def section_del(
        self, section_id: int
    ) -> dto.BaseResDTO:
        data = {
            "id": section_id,
        }
        res = self.post_form(
            "/x2/creative/web/season/section/del", data)
        return self.build_res(res, dto.BaseResDTO)

    def season_add(
        self, req: dto.SeasonAddReqDTO
    ) -> dto.BaseResDTO:
        return self.post("/x2/creative/web/season/add", req, res_clz=dto.BaseResDTO)

    def season_edit(
        self, req: dto.SeasonEditReqDTO
    ) -> dto.BaseResDTO:
        return self.post("/x2/creative/web/season/edit", req, res_clz=dto.BaseResDTO)

    def season_del(
        self, id: int
    ) -> dto.BaseResDTO:
        return self.post_form("/x2/creative/web/season/del", data={"id": id}, res_clz=dto.BaseResDTO)

    def season_switch_forbid(
        self, season_id: int, forbid: int
    ) -> dto.BaseResDTO:
        data = {"season_id": int(season_id), "forbid": int(forbid)}
        return self.post(
            "/x2/creative/web/season/switch/forbid",
            data=data,
            res_clz=dto.BaseResDTO
        )

    def season_section_switch(
        self, season_id: int, no_section: int
    ) -> dto.BaseResDTO:
        data = {"season_id": int(season_id), "no_section": int(no_section)}
        return self.post(
            "/x2/creative/web/season/section/switch",
            data=data,
            res_clz=dto.BaseResDTO,
        )

    #  def archive_edit(
        #  self, req: dto.ArchivesEditReqDTO
    #  ) -> dto.ArchivesEditResDTO:
        #  data = req.to_req_data()
        #  data['csrf'] = self.auth.bili_jct
        #  res = self.post("/x/vu/web/edit", data)
        #  return self.build_res(res, dto.ArchivesEditResDTO)

    def section_episode_move(
        self, section_id: int, ep_id: int
    ) -> dto.BaseResDTO:
        data = {"sectionId": section_id, "epId": ep_id}
        data['csrf'] = self.bili_jct
        return self.post_form(
            "/x2/creative/web/season/section/episode/move", data,
            res_clz=dto.BaseResDTO)

    def section_episode_del(
        self, ep_id: int
    ) -> dto.BaseResDTO:
        data = {"id": ep_id}
        return self.post_form(
            "/x2/creative/web/season/section/episode/del", data,
            res_clz=dto.BaseResDTO)

    def card_submit(
            self, req: dto.CardSubmitReqDTO
    ) -> dto.BaseResDTO:
        return self.post_form(
            "/x/web/card/submit", req,
            res_clz=dto.BaseResDTO)

    def allcards(
            self, aid: int, cid: int
    ) -> dto.AllCardsResDTO:
        data = {
            "aid": aid,
            "cid": cid,
        }
        return self.get("/x/web/allcards", params=data, res_clz=dto.AllCardsResDTO)


class QYApi(BaseApi):

    class Config(BaseApi.Config):
        HOST = "https://qyapi.weixin.qq.com"
        KEY = settings.QY_KEY
        FIELD_CODE: str = 'errcode'
        FIELD_MSG: str = 'errmsg'

    @classmethod
    def default(cls) -> 'QYApi':
        return cls.build()

    def send_webhook(self, req: dto.QYWebhookSendReqDTO):
        data = req.dict()
        res = self.post(f'/cgi-bin/webhook/send?key={self.Config.KEY}',
                        data, res_clz=dto.BaseResDTO)
        res.code = res.errcode
        res.message = res.errmsg
        return res

    def send_parting_line(self, text: str):
        line = '-' * 100
        data = dto.QYWebhookSendReqDTO.build_text(f"{text} {line}").dict()
        res = self.post(f'/cgi-bin/webhook/send?key={self.Config.KEY}',
                        data, res_clz=dto.BaseResDTO)
        res.code = res.errcode
        res.message = res.errmsg
        return res


DEFAULT_QY_API = QYApi.default()
#  DEFAULT_PASSPORT_API = PassportApi.build()

if __name__ == "__main__":
    ...
    #  from bili_cli.const import COOKIES
    #  req = dto.QYWebhookSendReqDTO(**{"text": {"content": "你好"}})
    #  res = QYApi.default().send_webhook(dto.QYWebhookSendReqDTO.build_text("这是一条小时"))
    #  print(res)
    #  r = ms.get_section('2245059')
    #  r.pprint()

    #  req = dto.ArchiveListReqDTO.default()
    #  req.keyword = "S01E15"
    #  res = ms.get_add_section_archives(req)
    #  #  res.pprint()
    #  for arch in res.archives:
    #  print(arch.aid, arch.cid, arch.title)
    #  res = ms.get_archive_videos(323518323)
    #  print(res.videos)
