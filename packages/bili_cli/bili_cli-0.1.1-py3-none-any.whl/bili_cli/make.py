#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
import random
import os
from pydantic import Field
from typing import List
from bili_cli.base import BaseModel, BaseMongoORM, MongoQuery
from bili_cli.part.base import PartManage, Part
from bili_cli.part import manage as pm
from bili_cli import dto, const, mod, tools, config, utils
from bili_cli.config import get_album, get_user_album, settings
from bili_cli.bili import get_bilis, BaseBili


class PartConfig(BaseModel):
    manage_name: str = pydantic.Field()
    ids: List[str] = pydantic.Field([])
    ts_list: List[str] = pydantic.Field([])
    use_random_ids: bool = pydantic.Field(False, title="是否使用随机")
    random_minute: int = pydantic.Field(30, title="随机片段的时间")
    max_part_minute: int = pydantic.Field(0, title="片段最大时长")
    is_skip: bool = pydantic.Field(False, title="是否跳过")
    #  is_main: bool = pydantic.Field(False, title="")
    nav_title: str = pydantic.Field("", title="导航名称")

    manage: PartManage | None = pydantic.Field(None, title="管理")
    parts: List[Part] = pydantic.Field([], title="片段列表")

    def load(self, user_id="") -> 'PartConfig':
        # 解析id
        #  self.ids = utils.format_part_ids(self.ids)
        parse_ids = []
        album = config.get_album(self.manage_name)
        for id in self.ids:
            if id.count('-') == 1:
                if album and album.get_story_part_ids(id):
                    parse_ids.extend(album.get_story_part_ids(id))
                else:
                    parse_ids.extend(utils.format_continuous_part_ids(id))
            else:
                parse_ids.append(id)
        self.ids = parse_ids

        if user_id:
            self.manage = pm.get_manage(self.manage_name, user_id)

            # 使用随机id
            if self.use_random_ids:
                self.ids = self.manage.get_random_ids(
                    self.random_minute,
                    max_part_duration=self.max_part_minute * 60)

            if not self.ts_list:
                for id in self.ids:
                    parts = self.manage.get_parts_by_id(id)
                    for part in parts:
                        self.ts_list.append(self.manage.get_part_ts(part))

            if not self.parts:
                for id in self.ids:
                    parts = self.manage.get_parts_by_id(id)
                    for part in parts:
                        self.parts.append(part)

        return self

    #  def to_nav(self) -> 'PartConfig':
        #  return PartConfig(
        #  manage_name=self.manage_name,
        #  is_skip=self.is_skip,
        #  ts_list=self.ts_list,
        #  nav_title=self.nav_title,
        #  )


class VideoConfig(BaseMongoORM):
    id: str = Field()
    title: str = Field("", title='标题')
    user_id: int = Field(0, title='用户id')
    type: str = Field("", title='类型')
    main_part: PartConfig = Field()
    suffix_parts: List[PartConfig] = Field([])
    with_random_suffix: bool = Field(False, title="是否使用随机后缀")
    with_part_title: bool = Field(False, title="是否使用片段名称")
    album_id: str = Field("", title="专辑")
    episode_id: str = Field("", title="剧集id")
    season: int = Field(0, title="季")
    episode_ids: List[str] = Field([], title="剧集列表")

    parts: List[Part] = Field([], title="片段列表", description="展示用")

    class Meta(BaseMongoORM.Meta):
        TABLE = "video_config"

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['id', 'title', 'album_id', 'type', 'season', 'episode_id']

    @property
    def manage_name(self):
        """The manage_name property."""
        return self.main_part.manage_name

    @property
    def manage(self):
        """The manage_name property."""
        return self.main_part.manage

    @property
    def configs(self) -> List[PartConfig]:
        """The manage_name property."""
        res = [self.main_part]
        for conf in self.suffix_parts:
            res.append(conf)
        return res

    def load(self, user_id: str = "") -> 'VideoConfig':
        # load 配置
        self.main_part.load(user_id)
        for part in self.suffix_parts:
            part.load(user_id)

        m = pm.get_manage(self.main_part.manage_name, '')
        self.parts = []
        configs = [self.main_part]
        configs.extend(self.suffix_parts)

        for conf in configs:
            m = pm.get_manage(conf.manage_name, '')
            for id in conf.ids:
                _parts = m.get_parts_by_id(id)
                self.parts.extend(_parts)

        if not self.album_id:
            self.album_id = self.main_part.manage_name
        return self

    def get_ts_list(self):
        ts = []
        for conf in self.configs:
            #  if conf.ts_list:
            #  ts.extend(conf.ts_list)
            #  continue
            #  ids = conf.ids
            #  if conf.use_random_ids:
            #  ids = conf.manage.get_random_ids(
            #  conf.random_minute,
            #  max_part_duration=conf.max_part_minute * 60)
            #  for id in ids:
            #  parts = conf.manage.get_parts_by_id(id)
            #  for part in parts:
            #  ts.append(conf.manage.get_part_ts(part))

            ts.extend(conf.ts_list)
        return ts

    @classmethod
    def find_configs(
        cls, *,
        album_id: str = '',
        user_id: int = 0,
        season: int = 0,
        type_: str = '',
        episode_id: str = '',
        page: int = 1,
        pagesize: int = 10,
    ):
        q = (
            MongoQuery.default()
            .page(page).pagesize(pagesize).sort('id', 'asc')
        )
        if album_id:
            q.eq('album_id', album_id)
        if user_id:
            q.eq('user_id', user_id)
        if type_:
            q.eq('type', type_)
        if episode_id:
            q.eq('episode_id', episode_id)
        if season:
            q.eq('season', season)

        return cls.find_page_items(q)


def create_pc_rand_music():
    return PartConfig(
        manage_name=const.MANAGE_NAME_MUSIC,
        use_random_ids=True,
        random_minute=1,
        is_skip=True,
    )


def create_pc_rand_lord_loser():
    return PartConfig(
        manage_name=const.MANAGE_NAME_LORD_LOSER,
        use_random_ids=True,
        random_minute=1,
        max_part_minute=3,
        is_skip=True,
    )


def create_pc_rand_movie_song():
    return PartConfig(
        manage_name=const.MANAGE_NAME_MOVIE_SONG,
        is_skip=True,
        use_random_ids=True,
        random_minute=1,
        max_part_minute=3
    )


def create_pc_rand_tom_jerry():
    return PartConfig(
        manage_name=const.MANAGE_NAME_TOM_JERRY,
        is_skip=True,
        use_random_ids=True,
        random_minute=1,
    )


def create_pc_rand_ipart():
    return PartConfig(
        manage_name=const.MANAGE_NAME_IPARTMENT,
        is_skip=True,
        use_random_ids=True,
        random_minute=1,
        max_part_minute=2
    )


def create_pc_rand_long():
    return PartConfig(
        manage_name=const.MANAGE_NAME_LONGMEN,
        is_skip=True,
        use_random_ids=True,
        random_minute=1,
        max_part_minute=3
    )


def create_pc_rand_noge():
    return PartConfig(
        manage_name=const.MANAGE_NAME_NOGE,
        is_skip=True,
        use_random_ids=True,
        random_minute=1,
        max_part_minute=3
    )


def create_pc_rand_opus(is_skip=True):
    return PartConfig(
        manage_name=const.MANAGE_NAME_OPUS,
        is_skip=is_skip,
        use_random_ids=True,
        random_minute=1,
    )


def create_pc_rand(album_id, is_skip=True):
    pc = PartConfig(
        manage_name=album_id,
        is_skip=is_skip,
        use_random_ids=True,
        random_minute=1,
    )
    if album_id in (const.MANAGE_NAME_IPARTMENT):
        pc.max_part_minute = 2
    elif album_id in (
            const.MANAGE_NAME_LONGMEN,
            const.MANAGE_NAME_NOGE,
            const.MANAGE_NAME_OPUS,
            const.MANAGE_NAME_MOVIE_SONG,
            const.MANAGE_NAME_LORD_LOSER,
    ):
        pc.max_part_minute = 3

    return pc


def build_tom_jerry_config(
        bili_name: str, start_ep: int, count: int) -> VideoConfig:
    m_name = const.MANAGE_NAME_TOM_JERRY
    m = pm.get_make_config(bili_name, m_name).get_manage()
    ids = []
    end_ep = 0
    for i in range(count):
        ep = start_ep + i
        end_ep = ep
        id = f"猫{ep:0>3}"
        ids.append(id)
    config = VideoConfig(
        id=f"猫{start_ep}",
        title=f"【{m.Config.title}】{start_ep}-{end_ep}-",
        main_part=PartConfig(
            manage_name=m_name,
            ids=ids,
        ),
        with_random_suffix=True,
        with_part_title=True,
    )
    return config


IPARTMENT_STORY_MAP = {
    const.BILI_NAME_IPART2: {
        "S02E10":
        {
            "title": "今年谁看春晚，谁就",
            "part_ids": ["1-7", "9-10", "12-16"],
        },
    },
    const.BILI_NAME_WXNACY: {
        "S02E04":
        {
            "title": "一菲虐张伟，再战三枪队",
            "part_ids": ["2-4-3"],
        },
        "S02E05":
        {
            "title": "我是个传统的女孩儿，不介意做小",
            "part_ids": ["2-5-2"],
        },
        "S02E08":
        {
            "title": "但是他好帅啊",
            "part_ids": ["2-16"],
        },
        "S02E18":
        {
            "title": "假如关谷把简历投在B站，一定不输坤哥这件事儿",
            "part_ids": ["1-3", "6-10"],
        },
        "S03E02":
        {
            "title": "小貂蝉，欢迎回来",
        },
        "S03E03.1":
        {
            "title": "菠~~萝~~",
            "part_ids": ["1-11"],
        },
        "S03E12":
        {
            "title": "最强特效，决战紫禁之巅",
        },
        "S03E14":
        {
            "title": "",
            "part_ids": ["2-12"],
        },

        "S04E13": {
            "title": "",
            "part_ids": ["1-9"],
        },
        "S04E04":
        {
            "title": "",
            "part_ids": ["1-14"],
        },
        "S04E01":
        {
            "title": "",
            "part_ids": ["1-12"],
        },
    }
}


def build_part_config(album_id: str, auth_user_id: int):
    m = pm.get_manage(album_id, '')
    parts = []
    for part in m.find_parts(pagesize=const.MAX_PAGESIZE).data:
        parts.append(part)
    parts.sort(key=lambda o: o.order)
    part: pm.Part
    for part in parts:
        conf = VideoConfig(
            id=f"{auth_user_id}-{album_id}-{part.order}",
            title=f'{part.id}',
            user_id=auth_user_id,
            type='one_part',
            with_part_title=True,
            main_part=PartConfig(
                manage_name=album_id,
                ids=[part.id],
            ),
            season=part.season,
            album_id=part.manage_name,
            episode_id=part.episode_id,
            suffix_parts=[
                #  create_pc_rand_opus(),
                create_pc_rand_tom_jerry(),
                create_pc_rand_ipart()
            ]
        )
        conf.save()


def init_yixi_mix_part_config(bili_name: str, id: str, title: str, part_ids: list):
    m_name = const.MANAGE_NAME_YIXI
    config = VideoConfig(
        id=f"{bili_name}-{id}",
        title=title,
        main_part=PartConfig(
            manage_name=m_name,
            ids=[part_ids[0]]
        ),
        with_part_title=True,
    )
    for id in part_ids[1:]:
        config.suffix_parts.append(
            PartConfig(
                manage_name=m_name,
                ids=[id]
            )
        )
    config.suffix_parts.append(create_pc_rand_opus(is_skip=False))
    config.suffix_parts.append(create_pc_rand_ipart())
    config.suffix_parts.append(create_pc_rand_long())
    config.suffix_parts.append(create_pc_rand_lord_loser())
    config.suffix_parts.append(create_pc_rand_tom_jerry())
    #  config.suffix_parts.append(create_pc_rand_noge())
    #  config.suffix_parts.append(create_pc_rand_music())
    config.suffix_parts.append(create_pc_rand_movie_song())
    CONFIG_MAP[bili_name].append(config)


def build_ipartment_config(
    bili_name: str,
    episode_id: str,
) -> VideoConfig:
    m_name = const.MANAGE_NAME_IPARTMENT
    m = pm.get_make_config(bili_name, m_name).get_manage()
    ep = m.get_episode(episode_id)
    album = config.get_album(m_name)
    ids = []
    ts_list = []
    story = IPARTMENT_STORY_MAP.get(bili_name, {}).get(ep.id)
    if not story:
        return None
    story_ids = story.get("part_ids")
    if story_ids:
        for id in story_ids:
            split_count = id.count('-')
            if split_count == 1:
                s, e = id.split('-')
                for i in range(int(s), int(e) + 1):
                    ids.append(f"{album.short}{ep.season}.{ep.ep}.{i}")
            elif split_count == 2:
                ids.extend(m.get_story_part_ids(id))
            else:
                ids.append(id)
    else:
        ts_list = [ep.ts]

    title = story.get("title") or ep.title
    conf = VideoConfig(
        id=f"{m_name}-{episode_id}",
        title='【{album}{season}】{ep}-《{title}》'.format(
            title=title,
            **ep.get_format_kwargs()
        ),
        main_part=PartConfig(
            manage_name=m_name,
            ids=ids,
            ts_list=ts_list,
        ),
        suffix_parts=[
            PartConfig(
                manage_name=const.MANAGE_NAME_YIXI,
                use_random_ids=True, random_minute=1, max_part_minute=10
            ),
            PartConfig(
                manage_name=const.MANAGE_NAME_TOM_JERRY,
                use_random_ids=True, random_minute=1
            ),
            PartConfig(
                manage_name=const.MANAGE_NAME_LONGMEN,
                use_random_ids=True, random_minute=1, max_part_minute=3
            ),
            PartConfig(
                manage_name=const.MANAGE_NAME_NOGE,
                use_random_ids=True, random_minute=1, max_part_minute=3
            ),
        ],
        #  with_random_suffix=True,
        #  with_part_title=True,
    )
    return conf


CONFIG_MAP = {
    const.BILI_NAME_WEN: [],
    const.BILI_NAME_XINXIN: [],
    const.BILI_NAME_FEIFEI: [
        VideoConfig(
            id="feifei-gb",
            title='【爱情公寓】曾小贤广播合集',
            main_part=PartConfig(
                manage_name=const.MANAGE_NAME_IPARTMENT,
                ids=[
                    "爱3.15.11_2", "爱4.4.15", "爱1.11.12", "爱2.1.14",
                    "爱5.24.21", "爱6.1.2", "爱6.1.3"]
            ),
            suffix_parts=[PartConfig(
                manage_name=const.MANAGE_NAME_IPARTMENT,
                ids=[
                    "爱3.15.11_2", "爱4.4.15", "爱1.11.12", "爱2.1.14",
                    "爱5.24.21", "爱6.1.2", "爱6.1.3"]
            )
            ]
        ),
    ],
    const.BILI_NAME_IPART2: []
}


class WenConfig():
    pass


CONFIG_MAP[const.BILI_NAME_WEN] = [
    VideoConfig(
        id="wen-gb",
        title='“一菲，你在听？”“我在听，我们都在听”爱情公寓每季一个曾小贤广播鸡汤',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱1.11.12", "爱2.1.14", "爱3.15.11_2",
                 "爱4.4.15", "爱5.24.21", "爱6.1.2", "爱3.1.11"]
        ),
        suffix_parts=[PartConfig(
            manage_name=const.MANAGE_NAME_MOVIE_SONG,
            ids=["曲1.1.10"])
        ]
    ),
    VideoConfig(
        id="wen-1-3-1-loop10",
        title='现在就爱自己，《一切都来得及》单曲循环10遍',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_MUSIC,
            ids=["歌1.3.1"] * 10
        ),
    ),
    VideoConfig(
        id="wen-1-4-1-loop10",
        title='现在《上春山》还来得及吗，单曲循环10遍',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_MUSIC,
            ids=["歌1.4.1"] * 10
        ),
    ),
    VideoConfig(
        id="wen-1-6-1-loop10",
        title='给你们十秒钟时间。《新造的人》（剧场版）循环10遍，助眠版',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_MUSIC,
            ids=["歌1.6.1"] * 10
        ),
    ),
]


class XinxinConfig():
    pass


CONFIG_MAP[const.BILI_NAME_XINXIN] = [
    VideoConfig(
        id="xinxin-l2241",
        title='破S02E24.1-这个胖子子乔得罪过两次',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_LORD_LOSER,
            ts_list=[
                "/Volumes/Getea/bili_cli/part/split/lord_loser/S02E24-6-True/S02E24-rbed.mp4_000.ts"]
        ),
        suffix_parts=[
            PartConfig(
                manage_name=const.MANAGE_NAME_IPARTMENT,
                ids=['爱3.7.8']
            ),
            create_pc_rand_long(),
            create_pc_rand(const.MANAGE_NAME_FEI_CHAI),
        ]
    ),
    VideoConfig(
        id="xinxin-l2242",
        title='破S02E24.2-诺澜你可出来了',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_LORD_LOSER,
            ts_list=[
                "/Volumes/Getea/bili_cli/part/split/lord_loser/S02E24-6-True/S02E24-rbed.mp4_001.ts"]
        ),
        suffix_parts=[
            PartConfig(
                manage_name=const.MANAGE_NAME_IPARTMENT,
                ids=['爱4.6.2']
            ),
            create_pc_rand_long(),
            create_pc_rand(const.MANAGE_NAME_FEI_CHAI),
        ]
    ),
    VideoConfig(
        id="xinxin-l2101",
        title='破S02E10.1-我叫黄辉冯，和宝芝林那个没有任何关系',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_LORD_LOSER,
            ts_list=[
                "/Volumes/Getea/bili_cli/part/split/lord_loser/S02E10-6-True/S02E10-rbed.mp4_000.ts"]
        ),
        suffix_parts=[
            PartConfig(
                manage_name=const.MANAGE_NAME_IPARTMENT,
                ids=['爱4.1.13']
            ),
            create_pc_rand_long(),
            create_pc_rand(const.MANAGE_NAME_FEI_CHAI),
        ]
    ),
]


class IpartConfig():
    pass


class WxnacyConfig():
    pass


CONFIG_MAP[const.BILI_NAME_WXNACY] = [
    VideoConfig(
        id="wxnacy-random-yixi",
        title='【喜剧大赛】今日随机',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            use_random_ids=True,
            random_minute=40
        ),
        suffix_parts=[
            create_pc_rand_opus(),
            create_pc_rand_tom_jerry(),
            create_pc_rand_noge(),
        ],
        #  with_random_suffix=True,
        with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-hs-3-1",
        title='【喜剧大赛】皓史成双系列作品(上)',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            ids=["喜1.2.2"]
        ),
        with_part_title=True,
        suffix_parts=[
            PartConfig(
                manage_name=const.MANAGE_NAME_YIXI,
                ids=["喜1.4.1"]
            ),
            PartConfig(
                manage_name=const.MANAGE_NAME_YIXI,
                ids=["喜1.6.4"]
            ),
            create_pc_rand_opus(is_skip=False),
            create_pc_rand_tom_jerry(),
            create_pc_rand_noge(),
        ]
    ),
    VideoConfig(
        id="wxnacy-x-1-3-2",
        title='喜1.3.2《水煮“三结义”》',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            #  nav_title="",
            ids=["喜1.3.11", "喜1.3.2"]
        ),
        suffix_parts=[
            create_pc_rand_noge(),
            create_pc_rand_tom_jerry(),
            create_pc_rand(const.MANAGE_NAME_FEI_CHAI),
        ]
    ),
    VideoConfig(
        id="wxnacy-hs-6",
        title='【喜剧大赛】皓史成双6部作品',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            #  nav_title="",
            ids=["喜1.2.2", "喜1.4.1"]
        ),
        with_part_title=True,
        suffix_parts=[
            create_pc_rand_opus(),
            PartConfig(
                manage_name=const.MANAGE_NAME_YIXI,
                ids=["喜1.6.4", "喜1.7.1"]
            ),
            create_pc_rand_opus(),
            PartConfig(
                manage_name=const.MANAGE_NAME_YIXI,
                ids=["喜1.10.2", "喜1.11.3"]
            ),
            create_pc_rand_opus(),
            create_pc_rand_ipart(),
            create_pc_rand_long(),
            create_pc_rand_noge(),
            create_pc_rand(const.MANAGE_NAME_FEI_CHAI),
            create_pc_rand_movie_song()
        ]
    ),
    VideoConfig(
        id="wxnacy-ys-4",
        title='【一喜】少爷和我4部作品正确顺序',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            ids=['喜2.12.3', '喜2.6.3', '喜2.9.2', '喜2.2.4']
        ),
        with_random_suffix=True,
        with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-pd-4",
        title='【一喜】胖达人8部作品',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            ids=["喜2.2.6", "喜2.4.5",
                 "喜2.7.4", "pd-3", "喜2.10.4", "喜2.12.4"]
        ),
        with_random_suffix=True,
        with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-mmm-6",
        title='【一喜】某某某6部作品',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            ids=["喜2.12.5", "喜2.8.1", "喜2.8.4",
                 "喜2.1.6", "喜2.9.3", "喜2.5.3"]
        ),
        with_random_suffix=True,
        with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-lsh-3",
        title='【一喜】老师好3部作品',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            ids=["喜2.1.1", "喜2.4.6", "喜2.10.6"]
        ),
        with_random_suffix=True,
        with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-gy-4",
        title='【一喜】小碗管乐4部作品',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            ids=["喜2.2.1", "喜2.6.4", "喜2.12.1", "喜2.10.1"]
        ),
        with_random_suffix=True,
        with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-ds-5",
        title='【一喜】大锁x孙天宇5部作品',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            ids=["ds-5"]
        ),
        with_random_suffix=True,
        with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-sg-4",
        title='【一喜】三狗4部作品',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_YIXI,
            ids=["3g-4"]
        ),
        with_random_suffix=True,
        with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-S03E03-1",
        title='【爱情公寓3】3.1-你们为什么不搬到一起去，捏',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱3.3.1-爱3.3.6"]
        ),
        with_random_suffix=True,
        #  with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-S03E03-2",
        title='【爱情公寓3】3.2-对了，子乔美嘉去哪了',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱3.3.7-爱3.3.11"]
        ),
        with_random_suffix=True,
        #  with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-S03E04-1",
        title='【爱情公寓3】4.1-噗，这就是传说中的雷哥？我还以为红雷呢',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱3.4.1-爱3.4.6"]
        ),
        with_random_suffix=True,
        #  with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-S03E04-2",
        title='【爱情公寓3】4.2-纳尼？拿什么泥',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱3.4.7-爱3.4.11"]
        ),
        with_random_suffix=True,
        #  with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-S03E12-1",
        title='【爱情公寓3】12.1-Lisa：忍不住了，导演快喊卡',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱3.12.1-爱3.12.6"]
        ),
        with_random_suffix=True,
        #  with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-S03E12-2",
        title='【爱情公寓3】12.2-来者何人，报上名来，貂蝉在哪，骑马路上',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱3.12.7-爱3.12.9"]
        ),
        with_random_suffix=True,
        #  with_part_title=True,
    ),
    VideoConfig(
        id="wxnacy-S03E09-1",
        title='【爱情公寓3】9.1-我怎么会怪你呢，小布',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱3.9.1-爱3.9.3"]
        ),
        with_random_suffix=True,
    ),
    VideoConfig(
        id="wxnacy-S03E09-2",
        title='【爱情公寓3】9.2-关谷，上面两个鸽子，下面一只死掉的羊，什么意思',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱3.9.4-爱3.9.7"]
        ),
        with_random_suffix=True,
    ),
    VideoConfig(
        id="wxnacy-S03E10-1",
        title='【爱情公寓3】10.1-你好，我是诺澜',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱3.10.1-爱3.10.6"]
        ),
        with_random_suffix=True,
    ),
    VideoConfig(
        id="wxnacy-S03E10-2",
        title='【爱情公寓3】10.2-曾小贤：怎么会这样？',
        main_part=PartConfig(
            manage_name=const.MANAGE_NAME_IPARTMENT,
            ids=["爱3.10.7-爱3.10.12"]
        ),
        with_random_suffix=True,
    ),
    VideoConfig(
        id="wxnacy-sh-12-2",
        title='三P2',
        main_part=create_pc_rand_ipart(),
        suffix_parts=[
            create_pc_rand_long(),
            create_pc_rand_lord_loser(),
            PartConfig(
                manage_name=const.MANAGE_NAME_MOVIE,
                ts_list=[
                    '/Volumes/Getea/bili_cli/part/split/movie/S2024E03011-12-True/S2024E03011-rbed.mp4_001.ts'
                ],
                nav_title="P2"
            ),
        ],
        album_id=const.MANAGE_NAME_MOVIE
    ),
    VideoConfig(
        id="wxnacy-sh-12-5",
        title='三P5',
        main_part=create_pc_rand_ipart(),
        suffix_parts=[
            create_pc_rand_long(),
            create_pc_rand_lord_loser(),
            PartConfig(
                manage_name=const.MANAGE_NAME_MOVIE,
                ts_list=[
                    '/Volumes/Getea/bili_cli/part/split/movie/S2024E03011-12-True/S2024E03011-rbed.mp4_004.ts'
                ],
                nav_title="P5"
            ),
        ],
        album_id=const.MANAGE_NAME_MOVIE
    ),
]


def get_split_part(album_id, ep_id, part_count, part_num):
    return os.path.join(
        const.get_part_dir(), 'split', album_id,
        f"{ep_id}-{part_count}-True",
        f"{ep_id}-rbed.mp4_00{part_num}.ts"
    )


def init_multi_part_drama(
        bili_name: str, album_id: str, season: int, ep_s: int, ep_e: int,
        ep_count: int, part_count: int, split_count=2):
    album = get_album(album_id)

    # 单集分片数
    #  split_count = 2
    if part_count < split_count:
        split_count = part_count

    if int(part_count / split_count) != part_count / split_count:
        raise Exception("part_count / split_count 必须可以除尽才行")

    def _get_ts_list(ep_id: str, index: int):
        count = int(part_count / split_count)
        ts_list = []
        for i in range(count):
            part_num = count * index + i
            ts = get_split_part(album_id, ep_id, part_count, part_num)
            ts_list.append(ts)
        return ts_list

    for eps in range(ep_s, ep_e+1, ep_count):
        if eps > ep_e:
            break
        #  print('-' * 20, eps)
        ep_str = f"E{eps:0>2}"
        ep_id = f"S{season:0>2}{ep_str}"
        video_title = f"{album.title}{ep_id}-E{eps+ep_count-1:0>2}"
        if ep_count == 1:
            video_title = f"{album.title}{ep_id}"
        config = VideoConfig(
            id=f"{bili_name}-{album_id}-{ep_id}",
            title=video_title,
            main_part=PartConfig(
                manage_name=const.MANAGE_NAME_COMMON,
                is_skip=True,
                ids=['共6.1.5']
            ),
            album_id=album_id,
            season=season,
            suffix_parts=[]
        )
        for ep in range(eps, eps+ep_count):
            ep_str = f"E{ep:0>2}"
            ep_id = f"S{season:0>2}{ep_str}"
            if ep > ep_e:
                break
            config.episode_ids.append(ep_id)
            for index in range(split_count):
                #  print(ep_id, index)
                #  #  config.suffix_parts.append(create_pc_rand_movie_song())
                #  config.suffix_parts.append(create_pc_rand_music())
                #  #  config.suffix_parts.append(create_pc_rand_movie_song())
                #  config.suffix_parts.append(create_pc_rand_music())
                #  config.suffix_parts.append(create_pc_rand_opus())
                #  config.suffix_parts.append(create_pc_rand_ipart())
                #  config.suffix_parts.append(create_pc_rand_long())
                #  config.suffix_parts.append(create_pc_rand_movie_song())

                config.suffix_parts.append(create_pc_rand_tom_jerry())
                config.suffix_parts.append(create_pc_rand_ipart())
                #  config.suffix_parts.append(create_pc_rand_music())
                config.suffix_parts.append(create_pc_rand_long())
                #  config.suffix_parts.append(create_pc_rand_music())
                config.suffix_parts.append(create_pc_rand_noge())
                config.suffix_parts.append(create_pc_rand_opus())
                config.suffix_parts.append(create_pc_rand_ipart())
                #  config.suffix_parts.append(create_pc_rand_music())
                config.suffix_parts.append(create_pc_rand_movie_song())
                config.suffix_parts.append(create_pc_rand_music())
                config.suffix_parts.append(create_pc_rand_music())
                config.suffix_parts.append(create_pc_rand_music())
                config.suffix_parts.append(create_pc_rand_music())
                config.suffix_parts.append(create_pc_rand_music())
                config.suffix_parts.append(create_pc_rand_music())
                config.suffix_parts.append(create_pc_rand_movie_song())
                nav_title = ep_str
                if split_count > 1:
                    nav_title += f".{index+1}"
                episode = album.get_episode(ep_id)
                if episode and episode.title:
                    nav_title += f" {episode.title}"

                ep_conf = PartConfig(
                    manage_name=album_id,
                    nav_title=nav_title,
                    ts_list=_get_ts_list(ep_id, index)
                )
                #  print(ep_conf)
                config.suffix_parts.append(ep_conf)
                #  config.suffix_parts.append(create_pc_rand_ipart())
                #  config.suffix_parts.append(create_pc_rand_music())
        config.suffix_parts.append(create_pc_rand_ipart())
        CONFIG_MAP[bili_name].append(config)


def build_rand_configs(type_rand_parts: List[mod.TypeRandPart]
                       ) -> List[PartConfig]:
    part_configs = []
    tp: mod.TypeRandPart
    for tp in type_rand_parts:
        tp_album_id = ""
        if isinstance(tp, str):
            tp_album_id = tp

        pc = create_pc_rand(tp_album_id)
        part_configs.append(pc)
    return part_configs


def init_single_part_drama(
    bili_name: str, album_id: str, season: int, ep_s: int, ep_e: int,
    use_count: int = 1
):
    album = get_album(album_id)
    ep_s_id = tools.build_episode_id(season, ep_s)
    ep_e_id = tools.build_episode_id(season, ep_e)
    #  print(ep_s_id, ep_e_id)
    episode_s = album.get_episode(ep_s_id)
    episode_e = album.get_episode(ep_e_id)
    ua = get_user_album(album_id, bili_name)

    suffix_parts = build_rand_configs(ua.big_video_suffix)

    config = VideoConfig(
        id=f"{bili_name}-{album_id}-{season}-{ep_s}-{ep_e}",
        title=f"{album.title}{episode_s.episode_id}-{episode_e.ep_str}",
        main_part=suffix_parts[0],
        suffix_parts=suffix_parts[1:],
        album_id=album_id,
        season=season,
    )
    for ep in range(ep_s, ep_e+1, use_count):
        #  ep_str = f"E{ep:0>2}"
        ts_list = []
        nav_titles = []
        for index in range(use_count):
            index_ep = ep + index
            if index_ep > ep_e:
                break
            index_ep_str = f"E{index_ep:0>2}"
            index_ep_id = f"S{season:0>2}{index_ep_str}"
            #  nav_title += f"{index_ep_str} "
            nav_titles.append(index_ep_str)
            ts_list.append(get_split_part(album_id, index_ep_id, 1, 0))

        config.suffix_parts.append(
            PartConfig(
                manage_name=album_id,
                nav_title='-'.join(nav_titles),
                ts_list=ts_list,
            ),
        )
        config.suffix_parts.extend(build_rand_configs(ua.big_video_suffix))
    CONFIG_MAP[bili_name].append(config)


def init_big_bang_config(bili_name: str, season: int, ep_s: int, ep_e: int):

    album_id = const.MANAGE_NAME_BIG_BANG
    #  ua = get_user_album(album_id, bili_name)
    config = VideoConfig(
        id=f"{bili_name}-{album_id}-{season}-{ep_s}-{ep_e}",
        title=f"生活大爆炸S0{season}E{ep_s:0>2}-{ep_e:0>2}",
        main_part=create_pc_rand_tom_jerry(),
        suffix_parts=[]
    )
    for ep in range(ep_s, ep_e+1):
        ep_str = f"E{ep:0>2}"
        ep_id = f"S{season:0>2}{ep_str}"
        config.suffix_parts.append(
            PartConfig(
                manage_name=album_id,
                nav_title=ep_str,
                ts_list=[
                    get_split_part(album_id, ep_id, 1, 0)
                ]
            ),
        )
        config.suffix_parts.append(create_pc_rand_opus())
        config.suffix_parts.append(create_pc_rand_ipart())
        config.suffix_parts.append(create_pc_rand_lord_loser())
        config.suffix_parts.append(create_pc_rand_long())
        config.suffix_parts.append(create_pc_rand_music())
        config.suffix_parts.append(create_pc_rand_music())
        config.suffix_parts.append(create_pc_rand_music())
        config.suffix_parts.append(create_pc_rand_music())
        config.suffix_parts.append(create_pc_rand_music())
        config.suffix_parts.append(create_pc_rand_music())
        config.suffix_parts.append(create_pc_rand_movie_song())
    CONFIG_MAP[bili_name].append(config)


def init_week_hot_music(bili_name: str, year: int, week: int, part_ids: list):
    m_name = const.MANAGE_NAME_MUSIC
    config = VideoConfig(
        id=f"{bili_name}-week-hot-{year}-{week}",
        title=f"【每周热歌】{year}年{week}周",
        main_part=PartConfig(
            manage_name=m_name,
            ids=[part_ids[0]]
        ),

        with_part_title=True,
    )
    for id in part_ids[1:]:
        config.suffix_parts.append(
            PartConfig(
                manage_name=m_name,
                ids=[id]
            )
        )
    CONFIG_MAP[bili_name].append(config)


def init_album_music(bili_name: str, season: int, ep: int, start: int,
                     end: int, title: str):
    m_name = const.MANAGE_NAME_MUSIC
    part_ids = []
    for s in range(start, end+1):
        part_ids.append(f"歌{season}.{ep}.{s}")
        #  print(part_ids)
    config = VideoConfig(
        id=f"{bili_name}-album-{season}-{ep}",
        title=title,
        main_part=PartConfig(
            manage_name=m_name,
            ids=[part_ids[0]]
        ),
        album_id=m_name,
        #  with_part_title=True,
    )
    for id in part_ids[1:]:
        config.suffix_parts.append(
            PartConfig(
                manage_name=m_name,
                ids=[id]
            )
        )
    config.save()


def init_config(bili: BaseBili):
    # 单个片段配置
    for album_id in (
        const.MANAGE_NAME_YIXI,
        const.MANAGE_NAME_TUOKOUXIU,
        const.MANAGE_NAME_XIREN,
    ):
        build_part_config(album_id, bili.auth.mid)

    _configs = CONFIG_MAP.get(bili.auth.bili_name) or []
    for _conf in _configs:
        _conf.album_id = _conf.main_part.manage_name
        _conf.load().save()


def init_vc(auth_user_id: int = 0):
    for bili in get_bilis(auth_user_id):
        init_config(bili)

    #  init_big_bang_config(const.BILI_NAME_XINXIN, 1, 1, 6)
    #  init_big_bang_config(const.BILI_NAME_XINXIN, 1, 7, 12)
    #  init_big_bang_config(const.BILI_NAME_XINXIN, 1, 13, 17)

    # wen
    #  init_week_hot_music(const.BILI_NAME_WEN, 2024, 8, [
        #  '歌1.5.1', '歌1.4.1', '歌2.2.1', '歌2.1.2', '歌2.1.3',
        #  '歌2.3.1', '歌2.1.1', '歌2.1.4', '歌2.1.6', '歌2.1.5'
    #  ])
    #  init_album_music(const.BILI_NAME_WEN, 3, 1, 1, 10,
                     #  "一声喔，开启一个时代。周杰伦首张专辑《JAY》纯享版")
    #  init_album_music(const.BILI_NAME_WEN, 3, 2, 1, 10,
                     #  "2024年《爱在西元前》歌词已过期。周杰伦第2张专辑《范特西》纯享版")
    #  init_single_part_drama(
        #  const.BILI_NAME_WEN, const.MANAGE_NAME_BIG_BANG, 1, 1, 6, 2
    #  )
    #  init_single_part_drama(
        #  const.BILI_NAME_WEN, const.MANAGE_NAME_FEI_CHAI, 1, 1, 5, 1
    #  )

    # xinxin
    #  init_yixi_mix_part_config(
        #  const.BILI_NAME_XINXIN, 'pdr1', "【喜剧】胖达人合集-1.1",
        #  part_ids=["喜1.1.3", "喜1.6.3", "喜1.8.3"]
    #  )
    #  init_yixi_mix_part_config(
        #  const.BILI_NAME_XINXIN, 'pdr2', "【喜剧】胖达人2合集-2.2",
        #  part_ids=["喜2.2.6", "喜2.4.5", "喜2.10.4", "喜2.7.4",  "喜2.12.4"]
    #  )
    #  init_yixi_mix_part_config(
        #  const.BILI_NAME_XINXIN, 'ys-5', "【喜剧】少爷和我系列-2.1",
        #  part_ids=['喜2.2.4', '喜2.9.2', '喜2.6.3', '喜2.12.3', '喜2.7.1']
    #  )
    #  init_multi_part_drama(
        #  'xinxin', const.MANAGE_NAME_LORD_LOSER, 1, 1, 24, 1, 6, split_count=3
    #  )
    #  init_multi_part_drama(
        #  'xinxin', const.MANAGE_NAME_LORD_LOSER, 2, 1, 24, 2, 6
    #  )
    #  init_multi_part_drama(
        #  'xinxin', const.MANAGE_NAME_LANG_YA_BANG, 1, 1, 54, 2, 2
    #  )
    #  init_multi_part_drama(
        #  'xinxin', const.MANAGE_NAME_BIG_BANG, 1, 1, 17, 6, 1
    #  )


#  init()


def get_config(bili_name: str, id) -> VideoConfig:
    return VideoConfig.find_by_id(id)


def make(req: dto.MixtureReqDTO):
    bili_name = req.bili_name
    id = req.ids[0]
    config = [o for o in CONFIG_MAP[bili_name] if o.id == id][0]
    main_m = pm.get_manage(config.main_part.manage_name, bili_name)
    # 初始化配置
    if config.main_part.use_random_ids:
        main_ids = main_m.make_mixture_video(
            "", total_seconds=config.main_part.random_minute * 60,
            with_suffix_video=False, is_get_id=True
        )
        config.main_part.ids = main_ids
    m_name = config.main_part.manage_name
    m_config = pm.get_make_config(bili_name, m_name)
    manage = m_config.get_manage()
    ts = []
    parts = [config.main_part]
    parts.extend(config.suffix_parts)
    for part in parts:
        m = pm.get_manage(part.manage_name, bili_name)
        for id in part.ids:
            parts = m.get_parts_by_id(id)
            for part in parts:
                ts.append(m.get_part_ts(part))

    # 是否使用随机后缀
    if config.with_random_suffix:
        suffix = pm.get_suffix_ts(m_name, bili_name)
        ts.extend(suffix)

    title = config.title
    if config.with_part_title:
        for id in config.main_part.ids:
            for p in m.get_parts_by_id(id):
                title += f"《{p.name}》"
    cachedir = manage.concat_video(ts, title)
    # 复制封面
    for id in config.main_part.ids:
        part = main_m.get_part_by_id(id)
        if part:
            main_m.copy_part_image_to_dir(part, cachedir)

    # 保存历史数据
    #  h = mod.HistoryModel.build(
        #  config.main_part.manage_name, title, part_ids=config.main_part.ids
    #  )

    #  bili = get_bili(bili_name)
    #  bili.save(h)
    #  tools.write_dict(os.path.join(cachedir, f"{h.id}.json"), h.dict())
    return cachedir


def make_story(req: dto.MixtureReqDTO):
    config = pm.get_make_config(req.bili_name, req.manage_name)
    manage = config.get_manage()
    story_id = req.ids[0]
    ids = []
    title = ""
    if story_id in manage.Config.story:
        part_detail = manage.Config.story[story_id]
        ids = part_detail.get("part_ids")
        title = part_detail.get("title")
        #  title = f"{manage.bili_name}-{title}-{str(time.time())}"
    elif story_id in manage.episode_data:
        ep = manage.get_episode(story_id)
        ids = ep.story
        titles = ep.subtitles
        random.shuffle(titles)
        subtitle = titles[0]
        title = config.title_fmt.format(
            album=manage.Config.title,
            season=ep.season,
            episode=ep.ep,
            title=ep.title,
            subtitle=subtitle,
        )
    else:
        ids = [story_id]
        part = manage.get_part_by_id(story_id)
        title = part.name or story_id
        #  title = f"{manage.bili_name}-{story_id}-{str(time.time())}"

    ts = []
    for id in ids:
        ts.append(manage.get_part_ts(manage.get_part_by_id(id)))
    suffix = []
    if req.with_suffix:
        suffix = pm.get_suffix_ts(req.manage_name, req.bili_name)
    ts.extend(suffix)
    path = manage.concat_video(ts, title)
    manage.save_id_used(ids)
    return path


if __name__ == "__main__":
    s = VideoConfig.schema()
    print(s)
