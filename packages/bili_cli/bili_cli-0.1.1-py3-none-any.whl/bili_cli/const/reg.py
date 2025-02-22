#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import re
from bili_cli.const import base
#  from bili_cli.const.base import *

#  class Rex(pydantic.BaseModel):
#  episode_splits: List[str] = pydantic.Field([])


#  REX = {
#  BILI_NAME_WXNACY: {
#  episode_splits
#  }
#  }
def get_manage_identity(album_id, user_id):
    return f"{album_id}-{user_id}"


EPISODE_TITLE_REX_DICT = {
    "album": '(?P<album>[\u4e00-\u9fa5]+)',
    "ab": '(?P<ab>[\u4e00-\u9fa5])',
    "episode": '(?P<album>[\u4e00-\u9fa5]+)',
    "season": '(?P<season>[\\d]*)',
    "ep": "(?P<ep>[\\d]*)",
    "part": '(?P<part>[\\d]*)',
}

COMMON_PART_ID_REX = "^{ab}{season}\\.{ep}\\.{part}".format(**EPISODE_TITLE_REX_DICT)
COMMON_PART_ID_REG = re.compile(COMMON_PART_ID_REX)

# wxnacy
#  REX_WXNACY_MOS_EPISODE_SPLITS = [
#  '^武林外传{ep}.{part}',
#  ]
#  REX_WXNACY_MOVIE_EPISODE_SPLITS = [
#  '^.*P{part}-{season}-{ep}',
#  ]
FMT_WXNACY_MOVIE_PART_TITLE = "{episode}P{part}-{season}-{ep}"

# xinxin
#  REX_XINXIN_IPARTMENT_EPISODE_SPLITS = [
#  '^S{season}E{ep}\\.{part}'
#  ]

# 可以识别出 episode 的正则
REX_EPISODE_SPLITS = {
    #  wxnacy
    get_manage_identity(base.MANAGE_NAME_MOS, base.BILI_NAME_WXNACY):  [
        '^武林外传{ep}.{part}',
    ],
    get_manage_identity(base.MANAGE_NAME_MOVIE, base.BILI_NAME_WXNACY): [
        '^.*P{part}-{season}-{ep}.*',
        '{episode}.{season}年{ep}$',
        '{episode}\\d.{season}年{ep}$',
    ],
    get_manage_identity(base.MANAGE_NAME_IPARTMENT, base.BILI_NAME_WXNACY): [
        '^【爱情公寓{season}】{ep}-',
        '^【爱情公寓{season}】{ep}.{part}-',
        '^【爱{season}】{ep}集P{part}-',
    ],
    #  get_manage_identity(
        #  base.MANAGE_NAME_GSKP,
        #  base.BILI_NAME_WXNACY
    #  ): [
        #  "【狗】{season}E{ep}P{part}",
    #  ],
    get_manage_identity(
        base.MANAGE_NAME_YIXI,
        base.BILI_NAME_WXNACY
    ): [
        "^喜{season}.{ep}.{part}",
    ],

    # wen
    get_manage_identity(base.MANAGE_NAME_IPARTMENT, base.BILI_NAME_WEN): [
        '^【{album}】{season}季{ep}集\\.{part}',
        '^爱{season}.{ep}.{part}',
        '^爱{season}.{ep} {episode} Part{part}',
    ],

    # ipart
    get_manage_identity(base.MANAGE_NAME_IPARTMENT, base.BILI_NAME_IPART): [
        '^爱情公寓{season}\\.{ep}\\.{part}',
    ],
    # ipart2
    #  get_manage_identity(base.MANAGE_NAME_IPARTMENT, base.BILI_NAME_IPART2): [
        #  '爱情公寓{season}E{ep}P{part}-',
        #  '^爱{season}.{ep}.{part}-',
    #  ],

    # xinxin
    get_manage_identity(base.MANAGE_NAME_MOS, base.BILI_NAME_XINXIN): [
        '武S{season:0>2}E{ep:0>2}',
        '武S{season:0>2}E{ep:0>2}.{part}-',
    ],
    get_manage_identity(base.MANAGE_NAME_MOT, base.BILI_NAME_XINXIN): [
        '动S{season:0>2}E{ep:0>2}-',
        '动S{season:0>2}E{ep:0>2}.{part}-',
    ],
    get_manage_identity(base.MANAGE_NAME_LORD_LOSER, base.BILI_NAME_XINXIN): [
        '^S{season}E{ep}\\.{part}',
        '^破S{season}E{ep}.{part}',
        '^破事精英S{season}E{ep}',
    ],
    get_manage_identity(base.MANAGE_NAME_IPARTMENT, base.BILI_NAME_XINXIN): [
        '^爱S{season}E{ep}\\.{part}',
        '^S{season}E{ep}\\.{part}',
        '^S{season}E{ep}-{part}',
        '^爱S{season}E{ep}-{episode}',
    ],
    get_manage_identity(base.MANAGE_NAME_ABANDON, base.BILI_NAME_XINXIN): [
        '废S{season:0>2}E{ep:0>2}',
        '废S{season:0>2}E{ep:0>2}.{part}-',
    ],
}

FMT_SPLIT_TITLE = {
    # wxnacy
    #  get_manage_identity(
        #  base.MANAGE_NAME_MOVIE,
        #  base.BILI_NAME_WXNACY
    #  ):  "{episode}P{part}-{season}-{ep}",
    get_manage_identity(
        base.MANAGE_NAME_IPARTMENT,
        base.BILI_NAME_WXNACY
    #  ):  "【爱情公寓{season}】{ep}.{part}-{episode}",
    ):  "【爱{season}】{ep}集P{part}-{episode}",
    get_manage_identity(
        base.MANAGE_NAME_GSKP,
        base.BILI_NAME_WXNACY
    ):  "【狗】{season}E{ep}P{part}",

    # xinxin
    get_manage_identity(
        base.MANAGE_NAME_LORD_LOSER,
        base.BILI_NAME_XINXIN
    ):  "破S{season:0>2}E{ep:0>2}.{part}-",
    get_manage_identity(
        base.MANAGE_NAME_IPARTMENT,
        base.BILI_NAME_XINXIN
    ):  "爱S{season:0>2}E{ep:0>2}.{part}-",

    # ipart
    get_manage_identity(
        base.MANAGE_NAME_IPARTMENT,
        base.BILI_NAME_IPART
    ):  "爱情公寓{season}.{ep}.{part}-{episode}({part_fmt})",
    # ipart2
    get_manage_identity(
        base.MANAGE_NAME_IPARTMENT,
        base.BILI_NAME_IPART2
    ):  "爱情公寓{season}E{ep}P{part}-{episode}",
}

REX_SEASON_ARCHIVE_TITLES = {
    # wen
    get_manage_identity(
        base.MANAGE_NAME_IPARTMENT,
        base.BILI_NAME_WEN
    ): [
        '^【爱情公寓】{season}季{ep}集\\.{part}',
        '^爱{season}.{ep}.{part}',
    ],

    # ipart
    get_manage_identity(
        base.MANAGE_NAME_IPARTMENT,
        base.BILI_NAME_IPART
    ): [
        '^爱情公寓{season}.{ep}.{part}',
    ],
    # ipart2
    #  get_manage_identity(
        #  base.MANAGE_NAME_IPARTMENT,
        #  base.BILI_NAME_IPART2
    #  ): [
        #  #  '爱情公寓{season}E{ep}P{part}-{episode}',
        #  '^爱情公寓{season}E{ep}P{part}',
        #  '^爱{season}.{ep}.{part}',
    #  ],

    # wxnacy
    get_manage_identity(
        base.MANAGE_NAME_IPARTMENT,
        base.BILI_NAME_WXNACY
    ): [
        '^【爱{season}】{ep}集P{part}',
    ],
    get_manage_identity(
        base.MANAGE_NAME_MOS,
        base.BILI_NAME_WXNACY
    ): [
        '^武林外传{ep}.{part}',
    ],
    get_manage_identity(
        base.MANAGE_NAME_MOVIE,
        base.BILI_NAME_WXNACY
    ): [
        '^.*P{part}-{season}-{ep}',
        '{episode}.{season}年{ep}$',
        '{episode}\\d.{season}年{ep}$',
    ],
    get_manage_identity(
        base.MANAGE_NAME_GSKP,
        base.BILI_NAME_WXNACY
    ): [
        "【狗】{season}E{ep}P{part}",
    ],

    # xinxin
    get_manage_identity(
        base.MANAGE_NAME_LORD_LOSER,
        base.BILI_NAME_XINXIN
    ): [
        '^破S{season}E{ep}.{part}',
        '^S{season}E{ep}.{part}',
        '^破事精英S{season}E{ep}',
    ],
    get_manage_identity(
        base.MANAGE_NAME_IPARTMENT,
        base.BILI_NAME_XINXIN
    ): [
        '^爱S{season}E{ep}.{part}',
        '^S{season}E{ep}.{part}',
        '^S{season}E{ep}-{part}',
    ],
    get_manage_identity(
        base.MANAGE_NAME_MOS,
        base.BILI_NAME_XINXIN
    ): [
        '武S{season:0>2}E{ep:0>2}-',
        '武S{season:0>2}E{ep:0>2}.{part}-',
    ],
    get_manage_identity(
        base.MANAGE_NAME_MOT,
        base.BILI_NAME_XINXIN
    ): [
        '动S{season:0>2}E{ep:0>2}-',
        '动S{season:0>2}E{ep:0>2}.{part}-',
    ],
    get_manage_identity(
        base.MANAGE_NAME_ABANDON,
        base.BILI_NAME_XINXIN
    ): [
        '废S{season:0>2}E{ep:0>2}',
        '废S{season:0>2}E{ep:0>2}.{part}-',
        #  '动S{season:0>2}E{ep:0>2}.{part}-',
    ],
}


def get_season_archive_titles(album_id, user_id):
    return REX_SEASON_ARCHIVE_TITLES.get(
        get_manage_identity(album_id, user_id)) or []

if __name__ == "__main__":
    m = COMMON_PART_ID_REG.match('喜1.6.4-sdfs_sfwef.png')
    print(m.groupdict())
