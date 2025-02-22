#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from prettytable import PrettyTable
from wpy.format import Format
from datetime import datetime, timedelta
from pydantic import model_validator
from typing import List
from typer import Argument, Option
import pysrt
import typer
import plotext as plt
import pydantic
import requests
import json
import os
from bili_cli import dto, const
from bili_cli.bili import get_bili
from bili_cli.video import ffmpeg_utils
from bili_cli.const import DATA_DIR, IPARTMENT_BED, CACHE_DIR, BILI_NAME
from bili_cli.part.manage import get_manage


app = typer.Typer()


class BaseModel(pydantic.BaseModel):
    origin_data: dict = pydantic.Field(dict, title="视频id")
    id: str = pydantic.Field(title="视频id")

    bili: 'Bili' = pydantic.Field(None)

    class Meta():
        TABLE = ""

    @classmethod
    def create_table(cls):
        try:
            os.makedirs(os.path.join(DATA_DIR, cls.Meta.TABLE))
        except Exception:
            pass

    @classmethod
    def generate_table_path(cls):
        return os.path.join(DATA_DIR, cls.Meta.TABLE)

    def save(self):
        with open(os.path.join(self.generate_table_path(), self.id), 'w') as f:
            #  print(lf.origin_data)
            f.write(json.dumps(self.origin_data))

    @classmethod
    def find_by_id(cls, id: str):
        path = os.path.join(cls.generate_table_path(), id)
        if not os.path.exists(path):
            return None
        with open(path, 'r') as f:
            lines = f.readlines()
        data = json.loads('\n'.join(lines))
        #  print(data)
        return cls(bili=bili, origin_data=data, **data)


class OnlineModel(pydantic.BaseModel):
    total: str = pydantic.Field("0", title="总数")
    online: int = pydantic.Field(0, title="在线总数", description="大概数")

    @model_validator(mode='before')
    def validator_all(cls, values):
        total = values.get("total") or ""
        total = total.replace("+", "")
        if '万' in total:
            total = float(total.replace("万", "")) + 10000
        try:
            values['online'] = int(total)
        except:
            pass
        #  online_f = float(total)
        return values


class RecentModel(BaseModel):
    bvid: str = pydantic.Field("", title="视频id")
    oid: int = pydantic.Field(0, title="分p id")
    uname: str = pydantic.Field("", title="发送人")
    title: str = pydantic.Field("", title="视频标题")
    msg: str = pydantic.Field("", title="视频标题")
    create_time: datetime = pydantic.Field(None, title="发布时间")
    play_time: timedelta = pydantic.Field(None, title="播放时间")

    class Meta():
        TABLE = "recent"

    @model_validator(mode='before')
    def validator_all(cls, values):
        #  values['origin_data'] = values
        values['id'] = values.get("id_str")
        values['create_time'] = datetime.fromtimestamp(
            values.get("ctime") or 0)
        progress = values.get("progress") or 0
        milliseconds = progress % 1000
        total_seconds = (progress - milliseconds) / 1000
        seconds = total_seconds % 60
        values['play_time'] = timedelta(
            seconds=seconds, milliseconds=milliseconds)
        return values

    def save(self):
        super().save()
        dir = os.path.join(self.generate_table_path(), str(self.oid))
        try:
            os.makedirs(dir)
        except:
            pass
        with open(os.path.join(dir, self.id), 'w') as f:
            #  print(lf.origin_data)
            f.write(json.dumps(self.origin_data))


class EpisodeModel(pydantic.BaseModel):
    id: int = pydantic.Field(0, title="")
    title: str = pydantic.Field("", title="标题")
    order: int = pydantic.Field(0, title="排序")


class SectionModel(BaseModel):
    title: str = pydantic.Field("", title="标题")
    order: int = pydantic.Field(0, title="排序")
    ep_count: int = pydantic.Field(0, title="排序", alias="epCount")
    episodes: List['EpisodeModel'] = pydantic.Field([], title="剧集")

    @model_validator(mode='before')
    def validator_all(cls, values):
        values['id'] = str(values.get("id"))
        section = values.get("section") or {}
        if section:
            values.update(section)
        return values


class SeasonModel(BaseModel):
    title: str = pydantic.Field("", title="标题")
    view: int = pydantic.Field(0, title="观看数量")
    subscription: int = pydantic.Field(0, title="订阅数")
    sections: List['SectionModel'] = pydantic.Field([], title="章节")

    class Meta():
        TABLE = "season"

    @model_validator(mode='before')
    def validator_all(cls, values):
        values.update(values.pop('season'))
        values['id'] = str(values.get("id"))
        values.update(values.pop('seasonStat') or {})
        values['sections'] = values.get("sections").get("sections")
        return values

    def print(self):
        x = PrettyTable()
        x.align = 'l'
        x.field_names = ["合集", "章节", "剧集"]
        for sec in self.sections:
            x.add_row([
                "", sec.title, sec.ep_count
            ])
        print(x)
        print(self.title)


class ArchiveModel(BaseModel):
    aid: int = pydantic.Field(title="视频id")
    bvid: str = pydantic.Field(title="视频id")
    cid: int = pydantic.Field(0, title="p1 id")
    state: int = pydantic.Field(
        0, title="状态", description="-30 审核中、-40 审核通过，等待发布")
    state_desc: str = pydantic.Field("", title="状态描述")
    reject_reason: str = pydantic.Field("", title="锁定原因")
    title: str = pydantic.Field("", title="标题")
    desc: str = pydantic.Field("", title="描述")
    view: int = pydantic.Field(0, title="播放")
    danmaku: int = pydantic.Field(0, title="弹幕")
    reply: int = pydantic.Field(0, title="回复")
    favorite: int = pydantic.Field(0, title="收藏")
    coin: int = pydantic.Field(0, title="硬币")
    share: int = pydantic.Field(0, title="分享")
    like: int = pydantic.Field(0, title="点赞")
    online: int = pydantic.Field(0, title="在线总数", description="大概数")
    total_income: int = pydantic.Field(0, title="总收入")
    income_upload_time: datetime = pydantic.Field(None, title="收入更新时间")
    publish_time: datetime = pydantic.Field(None, title="发布时间")
    subscribe_time: datetime = pydantic.Field(None, title="预约发布时间")
    publish_days: int = pydantic.Field(0, title="发布天数")

    class Meta():
        TABLE = "archive"

    @model_validator(mode='before')
    def validator_all(cls, values):
        stat = values.get("stat") or {}
        values.update(stat)
        income_upload_ts = values.get("income_upload_time") or 0
        if isinstance(income_upload_ts, int):
            values['income_upload_time'] = datetime.fromtimestamp(
                income_upload_ts)
        values['publish_time'] = datetime.fromtimestamp(
            values.get("ptime") or 0)
        values['subscribe_time'] = datetime.fromtimestamp(
            values.get("dtime") or 0)
        values['publish_days'] = (datetime.now() - values['publish_time']).days
        values['id'] = values.get("bvid")
        return values


class ReplyModel(BaseModel):
    oid: int = pydantic.Field(0, title="视频aid")
    rpid: int = pydantic.Field(0, title="评论id")
    title: str = pydantic.Field("", title="标题")
    bvid: str = pydantic.Field("", title="视频id")
    from_uname: str = pydantic.Field("", title="发送人")
    reply_uname: str = pydantic.Field("", title="被回复人")
    content: str = pydantic.Field("", title="内容")
    reply_content: str = pydantic.Field("", title="被回复的内容")
    root: int = pydantic.Field(0, title="根评论id")
    parent: int = pydantic.Field(0, title="回复人id")
    #  parent_info: 'ReplyModel' = pydantic.Field(None, title="原评论")

    bili: 'Bili' = pydantic.Field(None)

    class Meta():
        TABLE = "reply"

    @model_validator(mode='before')
    def validator_all(cls, values):
        def parse_data(values):
            data = {}
            cont_model = values.get("content") or {}
            member = values.get("member") or {}
            data['content'] = cont_model.get("message") or ""
            data['from_uname'] = member.get("uname") or ""
            return data
        data = parse_data(values)
        values.update(data)
        # 原评论
        parent = values.get("parent_info") or {}
        parent_data = parse_data(parent)
        values['reply_uname'] = parent_data.get("from_uname")
        values['reply_content'] = parent_data.get("content")
        #  values['origin_data'] = values
        values['id'] = str(values.get("rpid"))
        return values

    def format(self):
        return f"""
[{item.bvid}] {item.title}
{item.from_uname}:
({item.rpid}|{item.oid}): {item.content[0:90]}
        """
        print(f"{item.bvid} {item.title}")
        print(f"\t{item.from_uname}: \n\t{item.content[0:90]}\n")

    def delete(self):
        data = {
            "rpid": self.rpid,
            "oid": self.oid,
            "type": 1,
            "jsonp": "jsonp",
            "csrf": self.bili.csrf
        }
        print(data)
        print(self.bili.cookie)
        res = requests.post(
            "https://api.bilibili.com/x/v2/reply/del",
            data=data,
            headers={"Cookie": self.bili.cookie,
                     "Content-Type": "application/x-www-form-urlencoded"}
        )
        print(res.json())

    def reply(self, message: str):
        parent_id = self.rpid
        root_id = self.root
        if not self.parent:
            root_id = self.rpid
        print(parent_id, root_id, self.oid)
        self.bili.reply(
            self.oid, message, parent=parent_id, parent_uname=self.from_uname,
            root=root_id,
        )


class UserModel(pydantic.BaseModel):
    name: str = pydantic.Field("")
    following: int = pydantic.Field(0, title="关注数")
    follower: int = pydantic.Field(0, title="粉丝数")
    login_fans: int = pydantic.Field(0, title="在线粉丝数")
    dynamic_count: int = pydantic.Field(0, title="动态数量")


class DayIncomModel(pydantic.BaseModel):
    date: datetime = pydantic.Field(None, title="日期")
    amt: int = pydantic.Field(0, title="收入")
    play: 'OverviewItemModel' = pydantic.Field(None, title="播放数据")

    @property
    def income(self):
        """The foo property."""
        f = float(self.amt) / 100
        return f"{f:2}"

    @model_validator(mode='before')
    def validator_all(cls, values):
        #  print(values)
        date = values.get("date") or 0
        values['date'] = datetime.fromtimestamp(date)
        return values


class OverviewItemModel(pydantic.BaseModel):
    """
     "date_key": 1696608000,
                "total_inc": 4081,
                "sub_total_inc": 0
    """
    date_key: int = pydantic.Field(title="日期")
    date: datetime = pydantic.Field(title="日期")
    total_inc: int = pydantic.Field(title="数据")
    sub_total_inc: int = pydantic.Field(0, title="数据")

    @property
    def inc(self):
        """The foo property."""
        if self.total_inc > 1000:
            return Format.format_float(self.total_inc/10000.0)
        return self.total_inc

    @model_validator(mode='before')
    def validator_all(cls, values):
        #  print(values)
        date = values.get("date_key") or 0
        values['date'] = datetime.fromtimestamp(date)
        return values


class Bili(pydantic.BaseModel):
    name: str = pydantic.Field(title="名称")
    cookie: str = pydantic.Field("")
    income_publish_time: datetime = pydantic.Field(None)
    csrf: str = pydantic.Field("")


    def get_online_total(self, bvid: str, cid: int) -> OnlineModel:
        res = requests.get(
            "https://api.bilibili.com/x/player/online/total",
            params={"aid": "", "cid": cid, "bvid": bvid},
            headers={"Cookie": self.cookie}
        )
        data = res.json().get("data") or {}
        return OnlineModel(**data)

    def get_archives(
            self, page=1, pagesize=10, with_online=False, order="senddate",
            status="pubed", keyword="",
    ) -> List[ArchiveModel]:
        res = requests.get(
            "https://member.bilibili.com/x/web/archives",
            params={
                "status": status,
                "order": order,
                "ps": pagesize,
                "pn": page,
                "keyword": keyword,
            },
            headers={"Cookie": self.cookie}
        )
        arc_audits = res.json().get("data", {}).get("arc_audits", []) or []
        archives = []
        for arc in arc_audits:
            data = arc.get("Archive")
            data.update(arc.get("stat"))
            rejects = arc.get("Videos")
            reject_reason = ""
            for reject in rejects:
                reject_reason += "/" + reject.get("reject_reason")
            data['reject_reason'] = reject_reason
            a = ArchiveModel(**data)
            if with_online:
                if self.income_publish_time and self.income_publish_time > a.publish_time:
                    continue

                la = ArchiveModel.find_by_id(a.bvid)
                if la:
                    a.cid = la.cid
                else:
                    da = self.get_archive_detail(a.bvid)
                    if da:
                        a = da
                total = self.get_online_total(a.bvid, a.cid)
                a.online = int(total.total.replace("+", "").replace('-', ''))
            print(a)
            archives.append(a)
        return archives

    def get_archive_detail(self, bvid) -> ArchiveModel:
        res = requests.get(
            "https://api.bilibili.com/x/web-interface/view",
            params={
                "bvid": bvid,
            },
            headers={"Cookie": self.cookie}
        )
        data = res.json().get("data", {})
        if not data:
            return None
        item = ArchiveModel(origin_data=data, **data)
        #  self.save_video(item)
        item.save()
        return item

    def get_section(self, id: int) -> SectionModel:
        params = {
            "id": id,
        }
        res = requests.get(
            "https://member.bilibili.com/x2/creative/web/season/section",
            params=params,
            headers={"Cookie": self.cookie}
        )
        data = res.json().get("data", {})
        item = SectionModel(origin_data=data, **data)
        item.save()
        return item

    def get_season(self, id: int, with_episode=False) -> SeasonModel:
        params = {
            "id": id,
        }
        res = requests.get(
            "https://member.bilibili.com/x2/creative/web/season",
            params=params,
            headers={"Cookie": self.cookie}
        )
        data = res.json().get("data", {})
        item = SeasonModel(origin_data=data, **data)
        if with_episode:
            sections = []
            for sec in item.sections:
                section = self.get_section(int(sec.id))
                sections.append(section)
            item.sections = sections
        item.save()
        return item

    def get_seasons(self, page=1, pagesize=30) -> List[SeasonModel]:
        params = {
            "ps": pagesize,
            "pn": page,
        }

        res = requests.get(
            "https://member.bilibili.com/x2/creative/web/seasons?order=mtime&sort=desc&draft=1",
            params=params,
            headers={"Cookie": self.cookie}
        )
        items = res.json().get("data", {}).get("seasons", []) or []
        res = []
        for item in items:
            r = SeasonModel(origin_data=item, **item)
            r.save()
            res.append(r)
        return res

    def get_recents(self, page=1, pagesize=50, oid=0, keyword=""):
        params = {
            "ps": pagesize,
            "pn": page,
        }
        url = "https://api.bilibili.com/x/v2/dm/recent"
        if oid or keyword:
            url = "https://api.bilibili.com/x/v2/dm/search?type=1&order=ctime&sort=desc&cp_filter=false"
            #  ArchiveModel.find_by_id(bvid)
            params['oid'] = oid
            params['keyword'] = keyword

        res = requests.get(
            url,
            params=params,
            headers={"Cookie": self.cookie}
        )
        items = res.json().get("data", {}).get("result", []) or []
        res = []
        for item in items:
            r = RecentModel(origin_data=item, **item)
            r.save()
            res.append(r)
        return res

    def get_all_reply(
            self, page=1, pagesize=10, keyword="", bvid=""
    ) -> List[ReplyModel]:
        res = requests.get(
            "https://api.bilibili.com/x/v2/reply/up/fulllist?order=1&filter=-1&type=1&charge_plus_filter=false",
            params={
                "status": "pubed",
                "keyword": keyword,
                "ps": pagesize,
                "pn": page,
                "bvid": bvid,
            },
            headers={"Cookie": self.cookie}
        )
        replys = res.json().get("data", {}).get("list", []) or []
        res = []
        for reply in replys:
            r = ReplyModel(bili=self, origin_data=reply, **reply)
            r.save()
            res.append(r)
        return res

    def reply(
            self, aid, message, parent: int = 0, parent_uname: str = "", root: int = 0, ):
        data = {
            "oid": aid,
            "type": 1,
            "plat": 1,
            "csrf": self.csrf,
            "message": message,
        }
        #  if parent:
        #  if root:
        data['root'] = root
        data['parent'] = parent
        if root != parent:
            if not parent_uname:
                raise Exception("没有回复人名称")
            data['message'] = f"回复 @{parent_uname} :{message}"

        res = requests.post(
            "https://api.bilibili.com/x/v2/reply/add",
            data=data,
            headers={"Cookie": self.cookie,
                     "Content-Type": "application/x-www-form-urlencoded"}
        )
        print(res.json())

    def get_archives_income(self, page=1, pagesize=10):
        res = requests.get(
            "https://api.bilibili.com/studio/growup/up/income/archive?biz=1&bvid=&csrf=14dc3760e555af821de456ad2bd30e29&s_locale=zh_CN",
            params={
                #  "status": "pubed",
                "from": (page-1)*pagesize,
                "limit": pagesize,
            },
            headers={"Cookie": self.cookie}
        )
        items = res.json().get("data", {}).get("list", []) or []
        res = []
        for item in items:
            item['income_upload_time'] = item.get("date")
            a = ArchiveModel(**item)
            res.append(a)
        return res

    def get_user(self) -> UserModel:
        res = requests.get(
            "https://api.bilibili.com/x/web-interface/nav/stat",
            params={
                #  "status": "pubed",
                #  "from": (page-1)*pagesize,
                #  "limit": pagesize,
            },
            headers={"Cookie": self.cookie}
        )
        stat = res.json().get("data", {})
        res = requests.get(
            "https://member.bilibili.com/x/web/data/v2/fans/stat/num?period=0",
            params={
                #  "status": "pubed",
                #  "from": (page-1)*pagesize,
                #  "limit": pagesize,
            },
            headers={"Cookie": self.cookie}
        )
        fans_data = res.json().get("data", {})
        res = requests.get(
            "https://api.bilibili.com/x/web-interface/nav",
            params={
                #  "status": "pubed",
                #  "from": (page-1)*pagesize,
                #  "limit": pagesize,
            },
            headers={"Cookie": self.cookie}
        )
        base = res.json().get("data", {})
        data = stat
        data.update(fans_data)
        data['name'] = base.get("uname")
        return UserModel(**data)

    def get_daliy_income(self, days=30, with_play=False) -> List[DayIncomModel]:
        res = requests.get(
            "https://api.bilibili.com/x/earnings/up/income/trend",
            params={"days": days},
            headers={"Cookie": self.cookie}
        )
        data: list = res.json().get("data", {}).get("data", [])
        res = []
        if with_play:
            plays = self.get_overview_gragh("play", period=1)
            play_data = {o.date_key: o for o in plays}
        for day in data:
            m = DayIncomModel(**day)
            if with_play:
                play = play_data.get(day.get("date"))
                if play:
                    m.play = play

            res.append(m)
        return res

    def get_overview_gragh(self, type: str, period: int = 0) -> List[OverviewItemModel]:
        res = requests.get(
            "https://member.bilibili.com/x/web/data/v2/overview/stat/graph",
            params={"period": period, "type": type},
            headers={"Cookie": self.cookie}
        )
        data: list = res.json().get("data", {}).get("tendency", [])
        res = []
        for day in data:
            m = OverviewItemModel(**day)
            res.append(m)
        return res


def _income(cookie):
    res = requests.get(
        "https://api.bilibili.com/x/earnings/up/income/trend",
        params={"days": 30},
        headers={"Cookie": cookie}
    )
    print(res.json())
    data: list = res.json().get("data", {}).get("data", [])
    print(data)
    dates = []
    amts = []
    total = 0
    data.sort(key=lambda o: o.get("date"), reverse=True)
    for d in data:
        amt = d.get("amt")
        total += amt
        amts.append(float(amt) / 100)
        t = datetime.fromtimestamp(d.get("date"))
        dates.append(t.date().isoformat())
    #  dates.sort(reverse=True)
    #  amts.sort(reverse=True)
    plt.bar(dates, amts, orientation="horizontal")
    plt.title("Most Favored Pizzas in the World")
    plt.show()
    print("total: ", float(total)/100)


#  def _archives(cookie):
    #  res = requests.get(
    #  "https://member.bilibili.com/x/web/archives",
    #  params={
    #  "status": "pubed",
    #  "ps": 20,
    #  },
    #  headers={"Cookie": cookie}
    #  )
    #  #  print(res.json())
    #  arc_audits = res.json().get("data", {}).get("arc_audits", [])
    #  titles = []
    #  views = []
    #  danmakus = []
    #  likes = []
    #  for item in arc_audits:
    #  aid = item.get("Archive", {}).get("aid")
    #  #  if aid == 575094864:
    #  #  continue
    #  title = item.get("Archive", {}).get("title")
    #  display_fields = item.get("display_fields", [])
    #  view = 0
    #  danmaku = 0
    #  like = 0
    #  for display in display_fields:
    #  name = display.get("name")
    #  value = display.get("value")
    #  if name == 'view':
    #  view = value
    #  elif name == 'danmaku':
    #  danmaku = value
    #  elif name == 'like':
    #  like = float(value) / view * 100

    #  titles.append(title[:10])
    #  views.append(view)
    #  danmakus.append(danmaku)
    #  likes.append(like)

    #  plt.simple_multiple_bar(
    #  titles, [views, likes], width=100, labels=['播放', '点赞'],
    #  title='视频数据')
    #  plt.show()


def print_online(bilis: List[Bili]):
    total_archives = []
    for bili in bilis:
        for i in range(10):
            page = i + 1
            archives = bili.get_archives(
                page=page, pagesize=50, with_online=True)
            if not archives:
                break
            total_archives.extend(archives)
    total_archives = [o for o in total_archives if o.online > 1]
    total_archives.sort(key=lambda o: o.online, reverse=True)

    print("在线人数排行：")
    print_archives(total_archives)
    total = 0
    view = 0
    for item in total_archives:
        #  print(item.online, item.view, item.title)
        total += item.online
        view += item.view
    print(f"在线人数：{total}")
    print(f"在线总播放：{view}")


def print_archives(archives: List[ArchiveModel]):
    from prettytable import PrettyTable
    x = PrettyTable()
    x.align = 'l'
    x.field_names = ["ID", "日期", "播放", "在线", "点赞", "弹幕", "标题", "状态(原因)"]
    for item in archives:
        try:
            like_scale = float(item.like) / item.view * 100
        except Exception:
            like_scale = 0

        state_desc = item.state_desc + item.reject_reason
        if item.state == -40:
            state_desc = f"{state_desc} {item.subscribe_time}"
        x.add_row([
            f"{item.bvid}({item.aid})",
            item.publish_time, item.view,
            item.online, f"({like_scale:.2f}){item.like}", item.danmaku, item.title,
            state_desc
        ])
    print(x)


def print_seasons(items: List[SeasonModel]):
    from prettytable import PrettyTable
    x = PrettyTable()
    x.align = 'l'
    x.field_names = ["ID", "名称", "观看", "订阅", "章节数"]
    for item in items:
        x.add_row([
            item.id, item.title, item.view, item.subscription, len(
                item.sections)
        ])
    print(x)


def print_recents(items: List[RecentModel]):
    from prettytable import PrettyTable
    x = PrettyTable()
    x.align = 'l'
    x.field_names = ["发送人", "播放时间", "弹幕内容", "发送时间", "视频"]
    for item in items:
        x.add_row([
            item.uname, item.play_time, item.msg, item.create_time.isoformat(),
            item.title,
        ])
    print(x)


def print_replys(replys: List[ReplyModel]):
    from prettytable import PrettyTable
    x = PrettyTable()
    x.align = 'l'
    x.field_names = ["ID/回复ID/根评论ID", "视频", "发送人和内容(回复人和信息)"]
    for item in replys:
        x.add_row([
            f"{item.rpid}\n{item.parent}/{item.root}",
            #  item.rpid, item.parent, item.root,
            f"({item.bvid}/{item.oid}){item.title[0:10]}",
            f"{item.from_uname}\n\t{item.content}\n{item.reply_uname}\n\t{item.reply_content}",
            #  item.from_uname,
            #  item.content,
            #  f"({item.reply_uname}){item.reply_content}"
        ])
    print(x)


def print_total_play():
    from prettytable import PrettyTable
    x = PrettyTable()
    x.align = 'l'
    field_names = ["日期"]

    incomes: List[List[OverviewItemModel]] = []
    days = 30
    for bili in BILIS:
        field_names.append(bili.name)
        data = bili.get_overview_gragh("play", period=1)
        print(data)
        incomes.append(data)
    #  field_names.append("总收入")
    x.field_names = field_names
    #  total = 0
    #  total_list = [0] * len(BILIS)
    for i in range(days):
        row = [f"{incomes[0][i].date.date().isoformat()}"]
        # 每天的总收入
        #  day_total = 0
        for j, income in enumerate(incomes):
            day_income = income[i]
            row.append(day_income.inc)
        x.add_row(row)

    print(x)


def print_total_income():
    from prettytable import PrettyTable
    x = PrettyTable()
    x.align = 'l'
    field_names = ["日期"]

    bilis = [BILI_WEN, BILI_WXNACY, BILI_XINXIN, BILI_IPART]

    incomes: List[List[DayIncomModel]] = []
    days = 30
    for bili in bilis:
        field_names.append(bili.name)
        data = bili.get_daliy_income(days=days, with_play=True)
        incomes.append(data)
    field_names.append("总收入")
    x.field_names = field_names
    total = 0
    total_list = [0] * len(bilis)
    for i in range(days):
        row = [f"{incomes[0][i].date.date().isoformat()}"]
        # 每天的总收入
        day_total = 0
        for j, income in enumerate(incomes):
            day_income = income[i]
            row.append(day_income.income + f" ({day_income.play.inc})")
            day_total += day_income.amt
            total_list[j] += day_income.amt
        row.append(f"{float(day_total)/100:.2f}")
        x.add_row(row)

    total_row = ["总"] + [f"{float(o)/100:.2f}" for o in total_list]
    total = sum(total_list)
    total_row.append(f"{float(total)/100:.2f}")
    x.add_row(total_row)

    print(x)
    average = total / (days - 1)
    month_income = average * 30
    print("平均日收入：", Format.format_float(average/100.0))
    print("预计月收入:", Format.format_float(month_income/100.0))


BILI_WEN = Bili(
    name="wen",
    csrf="0a9d857e9cfcb604e1517c299e478e2d",
)
BILI_XINXIN = Bili(
    name="xinxin",
    income_publish_time=datetime(2023, 10, 24),
    csrf="515d465e06bc8b4a1a2ccb268398d480",
)
BILI_WXNACY = Bili(
    name="wxnacy",
    csrf="8d8c5cda42f832a671b25c301996e395",
)
BILI_IPART = Bili(
    name="ipart",
    csrf="c0007686c9e526a2e1582ec88b616db4"
)
BILI_IPART2 = Bili(
    name="ipart2",
    csrf="b95ee46b441565902c1e46d8ae193a87"
)
BILI_ANONY = Bili(
    name="anony",
    csrf=""
)

BILI_DICT = {
    "wen": BILI_WEN,
    "wxnacy": BILI_WXNACY,
    "xinxin": BILI_XINXIN,
    "ipart": BILI_IPART,
    "ipart2": BILI_IPART2,
    "anony": BILI_ANONY,
}

BILIS = list(BILI_DICT.values())

bili_name = os.getenv("BILI_NAME") or "wen"
bili = BILI_DICT.get(bili_name) or BILI_WEN


@app.command()
def section(
    id: int = Argument(..., help="id"),
):
    item = bili.get_section(id)
    print(item)


@app.command()
def season(
    id: int = Option(0, "--id", help="视频id"),
    name: str = Option("", "-n", "--name", help="名称"),
    with_online: bool = Option(False, "--with-online", help="是否看在线"),
    is_check: bool = Option(False, "--check", help="是否看在线"),
    is_del_error: bool = Option(False, "--del-error", help="删除错误的"),
    is_format: bool = Option(False, "--format", help="删除错误的"),
    is_auto_create: bool = Option(False, "--auto-create", help="创建"),
):
    from bili_cli.bili import BaseBili
    bili: BaseBili = get_bili(bili_name)
    if is_auto_create and name:
        bili.auto_create_season(name)
        return
    if is_format:
        bili.season_format_auto(title=name)
        return
    sea_res = None
    if name:
        sea_res = bili.search_season(name)
    if sea_res:
        for sec in sea_res.sections.sections:
            print(sec.title, sec.ep_count)
            sec_res = bili.member_api.get_section(sec.id)
            for ep in sec_res.episodes:
                if ep.is_error_state:
                    if is_check:
                        print(ep.archive_state, ep.title)
                    elif is_del_error:
                        print(ep.archive_state, ep.title)
                        bili.member_api.section_episode_del(ep.id)
                #  if with_online:
                    #  online_res = bili.api.get_online(ep.aid, ep.cid)
                    #  print(online_res.count, ep.title)
                #  else:
                    #  print(ep.title)


@app.command()
def seasons(
    page: int = Option(1, "-p", "--page", help=""),
    pagesize: int = Option(30, "-ps", "--pagesize", help=""),
):
    items = bili.get_seasons(
        pagesize=pagesize, page=page
    )
    print_seasons(items)


@app.command()
def recents(
    oid: int = Option(0, "--oid", help="视频id"),
    bvid: str = Option("", "--bvid", help="视频id"),
    keyword: str = Option("", "-k", "--keyword", help="搜索关键字"),
    page: int = Option(1, "-p", "--page", help=""),
    pagesize: int = Option(50, "-ps", "--pagesize", help=""),
):
    items = bili.get_recents(
        pagesize=pagesize, page=page, oid=oid, keyword=keyword,
    )
    print_recents(items)


@app.command()
def replys(
    bvid: str = Option("", "--bvid", help="视频id"),
    keyword: str = Option("", "-k", "--keyword", help="搜索关键字"),
    page: int = Option(1, "-p", "--page", help=""),
    pagesize: int = Option(10, "-ps", "--pagesize", help=""),
    is_delete: bool = Option(False, "-D", "--delete", help=""),
):
    items = bili.get_all_reply(
        pagesize=pagesize, keyword=keyword, bvid=bvid,
        page=page,
    )
    print_replys(items)
    if is_delete and items:
        confirm = typer.confirm("Are you sure you want to delete it?")
        if confirm:
            for item in items:
                if keyword in item.content:
                    print(item.rpid, item.content)
                    item.delete()


@app.command()
def reply(
    aid: str = Option("", "--aid", help="视频id"),
    rpid: str = Option("", "--rpid", help="评论id"),
    message: str = Option("", "-m", "--message", help="内容"),
    #  pagesize: int = Option(10, "-ps", "--pagesize", help=""),
):
    if rpid:
        r: ReplyModel = ReplyModel.find_by_id(rpid)
        print(r)
        r.reply(message)
    if aid:
        bili.reply(aid, message)
    items = bili.get_all_reply()
    print_replys(items)


@app.command()
def online():
    if bili_name == 'total':
        print_online(BILIS)
    else:
        print_online([bili])


@app.command()
def income():
    if bili_name == 'total':
        print_total_income()
    else:
        _income(bili.cookie)
        archives = bili.get_archives_income(pagesize=15)
        for item in archives:
            print(f"{item.total_income / 100.0} {item.title}")


@app.command()
def play():
    if bili_name == 'total':
        print_total_play()


@app.command()
def archives(
    order: str = Option("senddate", "-o", "--order", help="排序"),
    status: str = Option("pubed", "-s", "--order",
                         help="状态 is_pubing, not_pubed, pubed"),
    with_online: bool = Option(False, "--with-online", help="是否看在线"),
    keyword: str = Option("", "-k", "--keyword", help="搜索关键字"),
    page: int = Option(1, "-p", "--page", help=""),
    pagesize: int = Option(10, "-ps", "--pagesize", help=""),
):
    archives = bili.get_archives(
        order=order, status=status, page=page, with_online=with_online,
        pagesize=pagesize, keyword=keyword
    )
    print_archives(archives)


@app.command()
def to_ts(
    path: str = Argument(..., help="需要分割的视频地址"),
    #  scale: int = Option(1080, "-s", "--scale", help="分辨率"),
):
    if os.path.isfile(path):
        ffmpeg_utils.to_ts(path)
    if os.path.isdir(path):
        for name in os.listdir(path):
            _path = os.path.join(path, name)
            ffmpeg_utils.to_ts(_path)


@app.command()
def part(
    cmd: str = Argument(..., help="子命令"),
    name: str = Option("ipartment", "-n", "--name", help="使用名称"),
    id: List[str] = Option([], "--id", help="id"),
    seasons: List[int] = Option([], "-S", "--season", help="季"),
    minute: int = Option(30, "-m", "--minute", help="分钟"),
    keyword: List[str] = Option([], "-k", "--keyword", help="id"),
    path: List[str] = Option([], "-p", "--path", help="使用名称"),
    remove_suffix: bool = Option(False, "--remove-suffix", help="是否带后缀"),
):

    manage = get_manage(name, bili_name)
    from bili_cli.dto import MixtureReqDTO
    req = MixtureReqDTO(
        manage_name=name,
        bili_name=bili_name,
        minute=minute,
        ids=id,
        with_suffix=not remove_suffix,
    )

    if cmd == "mix":
        from bili_cli.part.manage import make_mixture
        d = make_mixture(req)
        print(d)

    elif cmd == "remake":
        from bili_cli.part.manage import remake_history
        remake_history(name, bili_name, id[0])
    # 已经重写
    #  elif cmd == "init_ts":
        #  manage.save_parts_data()
    #  elif cmd == "create_ts":
        #  part: Part
        #  for part in manage.get_all_parts():
            #  ts = manage.get_or_create_part_ts(part)
            #  print(ts)
    elif cmd == "story":
        #  from bili_cli.part.manage import make_story
        from bili_cli.make import make_story
        make_story(req)
    elif cmd == "video":
        #  manage.make_story(id[0])
        from bili_cli.part.manage import make_video
        from bili_cli.dto import MixtureReqDTO
        req = MixtureReqDTO(
            manage_name=name,
            bili_name=bili_name,
            paths=path
        )
        make_video(req)
    elif cmd == "config":
        #  manage.make_story(id[0])
        from bili_cli.make import make
        req = dto.MixtureReqDTO(
            bili_name=bili_name,
            manage_name=name,
            ids=id
        )
        make(req)
    elif cmd == "remove-bed":
        manage.remove_bed(path[0], "")
    #  elif cmd == "init_srt":
        #  ipart.save_subtitles()
    else:
        print(id)

@app.command()
def resolution(
    path: str = Argument(..., help="需要分割的视频地址"),
    scale: int = Option(1080, "-s", "--scale", help="分辨率"),
    filter: str = Option("", "-f", "--filter", help="过滤"),
):

    def _resol(input):
        output = input.replace(".mp4", f"-{scale}.mp4")
        ffmpeg_utils.reduce_resolution(input, output, scale)

    if os.path.isfile(path):
        _resol(path)
    elif os.path.isdir(path):
        for name in os.listdir(path):
            if filter and filter not in name:
                continue
            input = os.path.join(path, name)
            print(input)
            _resol(input)


@app.command()
def split(
    path: str = Argument(..., help="需要分割的视频地址"),
    manage_name: str = Option(const.MANAGE_NAME_IPARTMENT, "-m", "--manage"),
    prefix: str = Option("", "-pf",  "--prefix", help="分割后的前缀"),
    start_time: int = Option(0, "-s", "--start", help="开始时间"),
    split_time: int = Option(0, "-t", "--time", help="分割时间"),
    count: int = Option(8, "-c", "--count", help="分割个数"),
    is_remove_bed: bool = Option(False, "-rbe",  "--remove-bed", help=""),
    is_average: bool = Option(False, "-a",  "--average", help=""),
    with_suffix: bool = Option(False,  "--with-suffix", help=""),
    use_custom_title: bool = Option(False,  "--use-custom-title", help=""),
):

    from bili_cli.part.manage import split_video
    #  m = Manage.build(manage_name, bili_name)
    #  m.pm.get_episode
    req = dto.SplitReqDTO.default()
    req.manage_name = manage_name
    req.bili_name = bili_name
    req.path = path
    req.prefix = prefix
    req.start_time = start_time
    req.split_time = split_time
    req.count = count
    req.is_remove_bed = is_remove_bed
    req.is_average = is_average
    req.with_suffix = with_suffix
    req.use_custom_title = use_custom_title
    split_video(req)
    return


@app.command()
def merge(
    path: str = Argument(..., help="关键字"),
    keyword: str = Option(None, '-k', '--keyword', help="关键字"),
):
    def get_time(sub):
        start = sub.start
        begin_time = start.hours * 3600 + start.minutes * 60 + start.seconds
        split_time = sub.duration.seconds
        mill = sub.duration.milliseconds + start.milliseconds
        r = mill / 1000.0

        if r > int(r):
            split_time += int(r) + 1
        else:
            split_time += int(r)

        #  print(sub.start.to_time().second, sub.duration)
        return begin_time - 10, split_time + 10
    srt_path = path.replace(".mp4", ".srt")
    subs = pysrt.open(srt_path)
    for sub in subs:
        if keyword in sub.text:
            print(sub)
            begin_time, split_time = get_time(sub)
            tmp_path = path.replace(
                ".mp4", sub.start.to_time().isoformat()+".mp4")
            ffmpeg_utils.cut_video(path, tmp_path, begin_time, split_time)

    #  import math
    print(int(0.5))


@app.command()
def serve(
):
    print("serve")


ReplyModel.create_table()
ArchiveModel.create_table()
RecentModel.create_table()
SeasonModel.create_table()
if __name__ == "__main__":
    begin = datetime.now()
    app()
    end = datetime.now()
    et = (end - begin).total_seconds()
    print(f"time used: {et}")

#  if __name__ == "_main__":
    #  begin = datetime.now()
    #  from .cmd import add_typer
    #  from typer import Typer
    #  app = Typer()
    #  add_typer(app)
    #  app()
    #  end = datetime.now()
    #  et = (end - begin).total_seconds()
    #  print(f"time used: {et}")

    #  import sys
    #  import os
    #  args = sys.argv[1:]
    #  bili_name = os.getenv("BILI_NAME") or "wen"
    #  bili = BILI_DICT.get(bili_name) or BILI_WEN
    #  begin = datetime.now()
    #  import argparse
    #  parser = argparse.ArgumentParser()
    #  parser.add_argument("cmd", help="cmd")
    #  parser.add_argument("-o", "--order", default="senddate")
#  #  , dest="pubed, is_pubing, not_pubed"
    #  parser.add_argument("-s", "--status", default="pubed")
    #  parser.add_argument("-k", "--keyword", default="")
    #  parser.add_argument("-a", "--action", default="")
    #  parser.add_argument("--bvid", default="")
    #  parser.add_argument("-p", "--page", type=int, default=1)
    #  parser.add_argument("-ps", "--pagesize", type=int, default=10)
    #  parser.add_argument("--with-online", action="store_true",
                        #  help="是否查看在线人数")
    #  args = parser.parse_args()
    #  cmd = args.cmd
    #  print(sys.path)
    #  print(os.getcwd())
    #  sys.path.append(os.getcwd())
    #  from bili_cli.dto import ArchivesReqDTO
#  #  if __name__ == "main__":
    #  #  if not args:
    #  #  #  r = ReplyModel(rpid=192143520592, oid=535175780, bili=bili)
    #  #  #  r.delete()
    #  #  #  return
    #  #  if bili_name == 'total':
    #  #  for bili in BILIS:
    #  #  user = bili.get_user()
    #  #  print(user)
    #  #  else:
    #  #  user = bili.get_user()
    #  #  print(user)

    #  end = datetime.now()
    #  et = (end - begin).total_seconds()
    #  print(f"time used: {et}")
