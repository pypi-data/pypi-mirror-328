#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import BaseModel, Field
from bili_cli.dtos import PlayerUrlResDTO, ArchiveInfoResDTO


class DownloadArchiveReq(BaseModel):
    resolution: str = Field('1080p', title='分辨率')
    archive: ArchiveInfoResDTO = Field(title='稿件详情')
    player: PlayerUrlResDTO = Field(title='视频地址详情')
    download_dir: str = Field(title='存储目录')
    filename: str = Field('', title='文件名')
    size: int = Field(0, title='文件大小')

    def get_filename(self):
        name = self.filename or self.archive.title
        if not name.endswith('.mp4'):
            name = f"{name}.mp4"
        return name
