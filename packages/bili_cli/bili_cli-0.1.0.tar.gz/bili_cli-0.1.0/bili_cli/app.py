#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

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
import sys
#  sys.path.append(os.getcwd())
from bili_cli import ffmpeg_utils


app = typer.Typer()


COOKIES = {
    "wxnacy": "SESSDATA=9f1bddcd%2C1710740804%2C9106f%2A92CjAGw0sjq9RwlRTWrqIzIm6lVZenCNwC95v34nlNS_4Q_Ug2WVpASglmwcSOUl5ZThsSVlBLRU5Yb19EcnN1QnhYVjcwY0lLWl81TGx2TUs1NFExR1RLWWFKZWVSZEhSVkxhM2dreFNIODY5cEdZTUdDTFkzbHZfTWZpcmRmSG1VRUtsQ21oV0lRIIEC;",
    #  "wen": "SESSDATA=864156f2%2C1709474666%2C052aa%2A92Fy6q39eedhoRTrjHns_mmXxPZZnTAL6iIIFZx4EW-JEGdbKdZY1GlmBUTbNK4G4n6QaW9AAAOAA;",
    "wen": "SESSDATA=9b2e4fae%2C1713812954%2C8f808%2Aa2CjAHbq9ckIGuAnKiwIiZ8dqAtL0D92WJg9JguuKIo_tdBVUTcTAxBe9qGweWOfFKULQSVlRJNkVOclpmZ2xmMnBWOGJwSnNBTGVaNF9sQnNvSzhxd0xSWmZXM0FJTWxpbmNVcmpZN3lzb091b0ZQd3gzMDdIT1pLQThQMDNwQzNtcGhpU0RMdW53IIEC;",
    "xinxin": "SESSDATA=05fcf045%2C1714225123%2Ceea89%2Aa2CjAjpAK_yfWcnBk5sO8Vi7LybOW94C6E7x8vjkj4nNie2azLYrWTPkbnZKo5yYzkLgYSVlFNeWxrSy1UdGg0NWtVS0NnM0hUQjlxM3BNc2JPd0RHYTBVY09uSUxJaFVqWXR2NmctOVhYeWNqNUhIcUFXLVF0VXhTYjd5WE1rSVJlMmZYNHY5WEJnIIEC;",
}

#  TMP_DIR = '/tmp/bili'
DATA_DIR = os.path.join(os.getenv("HOME"), "Downloads/bili_cli/data")
try:
    os.mkdir(DATA_DIR)
except:
    pass


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

class BaseModel(pydantic.BaseModel):
    origin_data: dict = pydantic.Field(dict,title="视频id")
    id: str = pydantic.Field(title="视频id")


    class Meta():
        TABLE = ""

    @classmethod
    def create_table(cls):
        try:
            os.makedirs(os.path.join(DATA_DIR, cls.Meta.TABLE))
        except:
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
        return cls(bili=bili,origin_data=data, **data)

class RecentModel(BaseModel):
    bvid: str = pydantic.Field("", title="视频id")
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
        values['play_time'] = timedelta(seconds=seconds, milliseconds=milliseconds)
        return values

    def save(self):
        super().save()
        dir = os.path.join(self.generate_table_path(), self.bvid)
        try:
            os.makedirs(dir)
        except:
            pass
        with open(os.path.join(dir, self.id), 'w') as f:
            #  print(lf.origin_data)
            f.write(json.dumps(self.origin_data))
        

class ArchiveModel(BaseModel):
    aid: int = pydantic.Field(title="视频id")
    bvid: str = pydantic.Field(title="视频id")
    cid: int = pydantic.Field(0, title="p1 id")
    state: int = pydantic.Field(0, title="状态")
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


class Bili(pydantic.BaseModel):
    name: str = pydantic.Field(title="名称")
    cookie: str = pydantic.Field()
    income_publish_time: datetime = pydantic.Field(None)
    csrf: str = pydantic.Field("")

    #  def save_video(self, video: ArchiveModel):
        #  with open(os.path.join(TMP_DIR, video.bvid), 'w') as f:
            #  f.write(video.model_dump_json())

    #  def get_local_video(self, bvid) -> ArchiveModel:
        #  with open(os.path.join(TMP_DIR, bvid), 'r') as f:
            #  lines = f.readlines()
        #  data = json.loads('\n'.join(lines))
        #  return ArchiveModel(**data)

    def has_local(self, bvid) -> bool:
        #  self.find_by_id()
        return os.path.exists(os.path.join(TMP_DIR, bvid))

    def get_online_total(self, bvid: str, cid: int) -> OnlineModel:
        res = requests.get(
            "https://api.bilibili.com/x/player/online/total",
            params={"aid": "", "cid": cid, "bvid": bvid},
            headers={"Cookie": self.cookie}
        )
        data = res.json().get("data")
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
                    a = self.get_archive_detail(a.bvid)
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
        item = ArchiveModel(origin_data=data, **data)
        #  self.save_video(item)
        item.save()
        return item

    def get_recents(self, page=1, pagesize=50, oid=0, keyword="") :
        params={
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
            self, aid, message, parent: int=0, parent_uname: str ="", root: int=0, ):
        data={
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
            if not parent_uname :
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

    def get_daliy_income(self, days=30) -> List[DayIncomModel]:
        res = requests.get(
            "https://api.bilibili.com/x/earnings/up/income/trend",
            params={"days": days},
            headers={"Cookie": self.cookie}
        )
        data: list = res.json().get("data", {}).get("data", [])
        res = []
        for day in data:
            m = DayIncomModel(**day)
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
    x.field_names = ["ID", "日期", "播放", "在线", "点赞", "标题", "状态(原因)"]
    for item in archives:
        try:
            like_scale = float(item.like) / item.view * 100
        except Exception:
            like_scale = 0
        x.add_row([
            f"{item.bvid}({item.aid})",
            item.publish_time.isoformat(), item.view,
            item.online, f"({like_scale:.2f}){item.like}", item.title,
            item.state_desc + item.reject_reason
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
    x.field_names = ["ID", "回复ID", "根评论ID", "视频", "发送人", "内容", "回复人和信息"]
    for item in replys:
        x.add_row([
            item.rpid, item.parent, item.root,
            f"({item.bvid}/{item.oid}){item.title[0:20]}",
            item.from_uname,
            item.content,
            f"({item.reply_uname}){item.reply_content}"
        ])
    print(x)


def print_total_income():
    from prettytable import PrettyTable
    x = PrettyTable()
    x.align = 'l'
    field_names = ["日期"]

    incomes: List[List[DayIncomModel]] = []
    days = 10
    for bili in BILIS:
        field_names.append(bili.name)
        data = bili.get_daliy_income(days=days)
        incomes.append(data)
    field_names.append("总收入")
    x.field_names = field_names
    total = 0
    total_list = [0] * len(BILIS)
    for i in range(days):
        row = [f"{incomes[0][i].date.date().isoformat()}"]
        # 每天的总收入
        day_total = 0
        for j, income in enumerate(incomes):
            day_income = income[i]
            row.append(day_income.income)
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
    cookie=COOKIES.get("wen"),
    csrf="0a9d857e9cfcb604e1517c299e478e2d",
)
BILI_XINXIN = Bili(
    name="xinxin",
    cookie=COOKIES.get("xinxin"),
    income_publish_time=datetime(2023, 10, 24),
    csrf="515d465e06bc8b4a1a2ccb268398d480",
)
BILI_WXNACY = Bili(
    name="wxnacy",
    cookie=COOKIES.get("wxnacy"),
    csrf="8d8c5cda42f832a671b25c301996e395",
)

BILI_DICT = {
    "wen": BILI_WEN,
    "wxnacy": BILI_WXNACY,
    "xinxin": BILI_XINXIN,
}

BILIS = list(BILI_DICT.values())

bili_name = os.getenv("BILI_NAME") or "wen"
bili = BILI_DICT.get(bili_name) or BILI_WEN

@app.command()
def recents(
    aid: int = Option(0, "--aid", help="视频id"),
    bvid: str = Option("", "--bvid", help="视频id"),
    keyword: str = Option("", "-k", "--keyword", help="搜索关键字"),
    page: int = Option(1, "-p", "--page", help=""),
    pagesize: int = Option(50, "-ps", "--pagesize", help=""),
):
    items = bili.get_recents(
        pagesize=pagesize, page=page,
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
    if is_delete:
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
        r: ReplyModel =  ReplyModel.find_by_id(rpid)
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
def archives(
    order: str = Option("senddate", "-o", "--order", help="排序"),
    status: str = Option("pubed", "-s", "--order", help="状态 is_pubing, not_pubed, pubed"),
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

    import math
    print(int(0.5))


ReplyModel.create_table()
ArchiveModel.create_table()
RecentModel.create_table()
if __name__ == "__main__":
    begin = datetime.now()
    app()
    end = datetime.now()
    et = (end - begin).total_seconds()
    print(f"time used: {et}")

if __name__ == "_main__":
    import sys
    import os
    args = sys.argv[1:]
    bili_name = os.getenv("BILI_NAME") or "wen"
    bili = BILI_DICT.get(bili_name) or BILI_WEN
    begin = datetime.now()
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", help="cmd")
    parser.add_argument("-o", "--order", default="senddate")
#  , dest="pubed, is_pubing, not_pubed"
    parser.add_argument("-s", "--status", default="pubed")
    parser.add_argument("-k", "--keyword", default="")
    parser.add_argument("-a", "--action", default="")
    parser.add_argument("--bvid", default="")
    parser.add_argument("-p", "--page", type=int, default=1)
    parser.add_argument("-ps", "--pagesize", type=int, default=10)
    parser.add_argument("--with-online", action="store_true",
                        help="是否查看在线人数")
    args = parser.parse_args()
    cmd = args.cmd
    print(sys.path)
    print(os.getcwd())
    sys.path.append(os.getcwd())
    from bili_cli.dto import ArchivesReqDTO
#  if __name__ == "main__":
    #  if not args:
    #  #  r = ReplyModel(rpid=192143520592, oid=535175780, bili=bili)
    #  #  r.delete()
    #  #  return
    #  if bili_name == 'total':
    #  for bili in BILIS:
    #  user = bili.get_user()
    #  print(user)
    #  else:
    #  user = bili.get_user()
    #  print(user)


    if cmd == "delete_reply":
        for i in range(10):
            items = bili.get_all_reply(
                pagesize=10, page=i+1, keyword=args.keyword)
            for item in items:
                if args.keyword in item.content:
                    print(item.format())
                    item.delete()
    end = datetime.now()
    et = (end - begin).total_seconds()
    print(f"time used: {et}")
