from pydantic import Field
from typing import List
from bili_cli.base import BaseModel


class CookieItem(BaseModel):
    name: str = Field("", title="名称")
    value: str = Field("", title="值")
    expires: int = Field(0, title="过期时间")
    http_only: int = Field(0, title="过期时间")
    same_site: int = Field(0, title="")
    secure: int = Field(0, title="")


class CookieInfo(BaseModel):
    cookies: List[CookieItem] = Field([], title='cookie 列表')
    domains: List[str] = Field([], title='域名列表')


class TokenInfo(BaseModel):
    access_token: str = Field('')
    refresh_token: str = Field('')
    expires_in: int = Field(0, title='过期时间')
    mid: int = Field(0, title='用户id')


class BiliUPAuth(BaseModel):
    platform: str = Field("", title='平台')
    cookie_info: CookieInfo = Field(CookieInfo(), title='cookie 信息')
    sso: List[str] = Field([])
    token_info: TokenInfo = Field(TokenInfo(), title='token详情')

    @property
    def cookie_map(self):
        data = {}
        for cookie in self.cookie_info.cookies:
            data[cookie.name] = cookie.value
        return data
