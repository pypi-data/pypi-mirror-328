#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from typing import Self
from bilibili_sdk.enums import (
    ArchiveStatus,
)
from bilibili_sdk.dto import (
    GetArchiveListReq,
)
from bilibili_sdk import (
    api_client,
    member_client,
    ApiClient,
    MemberClient,
)
from bili_cli import const
from bili_cli.mod import AuthUser


class BiliBiliClient:
    api_client: ApiClient = api_client
    member_client: MemberClient = member_client
    mid: int

    def set_mid(self, mid: int) -> Self:
        self.mid = mid
        return self

    async def get_cookies(self) -> dict:
        user = AuthUser.find_by_id(self.mid)
        return user.cookies

    async def get_all_archives(
        self,
        status=ArchiveStatus.ALL,
        total_page: int = -1
    ):
        if total_page == -1:
            total_page = const.MAX_PAGE

        cookies = await self.get_cookies()
        ps = 50
        for i in range(total_page):
            pn = i+1
            req = GetArchiveListReq()
            req.ps = ps
            req.pn = pn
            req.status = status
            print(cookies)
            res = await self.member_client.set_cookies(cookies).get_archive_list(req)
            print(res)
            if not res.is_success:
                break
            items = res.data.arc_audits
            if not items:
                break
            await items
