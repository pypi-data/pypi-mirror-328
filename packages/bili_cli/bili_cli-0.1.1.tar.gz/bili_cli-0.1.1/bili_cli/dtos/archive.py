#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os
from typing import Optional, Union, List
from pydantic import Field, model_validator
from datetime import datetime
from .base import BaseReqDTO, BaseModel, BaseResDTO


class ArchiveUploadReqDTO(BaseReqDTO):
    path: str = Field(title='视频地址')
    cover: str = Field(title='封面地址')
    tag: str = Field(title='标签', description='用逗号隔开')
    title: str = Field("", title='标题')
    tid: int = Field(183, title='分区', description='默认影视剪辑')
    limit: int = Field(4, title='单视频文件最大并发数')
    dtime: Optional[Union[datetime, int, str]] = Field(None, title='预发布时间')
    desc: str = Field("")

    @model_validator(mode='before')
    def validator_all(cls, values):
        # 处理 dtme
        dtime = values.get('dtime')
        if dtime:
            if isinstance(dtime, str):
                dtime = datetime.strptime(dtime, '%Y-%m-%d %H:%M:%S')
            if isinstance(dtime, datetime):
                dtime = int(dtime.timestamp())
            values['dtime'] = dtime

        if not values.get("title"):
            path = values['path']
            video_dir, title = os.path.split(path)
            title, _ = os.path.splitext(title)
            values['title'] = title

        if not values.get("tag"):
            raise ValueError(f"tag: {values['tag']} 不能为空")

        return values

    def to_command_params(self) -> List[str]:
        cmds = [f"'{self.path}'",
                '--limit', f"{self.limit}",
                f'--tid {self.tid}',
                '--title', f'"{self.title}"',
                '--cover', f'"{self.cover}"',
                '--tag', f'"{self.tag}"',
                ]
        if self.dtime:
            cmds.append(f'--dtime {self.dtime}')
        return cmds


class PlayerUrlReqDTO(BaseReqDTO):
    avid: int = Field(0, title='avid')
    bvid: str = Field("", title="视频id")
    cid: int = Field(title="p1 id")
    qn: int = Field(80, title="清晰度",
        description='https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/videostream_url.md')
    fnval: int = Field(0, title="格式",
        description='https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/videostream_url.md#fnval%E8%A7%86%E9%A2%91%E6%B5%81%E6%A0%BC%E5%BC%8F%E6%A0%87%E8%AF%86')
    fourk: int = Field(1)
    platform: str = Field(None, title='平台')
    high_quality: int = Field(1, title='是否高画质', description='platform=html5时，此值为1可使画质为1080p')


class Durl(BaseModel):
    order: int = Field(0, title='视频分段序号', description='某些视频会分为多个片段（从1顺序增长')
    length: int = Field(0, title='视频长度', description='单位为毫秒')
    size: int = Field(0, title='视频大小', description='单位为Byte')
    url: str = Field("", title='默认流URL', description='注意 unicode 转义符,有效时间为120min')
    backup_url: Optional[List[str]] = Field([], title='备用视频流')


class DashVideo(BaseModel):
    id: int = Field(0, title='清晰度')
    base_url: str = Field("", title='默认流URL')


class Dash(BaseModel):
    duration: int = Field(0, title='视频', description='单位为毫秒')
    video: List[DashVideo] = Field([], title='视频流')
    audio: List[DashVideo] = Field([], title='音频流')


class PlayerUrlResDTO(BaseResDTO):
    format: str = Field("", title='视频格式')
    quality: int = Field(0, title='清晰度')
    timelength: int = Field(0, title='视频长度', description='单位为毫秒,不同分辨率 / 格式可能有略微差异')
    last_play_time: int = Field(0, title='上次播放进度', description='单位为毫秒')
    last_play_cid: int = Field(0, title='上次播放cid')
    durl: List[Durl] = Field([], title='视频分段流信息', description='注：仅 FLV / MP4 格式存在此字段')
    dash: Dash = Field(Dash(), title='dash 信息')

    @property
    def default_url(self):
        """使用默认地址"""
        if not self.durl:
            return ""
        return self.durl[0].url

    @property
    def default_durl(self) -> Durl:
        """使用默认地址对象"""
        if not self.durl:
            return None
        return self.durl[0]


class PageDimension(BaseModel):
    width: int = Field(0, title="")
    height: int = Field(0, title="")
    rotate: int = Field(0, title="是否将宽高对换", description='0：正常 1：对换')


class Page(BaseModel):
    cid: int = Field(0, title="cid")
    page: int = Field(0, title="序号")
    part: str = Field("", title="标题")
    from_: str = Field("", title="来源", alias='from',
        description='vupload：普通上传（B站）hunan：芒果TV qq：腾讯')
    duraction: int = Field(0, title="时长")
    dimension: PageDimension = Field(PageDimension(), title='分辨率')


class ArchiveInfoResDTO(BaseResDTO):
    aid: int = Field(title="视频id")
    bvid: str = Field(title="视频id")
    cid: int = Field(0, title="p1 id")
    videos: int = Field(0, title="视频数")
    title: str = Field("", title="标题")
    pic: str = Field("", title="封面")
    copyright: int = Field(0, title="版权保护")
    tid: int = Field(0, title="分区id")
    desc: str = Field("", title="描述")
    ctime: int = Field(0, title="")
    pubdate: int = Field(0, title="")
    duration: int = Field(0, title="时长")
    pages: List[Page] = Field([], title='分p信息')
