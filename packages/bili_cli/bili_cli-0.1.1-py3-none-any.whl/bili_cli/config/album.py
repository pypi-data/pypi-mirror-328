#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os
from pydantic import model_validator, Field
from typing import List
from bili_cli import mod, const
from bili_cli.base import BaseModel, BaseMongoORM, MongoQuery


class AlbumSeasonConfig(BaseModel):
    album_id: str = Field("", title="")
    id: int = Field(0, title="季数")
    title: str = Field("", title="名称")
    cover: str = Field("", title="封面")
    episode_count: int = Field(0, title="集数")


class AlbumConfig(BaseMongoORM):
    id: str = Field(title="")
    title: str = Field(title="名称")
    short: str = Field("", title="简称")
    category: str = Field("", title="分类")
    order: int = Field(0, title="排序")
    season_count: int = Field(1, title="季数")
    seasons: List[AlbumSeasonConfig] = Field([], title="季列表")
    episode_data: dict = Field({}, title="剧集数据")
    story: dict = Field({}, title="故事集")

    class Meta(BaseMongoORM.Meta):
        TABLE = "album"

    @model_validator(mode='before')
    def validator_all(cls, values):
        short = values.get('short')
        if not short:
            values['short'] = values['title'][0]
        return values

    @property
    def montage_root(self):
        """剪辑视频根目录"""
        return os.path.join(
            const.get_montage_root(), self.category, self.title
        )

    def get_story(self, story_id) -> dict:
        if self.story:
            return self.story.get(story_id) or {}
        return {}

    def get_story_part_ids(self, story_id) -> list:
        story = self.get_story(story_id)
        return story.get("part_ids") or []

    def find_parts(self):
        return mod.Part.find({"manage_name": self.id})

    def get_episode(self, id) -> mod.EpisodeModel:
        a: AlbumConfig = self.find_by_id(self.id)
        data = a.episode_data.get(id)
        if not data:
            from bili_cli.config.album import get_local_album
            data = get_local_album(self.id).episode_data.get(id)
            if not data:
                return None
        data['id'] = id
        item = mod.EpisodeModel(**data)
        item.album_id = self.id
        item.album = self.title
        item.manage_name = self.id
        season = self.get_season(item.season)
        item.season_title = season.title
        item.path = os.path.join(
            self.montage_root, item.season_title, f"{item.id}.mp4"
        )
        item.ts = os.path.join(
            self.montage_root, item.season_title, f"{item.id}.ts"
        )
        #  print(item)
        return item

    def get_seasons(self) -> List[AlbumSeasonConfig]:
        if not self.seasons:
            self.seasons = self.build_seasons()
        return self.seasons

    def get_season(self, season: int) -> AlbumSeasonConfig:
        for s in self.get_seasons():
            if s.id == season:
                return s

        return self.create_default_season(season)

    def create_default_season(self, season: int) -> AlbumSeasonConfig:
        sea = AlbumSeasonConfig(
            album_id=self.id,
            id=season,
            title=f"{self.title}{season}"
        )
        return sea

    def build_seasons(self) -> List[AlbumSeasonConfig]:
        seasons = []
        for i in range(self.season_count):
            s = i+1
            sea = self.create_default_season(s)
            sea_conf = ALBUM_SEASON_CONFIG.get(self.id, {}).get(s, None)
            if sea_conf:
                if sea_conf.title:
                    sea.title = sea_conf.title
                if sea_conf.cover:
                    sea.cover = sea_conf.cover
                if sea_conf.episode_count:
                    sea.episode_count = sea_conf.episode_count

            if self.id == const.MANAGE_NAME_IPARTMENT:
                if s == 1:
                    sea.episode_count = 20
                    sea.cover = const.IMAGE_SEASON_IPARTMENT1
                elif s == 2:
                    sea.cover = const.IMAGE_SEASON_IPARTMENT2
                    sea.episode_count = 20
                elif s == 3:
                    sea.cover = const.IMAGE_SEASON_IPARTMENT3
                    sea.episode_count = 20
                elif s == 4:
                    sea.cover = const.IMAGE_SEASON_IPARTMENT4
                    sea.episode_count = 24
                elif s == 5:
                    sea.cover = const.IMAGE_SEASON_IPARTMENT5
                    sea.episode_count = 36
                elif s == 6:
                    sea.title = '爱情公寓6·辣味英雄传1'
                    sea.episode_count = 4
                elif s == 7:
                    sea.title = '爱情公寓7·辣味英雄传2'
                    sea.episode_count = 4
                elif s == 8:
                    sea.title = '爱情公寓8·开心原力'
                    sea.episode_count = 4
                elif s == 9:
                    sea.title = '爱情公寓9·盗墓公寓'
                    sea.episode_count = 1
            elif self.id == const.MANAGE_NAME_MOT:
                sea.cover = 'https://archive.biliimg.com/bfs/archive/c528fd7800b6d383b0208083f1e61b8b549cf8ae.jpg'
                sea.episode_count = 24
            elif self.id == const.MANAGE_NAME_GSKP:
                sea.cover = 'https://archive.biliimg.com/bfs/archive/024f6988519cba66084f488561112dcf713fd7cc.jpg'
                sea.episode_count = 24
            elif self.id == const.MANAGE_NAME_MOS:
                sea.cover = 'https://archive.biliimg.com/bfs/archive/c3ccbc0b0506990dffe51bc6188e08875f61e7b5.jpg'
                sea.episode_count = 81
            elif self.id == const.MANAGE_NAME_LORD_LOSER:
                if s == 1:
                    sea.cover = 'https://archive.biliimg.com/bfs/archive/8b9e2b21c77d7e89c546601fb3f6e2e6209e5494.jpg'
                    sea.episode_count = 24
                elif s == 2:
                    sea.cover = 'https://archive.biliimg.com/bfs/archive/8b9e2b21c77d7e89c546601fb3f6e2e6209e5494.jpg'
                    sea.episode_count = 24
            elif self.id == const.MANAGE_NAME_BIG_BANG:
                sea.cover = 'https://archive.biliimg.com/bfs/archive/f90f47b7980c425ee319ac0d582bb9110efba2c6.jpg'
                if s == 1:
                    sea.episode_count = 17
            elif self.id == const.MANAGE_NAME_MOVIE:
                sea.id = 1990 + i
                sea.title = f"{self.title}{sea.id}"
            elif self.id == const.MANAGE_NAME_ABANDON:
                if s == 1:
                    sea.cover = 'https://archive.biliimg.com/bfs/archive/ed94fad67fbf86dfedd9c91ec3f7af7295506f36.jpg'
                    sea.episode_count = 30
            elif self.id == const.MANAGE_NAME_LANG_YA_BANG:
                if s == 1:
                    sea.cover = 'https://archive.biliimg.com/bfs/archive/cbfbef88528f1eeb9f0ae0bb94835f6ff5cd9c03.jpg'
                    sea.episode_count = 54
                    sea.title = "琅琊榜"
                elif s == 2:
                    sea.cover = 'https://archive.biliimg.com/bfs/archive/76967d1abf8cd8e2ff2ffe3c452f846120a7f9fb.jpg'
                    sea.episode_count = 50
                    sea.title = "琅琊榜之风起长林"
            elif self.id == const.MANAGE_NAME_MUSIC:
                if s == 1:
                    sea.title = '影视歌曲1'
                elif s == 2:
                    sea.title = '其他歌手2'
                elif s == 3:
                    sea.title = '周杰伦3'
                elif s == 4:
                    sea.title = '林俊杰4'
                elif s == 5:
                    sea.title = '王力宏5'
            elif self.id == const.MANAGE_NAME_TANG_DRAMA:
                if s == 1:
                    sea.episode_count = 12
                elif s == 2:
                    sea.episode_count = 16
            elif self.id == const.MANAGE_NAME_SHAOYE:
                if s == 1:
                    sea.cover = 'https://archive.biliimg.com/bfs/archive/c11991e26c64c518baa30a67093cc87836512862.jpg'
                    sea.episode_count = 12
            elif self.id == const.MANAGE_NAME_DAWANG:
                if s == 1:
                    sea.cover = 'https://archive.biliimg.com/bfs/archive/ff88f9af8e65f07ca1557388a97ade3274b9865f.jpg'
                    sea.episode_count = 14
            elif self.id == const.MANAGE_NAME_KUANGBIAO:
                if s == 1:
                    sea.cover = 'https://archive.biliimg.com/bfs/archive/5f505438a16ac170b03543d64af48f4f74164a0d.jpg'
                    sea.episode_count = 39
            elif self.id == const.MANAGE_NAME_LAONONGTANG:
                if s == 1:
                    sea.cover = const.IMAGE_SEASON_LAONONGTANG
                    sea.episode_count = 30
            elif self.id == const.MANAGE_NAME_WANWAN:
                if s == 1:
                    sea.episode_count = 15
                    sea.cover = 'https://archive.biliimg.com/bfs/archive/6f29b6f0cd44da52ada1c6678d44c26680e21ab7.jpg'
                elif s == 2:
                    sea.episode_count = 16
                elif s == 3:
                    sea.episode_count = 6
                elif s == 4:
                    sea.episode_count = 6
                    sea.title = '万万没想到之小兵过年'

            seasons.append(sea)
        return seasons


def init_album_episode(
        data: dict, season_count: int, ep_counts: List[int],
) -> dict:
    for s in range(1, season_count+1):
        init_episode(data, season=s, ep_count=ep_counts[s-1])
    return data


def init_episode(
    data: dict,
    *,
    season: int = 1,
    ep_count: int = 1,
    bed: list = None
) -> dict:
    if bed and not isinstance(bed, list):
        raise ValueError(f"bed: {bed} must be list")
    for ep in range(1, ep_count+1):
        episode = mod.EpisodeModel(season=season, ep=ep)
        ep_id = episode.episode_id
        ep_data = data.get(ep_id)
        if not ep_data:
            data[ep_id] = {"title": episode.ep_str}

        if bed and not data[ep_id].get('bed'):
            data[ep_id]['bed'] = bed
    return data


init_episode(const.EPISODE_TUOKOUXIU, season=3, ep_count=10)
init_episode(const.EPISODE_TUOKOUXIU, season=4, ep_count=22)
init_episode(const.EPISODE_FEI_CHAI, season=3, ep_count=21, bed=[(0, 0), (0, 5), (0, 57)])


_albums = [
    AlbumConfig(
        id=const.MANAGE_NAME_IPARTMENT,
        title=const.ALBUM_IPARTMENT,
        short="爱",
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=9,
        episode_data=const.IPARTMENT_DATA,
        story=const.IPARTMENT_PART_DATA
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_LORD_LOSER,
        title=const.ALBUM_LORD_LOSER,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=2,
        episode_data=const.LORDLOSER_DATA,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_TUOKOUXIU,
        title=const.ALBUM_TUOKOUXIU,
        category=const.ALBUM_CATEGORY_VARIETY,
        short="脱",
        season_count=5,
        episode_data=const.EPISODE_TUOKOUXIU,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_FAYI,
        title=const.ALBUM_FAYI,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=const.EPISODE_FAYI,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_FEI_CHAI,
        title=const.ALBUM_FEI_CHAI,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=5,
        episode_data=const.EPISODE_FEI_CHAI,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_XIREN,
        title=const.ALBUM_XIREN,
        category=const.ALBUM_CATEGORY_VARIETY,
        short="奇",
        season_count=1,
        episode_data=init_album_episode({}, 1, [12]),
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_YIXI,
        title=const.ALBUM_YIXI,
        category=const.ALBUM_CATEGORY_VARIETY,
        short="喜",
        season_count=2,
        episode_data=init_album_episode({}, 2, [13, 12]),
        story=const.STORY_YIXI,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_LAONONGTANG,
        title=const.ALBUM_LAONONGTANG,
        short='堂',
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=init_episode(
            const.EPISODE_LAONONGTANG,
            season=1, ep_count=30,
            bed=[(0, 0), (0, "00:01:40"), (0, 150)]),
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_MOVIE,
        title=const.ALBUM_MOVIE,
        short='影',
        category=const.ALBUM_CATEGORY_MOVIE,
        season_count=45,
        episode_data=const.MOVIE_DATA,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_KUANGBIAO,
        title=const.ALBUM_KUANGBIAO,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=init_episode(
            const.EPISODE_KUANGBIAO,
            season=1,
            ep_count=39,
            bed=[(0, 0), (0, "00:01:48"), ("00:43:15", 600)]),
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_LEI,
        title=const.ALBUM_LEI,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=const.EPISODE_LEI,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_SHAOYE,
        title=const.ALBUM_SHAOYE,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=const.EPISODE_SHAOYE,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_WANWAN,
        title=const.ALBUM_WANWAN,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=4,
        episode_data=const.EPISODE_WANWAN,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_TANG_DRAMA,
        title=const.ALBUM_TANG_DRAMA,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=2,
        episode_data=const.EPISODE_TANG_DRAMA,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_DAWANG,
        title=const.ALBUM_DAWANG,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=const.EPISODE_DAWANG,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_LANG_YA_BANG,
        title=const.ALBUM_LANG_YA_BANG,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=2,
        short="琅",
        episode_data=const.EPISODE_LANG_YA_BANG,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_TOM_JERRY,
        title=const.ALBUM_TOM_JERRY,
        category=const.ALBUM_CATEGORY_ANIMATION,
        season_count=1,
        #  episode_data=init_album_episode({}, 2, [30, 30]),
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_LONGMEN,
        title=const.ALBUM_LONGMEN,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        #  episode_data=const.,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_MOT,
        title=const.ALBUM_MOT,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=const.EPISODE_MOT_DATA,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_GSKP,
        title=const.ALBUM_GSKP,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=init_episode(
            const.GSKP_DATA,
            season=1,
            ep_count=24,
            bed=[(0, 0), (0, "00:01:36"), ("00:43:05", 300)]),
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_MOS,
        title=const.ALBUM_MOS,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=const.EPISODE_MOS_DATA,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_MOVIE_SONG,
        title=const.ALBUM_MOVIE_SONG,
        short='曲',
        category=const.ALBUM_CATEGORY_MUSIC,
        season_count=1,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_OPUS,
        title=const.ALBUM_OPUS,
        short='品',
        category=const.ALBUM_CATEGORY_VARIETY,
        season_count=1,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_BIG_BANG,
        title=const.ALBUM_BIG_BANG,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=12,
        short="爆",
        episode_data=const.EPISODE_BIG_BANG_DATA,
        #  episode_data=init_album_episode(
        #  const.EPISODE_BIG_BANG_DATA, 12,
        #  [17, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24],
        #  ),
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_COMMON,
        title='公用',
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_MUSIC,
        title=const.ALBUM_MUSIC,
        short='歌',
        category=const.ALBUM_CATEGORY_MUSIC,
        season_count=10,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_NOGE,
        title=const.ALBUM_NOGE,
        category=const.ALBUM_CATEGORY_VARIETY,
        season_count=8,
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_ABANDON,
        title=const.ALBUM_ABANDON,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=2,
        episode_data=init_album_episode({}, 2, [30, 30]),
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_ZHUI_FENG,
        title=const.ALBUM_ZHUI_FENG,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=init_episode(
            const.EPISODE_ZHUIFENG,
            season=1,
            ep_count=38,
            bed=[(0, 0), (0, "00:02:09"), ("00:43:35", 600)]),
    ),
    AlbumConfig(
        id=const.MANAGE_NAME_HUANLE,
        title=const.ALBUM_HUANLE,
        category=const.ALBUM_CATEGORY_DRAMA,
        season_count=1,
        episode_data=const.EPISODE_HUANLE,
    ),
]

_album_map = {o.id: o for o in _albums}

ALBUM_SEASON_CONFIG = {
    const.MANAGE_NAME_LEI: {
        1: AlbumSeasonConfig(
            cover=const.IMAGE_SEASON_LEI,
        )
    },
    const.MANAGE_NAME_HUANLE: {
        1: AlbumSeasonConfig(
            cover=const.IMAGE_SEASON_HUANLE,
            episode_count=51,
        )
    },
    const.MANAGE_NAME_ZHUI_FENG: {
        1: AlbumSeasonConfig(
            cover=const.IMAGE_SEASON_ZHUI_FENG,
            episode_count=38,
        )
    },
    const.MANAGE_NAME_FAYI: {
        1: AlbumSeasonConfig(
            cover=const.IMAGE_SEASON_FAYI,
            episode_count=20,
        )
    },
}


def get_album(name) -> AlbumConfig:
    item = AlbumConfig.find_by_id(name)
    if not item:
        item = get_local_album(name)
    return item


def get_local_album(name) -> AlbumConfig:
    return _album_map.get(name)


async def async_get_album(name) -> AlbumConfig:
    return await AlbumConfig.async_find_by_id(name)


def get_albums() -> List[AlbumConfig]:
    q = MongoQuery.build(AlbumConfig).sort('order', 'asc')
    return [o for o in AlbumConfig.find_page_items(q).data]


def get_album_ids() -> List[AlbumConfig]:
    return [o.id for o in get_albums()]


def init_album():
    for i, album in enumerate(_albums):
        album.order = i
        album.save()


if __name__ == "__main__":
    album = get_album(const.MANAGE_NAME_FEI_CHAI)
    print(album.id, album.title)
    for part in album.find_parts():
        print(part.id)

    #  e = a.get_episode("S05E36")
    #  print(e)
