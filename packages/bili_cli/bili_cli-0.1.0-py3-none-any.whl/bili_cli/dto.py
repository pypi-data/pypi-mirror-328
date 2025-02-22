#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
from pydantic import Field, SkipValidation
from requests import Response
import json
from typing import List, Callable, Union, Dict, Any
from bili_cli.mod import SectionModel, SectionEpisodeModel
from bili_cli import const, mod
from bili_cli.base import BaseModel


class BaseReqDTO(BaseModel):

    @property
    def model_dump_exclude(self):
        return ['create_time', 'update_time', 'is_delete']

    @classmethod
    def default(cls):
        return cls()

    def to_req_data(self) -> dict:
        return self.dict()


class BaseListReqDTO(BaseReqDTO):
    pn: int = pydantic.Field(1)
    ps: int = pydantic.Field(10)


class BaseActionDTO(BaseReqDTO):
    csrf: str = pydantic.Field("", title="身份表示")


class ResponseData(BaseModel):
    code: int = Field(0, title="状态")
    ttl: int = Field(1, title="状态")
    message: str = Field("", title="信息")
    data: SkipValidation[Any] = Field(None, title="数据")


class BaseResDTO(BaseModel):
    response: Response = Field(None, title='返回结果', exclude=True)
    response_data: ResponseData = Field(None, title='返回结果', exclude=True)
    code: int = Field(0, title="状态")
    ttl: int = Field(1, title="状态")
    message: str = Field("", title="信息")
    data: SkipValidation[Any] = Field(None, title="数据")
    data_model: BaseModel = Field(None, title="数据")
    # 微信使用
    errcode: int = Field(0, title="状态")
    errmsg: str = Field("", title="信息")

    @property
    def is_success(self):
        """The is_success property."""
        return self.code == 0

    def pprint(self):
        data = json.loads(self.json())
        print(json.dumps(data, indent=2, ensure_ascii=False))

    @classmethod
    def default_error(cls, message: str = ""):
        return cls(code=500, message=message)

    @classmethod
    def build(cls, **kwargs) -> 'BaseResDTO':
        return cls(**kwargs)


class BaseListResDTO(BaseResDTO):
    page: 'Page' = pydantic.Field(None)

    class Page(BaseModel):
        num: int = pydantic.Field(0, title="页码")
        size: int = pydantic.Field(0, title="单页数量")
        total: int = pydantic.Field(0, title="总数")
        # for archives
        pn: int = pydantic.Field(0, title="页码")
        ps: int = pydantic.Field(0, title="单页数量")
        count: int = pydantic.Field(0, title="总数")


class ArchivesReqDTO():
    pass


class ArchiveEditDTO(BaseModel):
    """自用"""
    bvid: str = pydantic.Field(title="视频id")
    title: str = pydantic.Field("", title="标题")

    def is_need_update(self):
        if self.title:
            return True
        return False


class ArchiveEditReqDTO(BaseActionDTO):
    aid: int = pydantic.Field()
    title: str = pydantic.Field()
    cover: str = pydantic.Field(title="封面")
    copyright: int = pydantic.Field(0, title="版权保护")
    tid: int = pydantic.Field(title="分区id")
    tag: str = pydantic.Field("", title="标签")
    mission_id: int = pydantic.Field(0, title="活动id")
    topic_id: int = pydantic.Field(0, title="话题id")
    topic_detail: 'TopicDetail' = pydantic.Field(None, title="话题详情")
    desc_format_id: int = pydantic.Field(0, title="")
    desc: str = pydantic.Field("", title="描述")
    recreate: int = pydantic.Field(-1, title="是否重新创建")
    dynamic: str = pydantic.Field("", title="")
    interactive: int = pydantic.Field(0, title="")
    new_web_edit: int = pydantic.Field(1, title="")
    videos: List['Video'] = pydantic.Field([], title="视频列表")
    act_reserve_create: int = pydantic.Field(0, title="")
    handle_staff: bool = pydantic.Field(False, title="")
    topic_grey: int = pydantic.Field(1, title="")
    no_reprint: int = pydantic.Field(0, title="")
    subtitle: 'Subtitle' = pydantic.Field(None, title="")
    is_360: int = pydantic.Field(0, title="是否为360")
    web_os: int = pydantic.Field(0, title="")

    class TopicDetail(BaseModel):
        from_topic_id: int = pydantic.Field(0, title="话题id")
        from_source: str = pydantic.Field(None, title="")

    class Video(BaseModel):
        cid: int = pydantic.Field(title="视频id")
        desc: str = pydantic.Field("", title="描述")
        filename: str = pydantic.Field("", title="猜测是md5")
        title: str = pydantic.Field("", title="标题")

    class Subtitle(BaseModel):
        open: int = pydantic.Field(0, title="")
        lan: str = pydantic.Field("", title="")

    @classmethod
    def from_archive(cls, arc: mod.ArcAuditModel) -> 'ArchiveEditReqDTO':
        arch = arc.archive
        data = arch.dict()
        data.pop('recreate', None)
        #  data.pop('act_reserve_create', None)
        #  data.pop('subtitle', None)
        item = cls(**data)
        item.act_reserve_create = int(arc.act_reserve_create)
        item.recreate = arch.receate.switch
        item.topic_detail = cls.TopicDetail(from_topic_id=arch.topic_id)
        item.subtitle = cls.Subtitle(
            open=int(arc.subtitle.allow), lan=arc.subtitle.lan)
        item.videos = arc.videos
        print('item videos', item.videos)
        return item


class ArchiveEditResDTO(BaseResDTO):
    aid: int = pydantic.Field(0)
    bvid: str = pydantic.Field(None)


class SectionDetailResDTO(BaseResDTO):
    section: SectionModel = pydantic.Field(None)
    episodes: List[SectionEpisodeModel] | None = pydantic.Field([], )


class SectionActiveResDTO(BaseResDTO):
    data: List[SectionModel] = pydantic.Field([], title="数据")


class ArchiveListReqDTO(BaseListReqDTO):
    keyword: str = pydantic.Field("", title="搜索关键字")
    order: str = pydantic.Field("senddate", title="")
    status: str = pydantic.Field(const.ARCHIVE_STATUS_ALL, title="")


class SeasonListReqDTO(BaseListReqDTO):
    order: str = pydantic.Field("mtime", title="排序字典")
    sort: str = pydantic.Field("desc", title="排序类型")
    draft: int = pydantic.Field(1, title="")


class SectionListResDTO(BaseResDTO):
    sections: List[mod.SectionModel] = pydantic.Field([])
    total: int = pydantic.Field(0, title="")


class SeasonDetailResDTO(BaseResDTO):
    season: mod.SeasonModel = pydantic.Field(None)
    sections: SectionListResDTO = pydantic.Field(None)

    def get_section_by_title(self, title):
        for sec in self.sections.sections:
            if sec.title == title:
                return sec
        return None


class SeasonListResDTO(BaseResDTO):
    seasons: List[SeasonDetailResDTO] | None = pydantic.Field([])
    total: int = pydantic.Field(0, title="总数")


class ArchiveListResDTO(BaseListResDTO):
    arc_audits: List[mod.ArcAuditModel] | None = pydantic.Field([])


class ArchiveViewResDTO(BaseResDTO):
    #  archive: mod.ArchiveModel = pydantic.Field(None)
    arc_audit: mod.ArcAuditModel | None = pydantic.Field(None)

    @classmethod
    def build(cls, **kwargs):
        item = cls(**kwargs)
        arc_data = kwargs.get("data") or {}
        arc_data['Archive'] = arc_data.pop('archive', {})
        item.arc_audit = mod.ArcAuditModel(**arc_data)
        return item


class ArchiveVideoListResDTO(BaseResDTO):
    archive: mod.ArchiveModel = pydantic.Field(None)
    videos: List[mod.VideoModel] = pydantic.Field([])


class OnlineResDTO(BaseResDTO):
    total: str = pydantic.Field("", title="")
    count: int = pydantic.Field(0, title="")

    @property
    def online(self) -> int:
        """The online property."""
        online = 0
        if self.total:
            try:
                total = self.total.replace("+", "")
                online = int(total)
            except Exception:
                online = self.count
        if online >= 1000:
            online += self.count
        return online


class DaliyIncomeResDTO(BaseResDTO):
    data: List[mod.DaliyIncomModel] = pydantic.Field([])


class ReplyListReqDTO(BaseListReqDTO):
    bvid: str = pydantic.Field("")
    keyword: str = pydantic.Field("")
    status: str = pydantic.Field("pubed")


class ReplyListResDTO(BaseListResDTO):
    list: List[mod.ReplyModel] = pydantic.Field([])


class ReplyLikeReqDTO(BaseActionDTO):
    oid: int = pydantic.Field(0, title="视频aid")
    rpid: int = pydantic.Field(0, title="评论id")
    type: int = pydantic.Field(1, title="")
    action: int = pydantic.Field(0, title="")


class ReplyDelReqDTO(BaseActionDTO):
    oid: int = pydantic.Field(0, title="视频aid")
    rpid: int = pydantic.Field(0, title="评论id")
    type: int = pydantic.Field(1, title="")


class ReplyAddReqDTO(BaseActionDTO):
    oid: int = pydantic.Field(0, title="视频aid")
    #  rpid: int = pydantic.Field(0, title="评论id")
    type: int = pydantic.Field(1, title="")
    root: int = pydantic.Field(0, title="")
    parent: int = pydantic.Field(0, title="")
    message: str = pydantic.Field("", title="")
    plat: int = pydantic.Field(1, title="")


class ReplyAddResDTO(BaseResDTO):
    rpid: int = pydantic.Field(0, title="评论id")
    reply: Union[mod.ReplyModel, None] = pydantic.Field(None, title="评论主体")
    success_action: int = pydantic.Field(0, title="状态")
    success_toast: str = pydantic.Field("", title="状态")


class CardSubmitReqDTO(BaseActionDTO):
    aid: int = pydantic.Field(0, title="视频aid")
    cid: int = pydantic.Field(0, title="视频aid")
    type: int = pydantic.Field(2, title="")
    permanent: bool = pydantic.Field(True, title="")
    cards: List[mod.Card] = pydantic.Field([], title="")

    def to_req_data(self) -> dict:
        data = self.dict()
        cards = json.dumps(data['cards'])
        data['cards'] = cards
        return data

    def add_card(self, from_: int, to: int, content: str
                 ) -> 'CardSubmitReqDTO':
        self.cards.append(mod.Card(
            from_=from_, to=to, content=content
        ))
        return self


class AllCardsResDTO(BaseResDTO):
    catalog: List['Catalog'] = pydantic.Field([], title="状态")

    class Catalog(BaseModel):
        cards: List[mod.Card] = pydantic.Field([])

# -------------------   企业微信


MSGTYPE_TEXT = 'text'
MSGTYPE_MARKDOWN = 'markdown'


class QYWebhookSendReqDTO(BaseReqDTO):
    msgtype: str = pydantic.Field(MSGTYPE_TEXT, title="类型")
    text: 'Text' = pydantic.Field(None, title="内容")
    markdown: 'Markdown' = pydantic.Field(None, title="内容")

    class Text(BaseModel):
        content: str = pydantic.Field("", title="内容")

    class Markdown(BaseModel):
        content: str = pydantic.Field("", title="内容")

    @classmethod
    def build_text(cls, text: str) -> 'QYWebhookSendReqDTO':
        t = cls.Text(content=text)
        req = cls()
        req.text = t
        return req

    @classmethod
    def build_markdown(cls, text: str) -> 'QYWebhookSendReqDTO':
        t = cls.Markdown(content=text)
        req = cls()
        req.markdown = t
        req.msgtype = MSGTYPE_MARKDOWN
        return req

# -------------------   自用


class MixtureReqDTO(BaseReqDTO):
    manage_name: str = pydantic.Field(
        const.MANAGE_NAME_IPARTMENT, title="名称")
    bili_name: str = pydantic.Field("", title="名称")
    minute: int = pydantic.Field(30, title="时长")
    ids: List[str] = pydantic.Field([], title="时长")
    paths: List[str] = pydantic.Field([], title="时长")
    with_suffix: bool = pydantic.Field(True, title="是否加后缀视频")


class SplitReqDTO(BaseReqDTO):
    id: str = pydantic.Field("", title="名称")
    manage_name: str = pydantic.Field("", title="名称")
    bili_name: str = pydantic.Field("", title="名称")
    season_id: int = pydantic.Field(0, title="季")
    episode_id: str = pydantic.Field("", title="季")
    prefix: str = pydantic.Field("", title="分割后名称前缀")
    part_title_fmt: str = pydantic.Field("", title="片段标题格式")
    path: str = pydantic.Field("", title="")
    is_remove_bed: bool = pydantic.Field(False, title="是否去掉片头片尾曲")
    is_average: bool = pydantic.Field(False, title="是否平均分割")
    with_suffix: bool = pydantic.Field(False, title="是否加后缀")
    with_prefix: bool = pydantic.Field(False, title="是否加前缀")
    suffix_func: Callable | None = pydantic.Field(None, title="后缀方法")
    use_custom_title: bool = pydantic.Field(False, title="使用剧集名称")
    #  part_title_func: Callable[[str, int], str] = pydantic.Field(None, title="片段名称方法")
    count: int = pydantic.Field(0, title="分割数量")
    start_time: int = pydantic.Field(0, title="开始时间")
    split_time: int = pydantic.Field(0, title="分割时间")
    use_exist_part_title: bool = pydantic.Field(False, title="使用已存在的片段名称")
    part_data: Dict[int, 'PartData'] = pydantic.Field({}, title="片段数据")
    is_concat_full: bool = pydantic.Field(False, title="是否拼接位完整视频")

    class PartData(BaseModel):
        part: int = pydantic.Field(0)
        title: str = pydantic.Field("")

    def get_part_title(self, part: int) -> str:
        data = self.part_data.get(part)
        if data:
            return data.title
        return ''


class IncomeChartResDTO(BaseResDTO):
    name: str = pydantic.Field(title="名称")
    type: str = pydantic.Field('bar', title="")
    color: str = pydantic.Field('', title="")
    label_position: str = pydantic.Field('insideTop', title="位置")
    data: list = pydantic.Field([], title="数据")


INCOME_CHART_RES_MAP = {
    "wxnacy": IncomeChartResDTO(name="wxnacy", color="rgba(0,191,183,1)"),
    "wen": IncomeChartResDTO(name="wen", color="rgba(255,144,128,1)"),
    "xinxin": IncomeChartResDTO(name="xinxin", color="rgba(138,43,226,1)"),
    "feifei": IncomeChartResDTO(name="feifei", color="rgba(255,105,180,1)"),
    "ipart": IncomeChartResDTO(name="ipart", color="rgba(0,191,255,1)",
                               label_position='top'),
    "ipart2": IncomeChartResDTO(name="feifei", color="rgba(255,105,180,1)"),
    "total": IncomeChartResDTO(name="total", color="rgba(252,230,48,1)",
                               type='line', label_position='top'),
}


class ManageResDTO(BaseResDTO):
    id: str = pydantic.Field(title="名称")
    title: str = pydantic.Field(title="名称")


class ReplyResDTO(BaseResDTO):
    replys: List[mod.ReplyModel] = pydantic.Field([], title="")
    total: int = pydantic.Field(0, title="总数")
