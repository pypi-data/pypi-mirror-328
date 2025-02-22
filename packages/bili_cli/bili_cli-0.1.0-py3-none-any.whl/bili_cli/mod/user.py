#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
from pydantic import Field
from collections import defaultdict
from datetime import datetime
from typing import List, Optional, Dict
from bili_cli.base import BaseMongoORM, BaseModel


class AuthCooke(BaseModel):
    sessdata: str = Field("", title="", alias='SESSDATA')
    bili_jct: str = Field("", title="")
    dede_user_id: str = Field('', title="", alias='DedeUserID')
    dede_user_id_ckmd5: str = Field('', title="", alias='DedeUserID__ckMd5')
    sid: str = Field("", title="")


class Wbi(BaseModel):
    img_url: str = Field("", title="")
    sub_url: str = Field("", title="")

    @property
    def img_key(self):
        """The img_key property."""
        return self.img_url.rsplit('/', 1)[1].split('.')[0]

    @property
    def sub_key(self):
        """The img_key property."""
        return self.sub_url.rsplit('/', 1)[1].split('.')[0]


class AuthUser(BaseMongoORM):
    mid: int = Field(0, title="用户mid")
    name: str = Field("", title="昵称", alias='uname')
    face: str = Field("", title="头像")
    money: float = Field(0, title="硬币")
    cookies: AuthCooke = Field(title="网络请求cookies")
    wbi: Optional[Wbi] = Field(None, title="新版鉴权信息")
    refresh_token: str = Field("", title="刷新 token")
    login_time: Optional[datetime] = Field(None, title="登录时间")
    refresh_time: Optional[datetime] = Field(None, title="刷新时间")
    # 额外字段，不保存
    is_default: bool = Field(False, title='是否为默认用户', exclude=False)

    class Meta(BaseMongoORM.Meta):
        TABLE = "auth_user"

    def get_id(self) -> str:
        return str(self.mid)

    def is_need_refresh(self):
        if not self.refresh_time:
            return True
        today = datetime.today()
        return today.date() != self.refresh_time.date()

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['mid', 'name', 'is_default', 'login_time', 'refresh_time']

    @property
    def name_fmt(self):
        return f"{self.name}({self.mid})"

    @property
    def bili_name(self):
        """The bili_name property."""
        return {
            43798284: 'wxnacy',
            3493118657694567: 'xinxin',
            3546560484870199: 'ipart',
            3546579025791044: 'feifei',
            3493080395156056: 'wen',
            3546621698640253: 'ipart2',
        }.get(self.mid)


class SysNotice(BaseModel):
    id: int = Field(0, title="")
    content: str = Field('', title="显示文案")
    url: str = Field('', title="跳转地址")
    notice_type: int = Field(0, title="提示类型")


class UserExt(BaseModel):
    is_followed: Dict[str, bool] = Field(defaultdict(bool), title='记录用户是否关注')


class User(BaseMongoORM):
    mid: int = Field(0, title="用户mid")
    name: str = Field("", title="用户昵称")
    sex: str = Field("", title="性别", description="男/女/保密")
    sign: str = Field("", title="签名")
    face: str = Field("", title="头像")
    coins: float = pydantic.Field(0, title="硬币")
    sys_notice: SysNotice = Field(SysNotice(), title="系统通知")
    silence: int = Field(0, title="封禁状态", description='0：正常 1：被封')
    rank: int = Field(0, title="用户权限等级", description='''目前应该无任何作用
5000：0级未答题
10000：普通会员
20000：字幕君
25000：VIP
30000：真·职人
32000：管理员''')
    level: int = Field(0, title="当前等级", description='0-6 级')
    jointime: int = Field(0, title="注册时间")
    ext: UserExt = Field(UserExt(), title='扩展字段')

    class Meta(BaseMongoORM.Meta):
        TABLE = "user"

    def get_id(self) -> str:
        return str(self.mid)

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['mid', 'name', 'sex', 'coins', 'sys_notice']

    def table_line(self) -> List[str]:
        return [self.get_id(), self.name, self.sex,
                self.coins, f"{self.sys_notice.id} {self.sys_notice.content}"]
