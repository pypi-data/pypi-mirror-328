#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


import inspect
import sys
from typing import List, Dict, Type, Union
from bili_cli import const
from bili_cli.mod import AuthUser
from bili_cli.bili.base import BaseBili
from bili_cli.base import MongoQuery
from bili_cli.tools import logger
from bili_cli.config import (
    SeasonConfig, SectionConfig, SeasonType, get_album, SectionSortType
)


def build_album_season_config(album_id: str, season: int) -> SeasonConfig:
    album = get_album(album_id)
    sea = album.get_season(season)

    return SeasonConfig(
        album_id=album_id,
        season=season,
        cover=sea.cover,
        #  desc='合集内切换下一集，你的点赞是我上传的动力',
        #  no_section=1,
        #  forbid=0,
        ep_count=sea.episode_count,
        type=SeasonType.EPISODE,
        #  section_ep_count=20,
        #  ep_prefix='爱情公寓1',
    )


class Ipart2Bili(BaseBili):
    class Meta(BaseBili.Meta):
        NAME = const.BILI_NAME_IPART2
        DB = f'bili_{NAME}'

        season_configs = [

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 3
            ).enable_forbid().enable_section().set_title(
                '爱3'
            ).set_section_ep_count(10).set_archive_title_rexs([
                '^爱情公寓{season}E{ep}P{part}',
                '^爱{season}.{ep}.{part}',
                '^爱情公寓{season}.{ep}.{part}',
            ]),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 4
            ).enable_forbid().enable_section().set_title(
                '爱4'
            ).set_section_ep_count(12).set_archive_title_rexs([
                '^爱情公寓{season}E{ep}P{part}',
                '^爱{season}.{ep}.{part}',
                '^爱情公寓{season}.{ep}.{part}',
            ]),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 5
            ).enable_section().set_title(
                '爱情公寓5'
            ).set_section_ep_count(12).set_archive_title_rexs_auto(NAME).enable_delete(),

            SeasonConfig(
                title='爱·番外',
                cover=const.IMAGE_SEASON_IPARTMENT7,
                desc='',
                album_id=const.MANAGE_NAME_IPARTMENT,
                type=SeasonType.CUSTOM,
                sections=[
                    SectionConfig(
                        title="辣味英雄传1", season=6, ep_start=1, ep_end=4),
                    SectionConfig(
                        title="辣味英雄传2", season=7, ep_start=1, ep_end=4),
                    SectionConfig(
                        title="开心原力", season=8, ep_start=1, ep_end=4),
                ],
            ).enable_section().set_archive_title_rexs([
                '^爱情公寓{season}E{ep}P{part}',
            ]),
        ]


class IpartBili(BaseBili):
    class Meta(BaseBili.Meta):
        NAME = const.BILI_NAME_IPART
        DB = f'bili_{NAME}'

        season_configs = [
            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 1
            ).enable_section().set_title(
                '爱情公寓1'
            ).set_section_ep_count(20).set_archive_title_rexs_auto(NAME),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 2
            ).enable_section().set_title(
                '爱情公寓2'
            ).set_section_ep_count(20).set_archive_title_rexs_auto(NAME),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 3
            ).enable_section().set_title(
                '爱情公寓3'
            ).set_section_ep_count(20).set_archive_title_rexs_auto(NAME),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 4
            ).enable_section().set_title(
                '爱情公寓4'
            ).set_section_ep_count(24).set_archive_title_rexs_auto(NAME),

        ]


class FeifeiBili(BaseBili):
    class Meta(BaseBili.Meta):
        NAME = 'feifei'
        DB = f'bili_{NAME}'


class WenBili(BaseBili):
    class Meta(BaseBili.Meta):
        NAME = 'wen'
        DB = f'bili_{NAME}'

        season_configs = [

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 3
            ).enable_section().set_title(
                '爱3'
            ).set_section_ep_count(20).set_archive_title_rexs_auto(NAME),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 4
            ).enable_section().set_title(
                '爱4'
            ).set_section_ep_count(24).set_archive_title_rexs_auto(NAME),

            build_album_season_config(
                const.MANAGE_NAME_HUANLE, 1
            ).enable_forbid().enable_section().set_title(
                '欢乐英雄'
            ).set_section_ep_count(20).set_archive_title_rexs([
                "^欢乐英雄{season}.{ep}.{part}",
            ]),

            build_album_season_config(
                const.MANAGE_NAME_LAONONGTANG, 1
            ).enable_forbid().enable_section().set_title(
                '欢笑老弄堂'
            ).set_section_ep_count(15).set_archive_title_rexs([
                "^欢笑老弄堂{season}.{ep}.{part}",
            ]),

            build_album_season_config(
                const.MANAGE_NAME_FAYI, 1
            ).enable_forbid().enable_section().set_title(
                const.ALBUM_FAYI
            ).set_section_ep_count(10).set_archive_title_rexs([
                "^法医秦明{season}.{ep}.{part}",
            ]).set_desc('合集随时被解散，请关注UP'),

            SeasonConfig(
                title='废柴联盟',
                cover='https://archive.biliimg.com/bfs/archive/ca2d0e5a2a497787ea0c94c4b8d058c24d828695.jpg',
                desc='合集随时被解散，关注 UP 吧',
                album_id=const.MANAGE_NAME_FEI_CHAI,
                type=SeasonType.CUSTOM,
                sections=[
                    SectionConfig(
                        title="第一季", season=1, ep_start=1, ep_end=20),
                    SectionConfig(
                        title="第二季", season=2, ep_start=1, ep_end=21),
                    SectionConfig(
                        title="第三季", season=3, ep_start=1, ep_end=21),
                ],
            ).enable_section().enable_forbid().set_archive_title_rexs([
                "废柴兄弟{season}.{ep}.{part}"
            ]),
            SeasonConfig(
                title='万万没想到',
                cover='https://archive.biliimg.com/bfs/archive/6f29b6f0cd44da52ada1c6678d44c26680e21ab7.jpg',
                desc='',
                album_id=const.MANAGE_NAME_WANWAN,
                type=SeasonType.CUSTOM,
                sections=[
                    SectionConfig(
                        title="第一季", season=1, ep_start=1, ep_end=15),
                    SectionConfig(
                        title="第二季", season=1, ep_start=1, ep_end=16),
                ],
            ).enable_section().set_archive_title_rexs([
                "^万万没想到{season}.{ep}.{part}"
            ]),
        ]


class WxnacyBili(BaseBili):
    class Meta(BaseBili.Meta):
        NAME = 'wxnacy'
        DB = f'bili_{NAME}'

        season_configs = [
            SeasonConfig(
                title='喜剧大赛',
                cover='https://archive.biliimg.com/bfs/archive/385db5845359fbe45694a1e879734eab0ff24782.jpg',
                desc='合集随时会被解散，还是关注UP吧',
                album_id=const.MANAGE_NAME_YIXI,
                type=SeasonType.CUSTOM,
                sections=[
                    SectionConfig(
                        title="合集",
                        sort_type=SectionSortType.VIEW_COUNT
                    ).set_archive_title_rexs([
                        '^【喜剧大赛】'
                    ]),
                    SectionConfig(
                        title="第一季", season=1, ep_start=1, ep_end=13),
                    #  SectionConfig(
                    #  title="S2E1-E6", season=2, ep_start=1, ep_end=6),
                    #  SectionConfig(
                    #  title="S2E6-E12", season=2, ep_start=7, ep_end=13),
                ],
            ).enable_section().enable_forbid().set_archive_title_rexs([
                '^喜{season}.{ep}.{part}'
            ]),

            SeasonConfig(
                title='脱口秀大会',
                cover=const.IMAGE_SEASON_TUOKOUXIU,
                desc='合集随时会被解散，还是关注UP吧',
                album_id=const.MANAGE_NAME_TUOKOUXIU,
                type=SeasonType.CUSTOM,
                sections=[
                    SectionConfig(
                        title="第三季", season=3, ep_start=1, ep_end=10),
                ],
            ).enable_section().set_archive_title_rexs([
                '.*【脱口秀大会{season}-{ep}-{part}】$'
            ]),

            SeasonConfig(
                title=const.ALBUM_XIREN,
                cover=const.IMAGE_SEASON_XIREN,
                desc='合集随时会被解散，还是关注UP吧',
                album_id=const.MANAGE_NAME_XIREN,
                type=SeasonType.CUSTOM,
                sections=[
                    SectionConfig(
                        title="第一季", season=1, ep_start=1, ep_end=12),
                ],
            ).enable_section().set_archive_title_rexs([
                '.*【喜人奇妙夜{season}-{ep}-{part}】.*'
            ]),

            build_album_season_config(
                const.MANAGE_NAME_TANG_DRAMA, 2
            ).enable_section().set_title(
                '唐网2'
            ).set_section_ep_count(16).set_archive_title_rexs([
                '唐网{season}.{ep}.{part}',
            ]).enable_delete(),

            SeasonConfig(
                title='三害',
                album_id=const.MANAGE_NAME_MOVIE,
                type=SeasonType.CUSTOM,
                cover=const.IMAGE_SEASON_SANHAI,
                sections=[
                    SectionConfig(
                        title="第一部", ep_ids=['S2024E03011']),
                ]
            ).enable_forbid().enable_section().set_archive_title_rexs([
                'zccsh-P{part}-{season}-{ep}',
            ]),

            SeasonConfig(
                title='灌篮高手',
                album_id=const.MANAGE_NAME_MOVIE,
                type=SeasonType.CUSTOM,
                cover=const.IMAGE_SEASON_GLGS,
                sections=[
                    SectionConfig(
                        title="第一部", ep_ids=['S2023E04201']),
                ]
            ).enable_forbid().enable_section().set_archive_title_rexs([
                'glgsddy-P{part}-{season}-{ep}',
            ]),

            SeasonConfig(
                title='夺宝奇兵',
                album_id=const.MANAGE_NAME_MOVIE,
                type=SeasonType.CUSTOM,
                cover=const.IMAGE_SEASON_DBQB,
                sections=[
                    SectionConfig(
                        title="第一部", ep_ids=['S1981E06121']),
                ]
            ).enable_forbid().enable_section().set_archive_title_rexs([
                'dbqb-P{part}-{season}-{ep}',
                '夺宝奇兵-P{part}-{season}-{ep}',
            ]),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 1
            ).enable_forbid().enable_section().set_title(
                '爱1'
            ).set_section_ep_count(10).set_archive_title_rexs_auto(NAME),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 2
            ).enable_forbid().enable_section().set_title(
                '爱2'
            ).set_section_ep_count(10).set_archive_title_rexs_auto(NAME),

            SeasonConfig(
                title='喜剧电影',
                cover='https://archive.biliimg.com/bfs/archive/1f732280bb73d7242a588947c439bbecbba183c6.jpg',
                desc='手动点击下一个视频，看完整电影',
                album_id=const.MANAGE_NAME_MOVIE,
                type=SeasonType.CUSTOM,
                sections=[
                    SectionConfig(
                        title="黄渤",
                        ep_ids=['S2014E09301', 'S2006E06301']
                    ),
                    SectionConfig(
                        title="非诚勿扰",
                        ep_ids=['S2008E12181', 'S2010E12221', 'S2023E12301']
                    ),
                    SectionConfig(
                        title="周星驰",
                        ep_ids=['S1993E07011', 'S1994E02031',
                                'S1994E03311', 'S1994E09171', 'S2004E12231']
                    ),
                    SectionConfig(
                        title="王宝强",
                        ep_ids=['S2010E06041', 'S2015E12311',
                                'S2018E02161', 'S2021E02121']
                    ),
                ],
            ).enable_section().set_archive_title_rexs([
                '{episode}.{season}年{ep}$',
                '{episode}\\d.{season}年{ep}$',
            ]),
            SeasonConfig(
                title='唐探',
                album_id=const.MANAGE_NAME_MOVIE,
                type=SeasonType.CUSTOM,
                cover='https://archive.biliimg.com/bfs/archive/ac6bd2c7186b4c5fb5ab52329f7a962baeaaf1fc.jpg',
                sections=[
                    SectionConfig(
                        title="第一部", ep_ids=['S2015E12311']),
                ]
            ).enable_section().set_archive_title_rexs([
                '^唐人街探案-P{part}-{season}-{ep}',
                '^唐人街探案2-P{part}-{season}-{ep}',
                '^唐人街探案3-P{part}-{season}-{ep}',
                '^trjta-P{part}-{season}-{ep}',
                '^trjta2-P{part}-{season}-{ep}',
                '^trjta3-P{part}-{season}-{ep}',
            ]),
            SeasonConfig(
                title='沈腾',
                album_id=const.MANAGE_NAME_MOVIE,
                type=SeasonType.CUSTOM,
                cover='https://archive.biliimg.com/bfs/archive/acf44cdc1feba8475e74958f96e998706d3ded62.jpg',
                sections=[
                    SectionConfig(
                        title="飞驰人生", ep_ids=['S2019E02051', 'S2024E02101']),
                ]
            ).enable_section().set_archive_title_rexs([
                '^飞驰人生-P{part}-{season}-{ep}',
                '^fcrs-P{part}-{season}-{ep}',
                '^你好李焕英-P{part}-{season}-{ep}',
                'nhlhy-P{part}-{season}-{ep}',
                '.*【飞驰人生2-P{part}-{season}-{ep}】$',
            ]),

            SeasonConfig(
                title='爱情公寓',
                album_id=const.MANAGE_NAME_IPARTMENT,
                type=SeasonType.CUSTOM,
                cover='https://archive.biliimg.com/bfs/archive/041d90d65c0f70f94a66092b62256db2cf8a190a.jpg',
                sections=[
                    SectionConfig(
                        title="第三季", season=3, ep_start=1, ep_end=20),
                    #  SectionConfig(
                    #  title="第四季", season=4, ep_start=1, ep_end=24),
                ]
                #  desc='手动点击下一个视频，看完整剧集',
            ).enable_section().set_archive_title_rexs([
                '^【{album}{season}】{ep}-'
            ]),
        ]


class XinxinBili(BaseBili):
    class Meta(BaseBili.Meta):
        NAME = 'xinxin'
        DB = f'bili_{NAME}'

        season_configs = [
            #  build_album_season_config(
            #  const.MANAGE_NAME_ABANDON, 1
            #  ).enable_forbid().enable_section().set_title(
            #  '废弃单集（不要订阅）'
            #  ).set_section_ep_count(30).set_archive_title_rexs_auto(NAME),

            build_album_season_config(
                const.MANAGE_NAME_MOS, 1
            ).enable_forbid().enable_section().set_title(
                '武林外传'
            ).set_section_ep_count(10).set_archive_title_rexs_auto(NAME),

            (build_album_season_config(const.MANAGE_NAME_MOT, 1)
             .enable_forbid().enable_section().set_title('动管局')
             .set_desc('本剧版权抓的比较紧，且观看量也不高，后续不再补档')
             .set_section_ep_count(12).set_archive_title_rexs_auto(NAME)
             .enable_delete()
             ),

            build_album_season_config(
                const.MANAGE_NAME_FAYI, 1
            ).enable_forbid().enable_section().set_title(
                const.ALBUM_FAYI
            ).set_section_ep_count(10).set_archive_title_rexs([
                "^法S{season:0>2}E{ep:0>2}.{part}",
            ]),

            SeasonConfig(
                title='生活大爆炸',
                album_id=const.MANAGE_NAME_BIG_BANG,
                type=SeasonType.CUSTOM,
                cover='https://archive.biliimg.com/bfs/archive/f90f47b7980c425ee319ac0d582bb9110efba2c6.jpg',
                sections=[
                    SectionConfig(
                        title="S1", season=1, ep_start=1, ep_end=17),
                ]
            ).enable_section().enable_forbid().set_archive_title_rexs([
                '^生活大爆炸S{season:0>2}E{ep:0>2}',
                '^爆S{season:0>2}E{ep:0>2}',
            ]),

            #  SeasonConfig(
            #  title='喜剧',
            #  album_id=const.MANAGE_NAME_YIXI,
            #  type=SeasonType.CUSTOM,
            #  cover='https://archive.biliimg.com/bfs/archive/00d918ef47f7c813c983f672616c4be3a7025a37.jpg',
            #  sections=[
            #  SectionConfig(
            #  title="合集", season=1, ep_start=1, ep_end=17),
            #  ]
            #  ).enable_section().enable_forbid().set_archive_title_rexs([
            #  '【喜剧】少爷和我系列-2.1',
            #  ]),
            build_album_season_config(
                const.MANAGE_NAME_LANG_YA_BANG, 1
            ).enable_forbid().enable_section().set_title(
                '琅琊榜'
            ).set_section_ep_count(10).set_archive_title_rexs([
                '^琅琊榜S{season:0>2}E{ep:0>2}',
                '^琅S{season:0>2}E{ep:0>2}'
            ]).enable_delete(),

            build_album_season_config(
                const.MANAGE_NAME_LORD_LOSER, 1
            ).enable_forbid().enable_section().set_title(
                '破1'
            ).set_section_ep_count(6).set_archive_title_rexs_auto(NAME).enable_delete(),

            build_album_season_config(
                const.MANAGE_NAME_LORD_LOSER, 2
            ).enable_forbid().enable_section().set_title(
                '破2'
            ).set_section_ep_count(6).set_archive_title_rexs_auto(NAME).enable_delete(),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 5
            ).enable_forbid().enable_section().set_title(
                '爱5'
            ).set_section_ep_count(6).set_archive_title_rexs_auto(NAME),


            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 1
            ).enable_forbid().enable_section().set_title(
                '爱1'
            ).set_section_ep_count(10).set_archive_title_rexs_auto(NAME),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 2
            ).enable_forbid().enable_section().set_title(
                '爱2'
            ).set_section_ep_count(10).set_archive_title_rexs_auto(NAME),

            build_album_season_config(
                const.MANAGE_NAME_IPARTMENT, 3
            ).enable_forbid().set_title(
                '爱3重制'
            ).set_section_ep_count(20).set_archive_title_rexs([
                '^爱S{season}E{ep}-{episode}',
            ]),

            SeasonConfig(
                title='爱3',
                album_id=const.MANAGE_NAME_IPARTMENT,
                season=3,
                cover=const.IMAGE_SEASON_IPARTMENT3,
                no_section=0,
                forbid=1,
                ep_count=24,
                section_ep_count=4,
                ep_prefix='S03E',
            ),
            SeasonConfig(
                title='爱4',
                album_id=const.MANAGE_NAME_IPARTMENT,
                season=4,
                cover=const.IMAGE_SEASON_IPARTMENT4,
                no_section=0,
                forbid=1,
                ep_count=24,
                section_ep_count=4,
                ep_prefix='S04E',
            ),
            SeasonConfig(
                title='爱·番',
                album_id=const.MANAGE_NAME_IPARTMENT,
                season=7,
                cover=const.IMAGE_SEASON_IPARTMENT7,
                no_section=0,
                forbid=1,
                #  ep_count=24,
                #  section_ep_count=4,
                ep_prefix='番',
            ),
            SeasonConfig(
                title='爱·大',
                album_id=const.MANAGE_NAME_IPARTMENT,
                season=6,
                cover=const.IMAGE_SEASON_IPARTMENT6,
                no_section=1,
                forbid=0,
                #  ep_count=24,
                #  section_ep_count=4,
                ep_prefix='盗墓公寓',
            ),
            build_album_season_config(
                const.MANAGE_NAME_LAONONGTANG, 1
            ).enable_forbid().enable_section().set_title(
                '欢笑老弄堂'
            ).set_section_ep_count(10).set_archive_title_rexs([
                '^欢笑老弄堂S{season}E{ep}.{part}',
            ]),
        ]


class DefaultBili(BaseBili):
    class Meta(BaseBili.Meta):
        NAME = 'default'
        DB = f'bili_{NAME}'


BILI_MAP: Dict[str, BaseBili] = {}
BILI_CLZ_MAP: Dict[str, Type[BaseBili]] = {}


def init_bilis():
    clzs = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for name, clz in clzs:
        if clz.__base__.__name__ == 'BaseBili':
            BILI_CLZ_MAP[clz.Meta.NAME] = clz

            #  BILI_MAP[clz.Meta.NAME] = clz().load()


init_bilis()


def get_bili(bid: Union[int, str]) -> BaseBili:
    if isinstance(bid, str):
        return BILI_CLZ_MAP[bid]().load()
    if isinstance(bid, int):
        user = AuthUser.find_by_id(bid)
        return BILI_CLZ_MAP[user.bili_name].build(bid)


DEFAULT_BILI = get_bili('default')


def get_bilis(auth_user_id: int = 0) -> List[BaseBili]:
    for user in AuthUser.find(MongoQuery.default().sort('+mid')):
        if auth_user_id and user.mid != auth_user_id:
            continue
        yield get_bili(user.mid)


def init_season_config():
    for bili in get_bilis():
        for conf in bili.Meta.get_season_configs():
            conf.id = conf.title
            logger.info(f"{bili.log_prefix()} Save: {conf.title}")
            bili.save(conf)

        items = bili.find_items(MongoQuery.build(SeasonConfig))
        item: SeasonConfig
        for item in items:
            sc = bili.Meta.get_season_config(item.title)
            if not sc:
                logger.info(f"{bili.log_prefix()} Delete: {item.id}")
                bili.delete_by_id(item.id, SeasonConfig)
