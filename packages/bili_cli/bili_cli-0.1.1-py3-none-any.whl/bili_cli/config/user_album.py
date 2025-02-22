#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import pydantic
import re
import sys
import random
import inspect
from typing import List, Callable, Dict, Optional
from bili_cli.base import BaseModel, BaseMongoORM, MongoQuery
from bili_cli import const, mod, dto
from bili_cli.config.user import UserConfig, get_user, get_users
from bili_cli.config.album import AlbumConfig, get_album, get_albums
from bili_cli import utils
from bili_cli.tools import logger
from bili_cli.mod import AuthUser, PartConfig, TypeRandPart


class ReplyConfig(mod.BaseEpisode):
    message: str = pydantic.Field("", title="回复内容")


class UserAlbumConfig(BaseMongoORM):
    user_id: Optional[str] = pydantic.Field(None, title="")
    user: Optional[UserConfig] = pydantic.Field(None, title="")
    album_id: str = pydantic.Field(title="")
    album: Optional[AlbumConfig] = pydantic.Field(None, title="")
    episode_split_title_rexs: List[str] = pydantic.Field([], title="分集名称的正则")
    episode_split_title_regs: List[re.Pattern] = pydantic.Field(
        [], title="分集名称的正则")
    season_reg_configs: List['SeasonRegConfig'] = pydantic.Field([])
    archive_to_episode_func: Callable[
        ['UserAlbumConfig', mod.ArcAuditModel],
        mod.EpisodeModel] = pydantic.Field(
        None, title="稿件转剧集的方法")
    common_split_req: dto.SplitReqDTO | None = pydantic.Field(None, title="分割视频的请求")
    split_reqs: List[dict] = pydantic.Field([], title="分割视频的请求")
    common_reply: str = pydantic.Field("", title="公用评论")
    replys: List[ReplyConfig] = pydantic.Field([], title="评论配置")
    reply_map: Dict[any, ReplyConfig] = pydantic.Field({}, title="评论配置")
    big_video_suffix: List[TypeRandPart] = pydantic.Field(
        [], title="大视频混合后缀")
    split_suffix: List[TypeRandPart] = pydantic.Field([], title="分割视频后缀")

    class SeasonRegConfig(BaseModel):
        title: str = pydantic.Field(title="集合的名字")
        episode_rex: str = pydantic.Field(title="符合集合的剧集名称正则")
        episode_reg: re.Pattern = pydantic.Field(None, title="")

    class Meta(BaseMongoORM.Meta):
        TABLE = 'user_album'

        user_id: str = ""
        album_id: str = ""
        common_split_req: dto.SplitReqDTO = None
        episode_split_title_rexs: List[str] = []
        split_reqs: List[dict] = []
        split_suffix: List[mod.TypeRandPart] = []

    def get_id(self) -> str:
        return self.build_id(self.user_id, self.album_id)

    @classmethod
    def build_id(cls, user_id, album_id):
        return str(f"{user_id}-{album_id}")

    @property
    def conf_id(self):
        return self.get_id()

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['conf_id', 'album_id', 'split_count', 'episode_split_title_rexs', 'split_suffix']

    @property
    def split_count(self):
        if self.common_split_req:
            return self.common_split_req.count
        return 0

    def get_save_data(self) -> dict:
        data = super().get_save_data()
        data.pop('user', None)
        data.pop('album', None)
        data.pop('episode_split_title_regs', None)
        data.pop('archive_to_episode_func', None)
        data.pop('season_reg_configs', None)
        data.pop('reply_map', None)
        return data

    @classmethod
    def build(cls) -> 'UserAlbumConfig':
        item = cls(
            user_id=cls.Meta.user_id,
            album_id=cls.Meta.album_id,
        )
        for field in (
            'episode_split_title_rexs', 'common_split_req',
            'split_reqs', 'common_reply', 'big_video_suffix',
            'split_suffix',
        ):
            if hasattr(cls.Meta, field):
                setattr(item, field, getattr(cls.Meta, field))
        return item

    def load(self) -> 'UserAlbumConfig':
        # 初始化基本信息
        if not self.user_id or not self.album_id:
            raise ValueError("user_id or album_id not found")

        self.user = get_user(self.user_id)
        self.album = get_album(self.album_id)

        rex_kwargs = {
            'album': self.album.title,
        }

        # season_reg_configs
        season_reg_configs = self.season_reg_configs or []
        for i, conf in enumerate(season_reg_configs):
            season_reg_configs[i].title = conf.title.format(**rex_kwargs)
            episode_rex = conf.episode_rex.format(**rex_kwargs)
            season_reg_configs[i].episode_rex = episode_rex
            season_reg_configs[i].episode_reg = re.compile(episode_rex)
        self.season_reg_configs = season_reg_configs

        # 回复
        for reply in self.replys:
            if reply.episode_id:
                self.reply_map[reply.episode_id] = reply
            else:
                self.reply_map[reply.season] = reply

        # 正则相关
        rex_kwargs = {
            'album': self.album.title,
        }
        rex_kwargs.update(const.EPISODE_TITLE_REX_DICT)
        #  episode_split_title_rex = self.episode_split_title_rex
        episode_split_title_rexs: list = self.episode_split_title_rexs
        if not episode_split_title_rexs:
            episode_split_title_rexs = const.REX_EPISODE_SPLITS.get(
                const.get_manage_identity(self.album_id, self.user_id)) or []
        regs = []
        for rex in episode_split_title_rexs:
            rex = rex.format(**rex_kwargs)
            regs.append(re.compile(rex))
        self.episode_split_title_regs = regs
        # common_split_req
        if self.common_split_req:
            if not self.common_split_req.part_title_fmt:
                split_fmt = const.FMT_SPLIT_TITLE.get(
                    const.get_manage_identity(self.album_id, self.user_id)) or ""
                if split_fmt:
                    self.common_split_req.part_title_fmt = split_fmt
            #  values['common_split_req'] = common_split_req

        return self

    def match_archive_to_episode(
            self, arc: mod.ArcAuditModel) -> mod.EpisodeModel:
        return self.match_title_to_episode(arc.title)

    def match_title_to_episode(
            self, title: str) -> mod.EpisodeModel:
        part = self.match_title_to_part(title)
        if part:
            return self.album.get_episode(part.episode_id)
        return None

    def match_title_to_part(
            self, title: str) -> mod.MatchPart:
        def _match(reg):
            try:
                part = utils.match_part(reg, title)
                logger.debug(f"match {reg} with {title} to {part}")
                if part:
                    return part
            except Exception as e:
                print(e)
                return None
        for reg in self.episode_split_title_regs:
            item = _match(reg)
            if item:
                return item

    def get_split_req_by_episode(
            self, episode: mod.EpisodeModel) -> dto.SplitReqDTO:
        def _filter():
            for req in self.split_reqs:
                season_id = req.get("season_id")
                if season_id == episode.season:
                    return req
                elif req.get("episode_id") == episode.id:
                    return req
            return {}

        common_split = self.common_split_req
        req_dict = common_split.dict()
        filter_req = _filter()
        req_dict.update(filter_req)

        item = dto.SplitReqDTO(**req_dict)
        item.manage_name = self.album_id
        item.bili_name = self.user_id
        item.season_id = episode.season
        return item

    def get_reply(self, episode: mod.EpisodeModel = None) -> str:
        if self.reply_map and episode:
            reply = self.reply_map.get(episode.id)
            if reply:
                return reply.message
            reply = self.reply_map.get(episode.season)
            if reply:
                return reply.message

        return self.common_reply


def xinxin_archive_to_episode(
        conf: UserAlbumConfig, arc: mod.ArcAuditModel) -> mod.EpisodeModel:
    if arc.title.startswith('02'):
        title_prefix, _ = arc.title.split(' ')
        id_prefix, part = title_prefix.split('.')
        s, ep = id_prefix.rsplit('0', 1)
        s = int(s)
        ep = int(ep)
        ep_id = f"S{s:0>2}E{ep:0>2}"
        return mod.EpisodeModel(id=ep_id, album_id=conf.album_id)
    episode = conf.match_archive_to_episode(arc)
    if not episode:
        return None
    for album in get_albums():
        if album.title in arc.archive.tag:
            episode.album_id = album.id
    return episode


def get_portrait_suffixs():
    #  "共2.2.1", "共3.1.1", "共4.1.1"
    items = [
        #  "/Volumes/Getea/bili_cli/part/common/共2.2.1.ts",
        "/Volumes/Getea/bili_cli/part/common/共3.1.1.ts",
        "/Volumes/Getea/bili_cli/part/common/共4.1.1.ts",
        "/Volumes/Getea/bili_cli/part/common/共4.2.1.ts",
    ]
    random.shuffle(items)
    return items


_BMS = []


def append_user_configs(bili_name: str, configs: list):
    for conf in configs:
        conf.user_id = bili_name
        _BMS.append(conf)


class WenConfig(UserAlbumConfig):

    class Meta(UserAlbumConfig.Meta):
        user_id = const.BILI_NAME_WEN


append_user_configs(const.BILI_NAME_WEN, [
    # 已删除
    UserAlbumConfig(
        album_id=const.MANAGE_NAME_LEI,
    ).enable_delete(),
    UserAlbumConfig(
        album_id=const.MANAGE_NAME_KUANGBIAO,
    ).enable_delete(),
    UserAlbumConfig(
        album_id=const.MANAGE_NAME_ZHUI_FENG,
    ).enable_delete(),
])


class WenIpartmentConfig(WenConfig):

    class Meta(WenConfig.Meta):
        album_id = const.MANAGE_NAME_IPARTMENT
        common_split_req = dto.SplitReqDTO(
            count=3, with_suffix=True, is_average=True, is_remove_bed=True,
            part_title_fmt="{album}{season}.{ep}.{part}-{episode}"
        )
        split_reqs = [
            dict(season_id=3, is_remove_bed=False),
        ]
        episode_split_title_rexs = [
            "^爱情公寓{season}.{ep}.{part}",
        ]
        split_suffix = [
            mod.PartConfig.build(const.MANAGE_NAME_LORD_LOSER, max_duration=3 * 60),
            mod.PartConfig.build(const.MANAGE_NAME_FEI_CHAI, max_duration=3 * 60),
        ]


class WenWanwanConfig(WenConfig):

    class Meta(WenConfig.Meta):
        album_id = const.MANAGE_NAME_WANWAN
        common_split_req = dto.SplitReqDTO(
            count=1, with_suffix=True, is_average=True, is_remove_bed=True,
            part_title_fmt="{album}{season}.{ep}.{part}"
        )
        episode_split_title_rexs = [
            "^万万没想到{season}.{ep}.{part}"
        ]


class WenHuanleConfig(WenConfig):

    class Meta(WenConfig.Meta):
        album_id = const.MANAGE_NAME_HUANLE
        common_split_req = dto.SplitReqDTO(
            count=4, with_suffix=True, is_average=True, is_remove_bed=True,
            part_title_fmt="{album}{season}.{ep}.{part}"
        )
        episode_split_title_rexs = [
            "^欢乐英雄{season}.{ep}.{part}"
        ]


class WenFeichaiConfig(WenConfig):

    class Meta(WenConfig.Meta):
        album_id = const.MANAGE_NAME_FEI_CHAI
        common_split_req = dto.SplitReqDTO(
            count=2, with_suffix=True, is_average=True, is_remove_bed=True,
            part_title_fmt="废柴兄弟{season}.{ep}.{part}-{episode}({part_fmt})"
        )
        episode_split_title_rexs = [
            "废柴兄弟{season}.{ep}.{part}"
        ]
        split_suffix = [
            mod.PartConfig.build(const.ALBUM.IPARTMENT, max_duration=2 * 60),
            mod.PartConfig.build(const.ALBUM.LONGMEN, max_duration=3 * 60),
        ]


class WenBigBangConfig(WenConfig):

    class Meta(WenConfig.Meta):
        album_id = const.MANAGE_NAME_BIG_BANG


class WenLaonongtangConfig(WenConfig):

    class Meta(WenConfig.Meta):
        album_id = const.MANAGE_NAME_LAONONGTANG
        common_split_req = dto.SplitReqDTO(
            count=3, with_suffix=True, is_average=True, is_remove_bed=True,
            part_title_fmt="欢笑老弄堂{season}.{ep}.{part}-{episode}"
        )
        episode_split_title_rexs = [
            '欢笑老弄堂{season}.{ep}.{part}-{episode}',
        ]
        split_suffix = [
            mod.PartConfig.build(const.ALBUM.IPARTMENT, max_duration=3 * 60),
            mod.PartConfig.build(const.ALBUM.LONGMEN, max_duration=3 * 60),
        ]


class WenFayiConfig(WenConfig):

    class Meta(WenConfig.Meta):
        album_id = const.MANAGE_NAME_FAYI
        common_split_req = dto.SplitReqDTO(
            count=3, with_suffix=True, is_average=True, is_remove_bed=True,
            part_title_fmt="法医秦明{season}.{ep}.{part}-{episode}"
        )
        episode_split_title_rexs = [
            '法医秦明{season}.{ep}.{part}',
        ]
        split_suffix = [
            PartConfig.build(const.ALBUM.IPARTMENT, max_duration=3 * 60),
            PartConfig.build(const.ALBUM.LONGMEN, max_duration=3 * 60),
        ]


class XinxinConfig(UserAlbumConfig):

    class Meta(UserAlbumConfig.Meta):
        user_id = const.BILI_NAME_XINXIN

append_user_configs(const.BILI_NAME_WEN, [
    # 已删除
    UserAlbumConfig(
        album_id=const.MANAGE_NAME_MOT,
    ).enable_delete(),
    UserAlbumConfig(
        album_id=const.MANAGE_NAME_LANG_YA_BANG,
    ).enable_delete(),
])


class XinxinIpartmentConfig(XinxinConfig):

    class Meta(XinxinConfig.Meta):
        album_id = const.MANAGE_NAME_IPARTMENT
        common_split_req = dto.SplitReqDTO(
            count=6, use_exist_part_title=True,
            is_remove_bed=True, with_suffix=True, is_average=True,
        )
        split_suffix = [
            PartConfig.build(const.ALBUM.LORD_LOSER, max_duration=3 * 60),
            PartConfig.build(const.ALBUM.LONGMEN, max_duration=3 * 60),
            PartConfig.build(const.ALBUM.NOGE, max_duration=3 * 60),
            PartConfig.build(const.ALBUM.FEI_CHAI, max_duration=3 * 60),
        ]
        split_reqs = [
            dict(season_id=1, count=8),
            dict(season_id=3, count=2, is_remove_bed=False,
                 is_concat_full=True, use_exist_part_title=False,
                 part_title_fmt="爱S{season:0>2}E{ep:0>2}-{episode}"
                 ),
            #  dict(episode_id="S05E35", suffix_func=get_portrait_suffixs),
        ]


class XinxinLordLoserConfig(XinxinConfig):

    class Meta(XinxinConfig.Meta):
        album_id = const.MANAGE_NAME_LORD_LOSER
        common_split_req = dto.SplitReqDTO(
            count=6, use_exist_part_title=True,
            is_remove_bed=True, with_suffix=True, is_average=True,
        )
        split_suffix = [
            PartConfig.build(const.ALBUM.IPARTMENT, max_duration=2 * 60),
            PartConfig.build(const.ALBUM.LONGMEN, max_duration=3 * 60),
            PartConfig.build(const.ALBUM.NOGE, max_duration=3 * 60),
            PartConfig.build(const.ALBUM.FEI_CHAI, max_duration=3 * 60),
        ]
        split_reqs = [
            #  dict(episode_id="S02E07", count=6,
                 #  suffix_func=get_portrait_suffixs),
        ]
        common_reply = "其他集会慢慢补上，最近数据越来越差了，三联也不敢要，看的舒服了有能力给充充电吧，不然真是没动力搞下去了[笑哭]"


class XinxinLaonongtangConfig(XinxinConfig):

    class Meta(XinxinConfig.Meta):
        album_id = const.MANAGE_NAME_LAONONGTANG
        common_split_req = dto.SplitReqDTO(
            count=4, with_suffix=True, is_average=True, is_remove_bed=True,
            part_title_fmt="欢笑老弄堂S{season:0>2}E{ep:0>2}.{part}"
        )
        episode_split_title_rexs = [
            '^欢笑老弄堂S{season:0>2}E{ep:0>2}',
        ]
        split_suffix = [
            PartConfig.build(const.ALBUM.IPARTMENT, max_duration=3 * 60),
            PartConfig.build(const.ALBUM.LONGMEN, max_duration=3 * 60),
        ]


class XinxinBigBangConfig(XinxinConfig):

    class Meta(XinxinConfig.Meta):
        album_id = const.MANAGE_NAME_BIG_BANG
        common_split_req = dto.SplitReqDTO(
            count=1, with_suffix=True, is_average=True, is_remove_bed=True,
            is_concat_full=True,
            part_title_fmt="爆S{season:0>2}E{ep:0>2}"
        )
        episode_split_title_rexs = [
            '^爆S{season:0>2}E{ep:0>2}',
            '^生活大爆炸S{season:0>2}E{ep:0>2}'
        ]
        big_video_suffix = [
            const.MANAGE_NAME_TOM_JERRY,
            const.MANAGE_NAME_MUSIC,
            const.MANAGE_NAME_OPUS,
            const.MANAGE_NAME_MUSIC,
            const.MANAGE_NAME_IPARTMENT,
            const.MANAGE_NAME_MUSIC,
            const.MANAGE_NAME_LORD_LOSER,
            const.MANAGE_NAME_MUSIC,
            const.MANAGE_NAME_LONGMEN,
            const.MANAGE_NAME_MUSIC,
            const.MANAGE_NAME_MOVIE_SONG,
            const.MANAGE_NAME_MUSIC,
            const.MANAGE_NAME_MOVIE_SONG,
        ]



class XinxinMOSConfig(XinxinConfig):

    class Meta(XinxinConfig.Meta):
        album_id = const.MANAGE_NAME_MOS
        common_split_req = dto.SplitReqDTO(
            count=4, with_prefix=True,
            is_remove_bed=True, with_suffix=True, is_average=True,
            is_concat_full=True,
            part_title_fmt="武S{season:0>2}E{ep:0>2}-{episode}"
        )


class XinxinFayiConfig(XinxinConfig):

    class Meta(XinxinConfig.Meta):
        album_id = const.MANAGE_NAME_FAYI
        common_split_req = dto.SplitReqDTO(
            count=3, with_suffix=True, is_average=True, is_remove_bed=True,
            part_title_fmt="法S{season:0>2}E{ep:0>2}.{part}-{episode}"
        )
        episode_split_title_rexs = [
            '^法S{season:0>2}E{ep:0>2}.{part}',
        ]
        split_suffix = [
            PartConfig.build(const.ALBUM.LONGMEN, max_duration=3 * 60),
            PartConfig.build(const.ALBUM.IPARTMENT, max_duration=2 * 60),
        ]


class IpartConfig(UserAlbumConfig):

    class Meta(UserAlbumConfig.Meta):
        user_id = const.BILI_NAME_IPART


class IpartIpartmengConfig(IpartConfig):

    class Meta(IpartConfig.Meta):
        album_id = const.MANAGE_NAME_IPARTMENT
        common_split_req = dto.SplitReqDTO(
            count=4,
            use_exist_part_title=True,
            is_remove_bed=True, with_suffix=True, is_average=True,
            part_title_fmt="{album}{season}.{ep}.{part}-{episode}",
        )
        split_reqs = [
            dict(season_id=3, is_remove_bed=False),
            #  dict(episode_id="S05E35", suffix_func=get_portrait_suffixs),
        ]
        common_reply = "点个关注就可以入住爱情公寓[给心心]，这里情侣入住，投币全免，只需点赞[doge]"


class Ipart2Config(UserAlbumConfig):

    class Meta(UserAlbumConfig.Meta):
        user_id = const.BILI_NAME_IPART2


class Ipart2IpartmengConfig(IpartConfig):

    class Meta(Ipart2Config.Meta):
        album_id = const.MANAGE_NAME_IPARTMENT
        common_split_req = dto.SplitReqDTO(
            count=4, is_remove_bed=True, with_suffix=True, is_average=True,
            part_title_fmt="爱情公寓{season}E{ep}P{part}-{episode}",
        )
        split_reqs = [
            dict(season_id=3, is_remove_bed=False),
            dict(season_id=6, is_remove_bed=False, count=1),
            dict(season_id=7, is_remove_bed=False, count=1),
            dict(season_id=8, is_remove_bed=False, count=1),
            #  dict(season_id=9, is_remove_bed=False),
        ]
        episode_split_title_rexs = [
            '^爱情公寓{season}E{ep}P{part}',
            '^爱{season}.{ep}.{part}',
            '^爱情公寓{season}.{ep}.{part}',
        ]
        common_reply = "点个关注就可以入住爱情公寓[给心心]，这里情侣入住，投币全免，只需点赞[doge]"
        split_suffix = [
            PartConfig.build(const.ALBUM.LORD_LOSER, max_duration=3 * 60),
            PartConfig.build(const.ALBUM.LONGMEN, max_duration=3 * 60),
        ]


class WxnacyConfig(UserAlbumConfig):

    class Meta(UserAlbumConfig.Meta):
        user_id = const.BILI_NAME_WXNACY


append_user_configs(const.BILI_NAME_WXNACY, [
    # 已删除
    UserAlbumConfig(
        album_id=const.MANAGE_NAME_DAWANG,
    ).enable_delete(),
    UserAlbumConfig(
        album_id=const.MANAGE_NAME_SHAOYE,
    ).enable_delete(),
])


class WxnacyIpartmentConfig(WxnacyConfig):

    class Meta(WxnacyConfig.Meta):
        album_id = const.MANAGE_NAME_IPARTMENT
        common_split_req = dto.SplitReqDTO(
            count=3,
            is_remove_bed=True, with_suffix=True, is_average=True,
        )
        split_reqs = [
            dict(season_id=3, is_remove_bed=False),
        ]


class WxnacyMovieConfig(WxnacyConfig):

    class Meta(WxnacyConfig.Meta):
        album_id = const.MANAGE_NAME_MOVIE
        common_reply = '为保留视频切莫三联，欢迎点播喜剧电影，尽量更新。如果喜欢看，欢迎充电支持UP，这是对我最大的鼓励'
        common_split_req = dto.SplitReqDTO(
            count=6, with_suffix=True, is_average=True, is_remove_bed=True,
            part_title_fmt="{episode}P{part}-{season}-{ep}"
        )
        split_reqs = [
            dict(episode_id="S1994E02031", is_concat_full=False,
                 with_prefix=False,
                 part_title_fmt="{episode}P{part}-{season}-{ep}"),
            dict(episode_id="S2004E12231", is_concat_full=False,
                 with_prefix=False,
                 part_title_fmt="{episode}P{part}-{season}-{ep}"),
            dict(episode_id="S2024E03011", is_concat_full=False,
                 with_prefix=False, count=12,
                 part_title_fmt="zccsh-P{part}-{season}-{ep}"),
            dict(episode_id="S2019E02051", is_concat_full=False,
                 with_prefix=False, count=9,
                 part_title_fmt="fcrs-P{part}-{season}-{ep}"),
            dict(episode_id="S2015E12311", is_concat_full=False,
                 with_prefix=False, count=12,
                 part_title_fmt="trjta-P{part}-{season}-{ep}"),
            dict(episode_id="S2018E02161", is_concat_full=False,
                 with_prefix=False, count=12,
                 part_title_fmt="trjta2-P{part}-{season}-{ep}"),
            dict(episode_id="S2021E02122", is_concat_full=False,
                 with_prefix=False, count=12,
                 part_title_fmt="nhlhy-P{part}-{season}-{ep}"),
            dict(episode_id="S1981E06121", is_concat_full=False,
                 with_prefix=False, count=12,
                 part_title_fmt="dbqb-P{part}-{season}-{ep}"),
            dict(episode_id="S2023E04201", is_concat_full=False,
                 with_prefix=False, count=12,
                 part_title_fmt="glgsddy-P{part}-{season}-{ep}"),
            dict(episode_id="S2024E02101", is_concat_full=False,
                 with_prefix=False, count=9,
                 part_title_fmt="fcrs2-P{part}-{season}-{ep}"),
        ]
        split_suffix = [
            PartConfig.build(const.ALBUM.IPARTMENT, max_duration=2 * 60),
            PartConfig.build(const.ALBUM.LONGMEN, max_duration=3 * 60),
            PartConfig.build(const.MANAGE_NAME_FEI_CHAI, max_duration=3 * 60),
        ]
        episode_split_title_rexs = [
            '.*【飞驰人生2-P{part}-{season}-{ep}】.*',
        ]


class WxnacyTangDramaConfig(WxnacyConfig):

    class Meta(WxnacyConfig.Meta):
        album_id = const.MANAGE_NAME_TANG_DRAMA
        common_split_req = dto.SplitReqDTO(
            count=4, with_suffix=True, is_average=True, is_remove_bed=True,
            part_title_fmt="唐网{season}.{ep}.{part}"
        )
        episode_split_title_rexs = [
            '唐网{season}.{ep}.{part}',
        ]


class WxnacyTuokouxiuConfig(WxnacyConfig):

    class Meta(WxnacyConfig.Meta):
        album_id = const.MANAGE_NAME_TUOKOUXIU
        episode_split_title_rexs = [
            '.*【脱口秀大会{season}-{ep}-{part}】.*'
        ]


class WxnacyXirenConfig(WxnacyConfig):

    class Meta(WxnacyConfig.Meta):
        album_id = const.MANAGE_NAME_XIREN
        episode_split_title_rexs = [
            '.*【喜人奇妙夜{season}-{ep}-{part}】.*'
        ]


def init_ua():
    _init_config_names = set()
    for user in get_users():
        _init_config_names.add(f'{user.id.capitalize()}Config')
    clzs = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for name, clz in clzs:
        if clz.__base__.__name__ in _init_config_names:
            clz.build().save()

    for item in _BMS:
        item.load().save()


def get_user_album(manage_name: str, bili_name: str) -> UserAlbumConfig:
    ua = UserAlbumConfig.find_by_id(UserAlbumConfig.build_id(bili_name, manage_name))
    if ua:
        return ua.load()
    return UserAlbumConfig(
        user_id=bili_name,
        album_id=manage_name,
    ).load()


def get_user_albums():
    for item in UserAlbumConfig.find(MongoQuery.default()):
        yield item.load()


def iter_album_and_user():
    for album in get_albums():
        for user in AuthUser.find():
            yield album, user
