#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import os

MANAGE_NAME_IPARTMENT = 'ipartment'
MANAGE_NAME_TOM_JERRY = 'tom_jerry'
MANAGE_NAME_YIXI = 'yixi'
MANAGE_NAME_GSKP = 'gskp'
MANAGE_NAME_MOVIE_SONG = 'movie_song'
MANAGE_NAME_LORD_LOSER = 'lord_loser'
MANAGE_NAME_MOS = 'mos'
MANAGE_NAME_MOVIE = 'movie'
MANAGE_NAME_LONGMEN = 'longmen'
MANAGE_NAME_NOGE = 'noge'
MANAGE_NAME_MOT = 'mot'
MANAGE_NAME_OPUS = 'opus'
MANAGE_NAME_COMMON = 'common'
MANAGE_NAME_BIG_BANG = 'big_bang'
MANAGE_NAME_ABANDON = 'abandon'
MANAGE_NAME_MUSIC = 'music'
MANAGE_NAME_LANG_YA_BANG = 'lang_ya_bang'
MANAGE_NAME_TANG_DRAMA = 'tang_drama'
MANAGE_NAME_FEI_CHAI = 'feichai'
MANAGE_NAME_DAWANG = 'dawang'
MANAGE_NAME_SHAOYE = 'shaoye'
MANAGE_NAME_HUANLE = 'huanle'
MANAGE_NAME_FEI_DRAMA = 'fei_drama'
MANAGE_NAME_WANWAN = 'wanwan'
MANAGE_NAME_KUANGBIAO = 'kuang_biao'
MANAGE_NAME_LEI = 'lei'
MANAGE_NAME_ZHUI_FENG = 'zhui_feng'
MANAGE_NAME_LAONONGTANG = 'laonongtang'
MANAGE_NAME_TUOKOUXIU = 'tuokouxiu'
MANAGE_NAME_FAYI = 'fayi'
MANAGE_NAME_XIREN = 'xiren'


class ALBUM():
    IPARTMENT = 'ipartment'
    LONGMEN = 'longmen'
    NOGE = 'noge'
    FEI_CHAI = 'feichai'
    LORD_LOSER = 'lord_loser'


ALBUM_XIREN = '喜人奇妙夜'
ALBUM_FAYI = '法医秦明'
ALBUM_TUOKOUXIU = '脱口秀大会'
ALBUM_LAONONGTANG = '欢笑老弄堂'
ALBUM_ZHUI_FENG = '追风者'
ALBUM_LEI = '泪之女王'
ALBUM_KUANGBIAO = '狂飙'
ALBUM_WANWAN = '万万没想到'
ALBUM_FEI_DRAMA = '飞驰人生网剧'
ALBUM_HUANLE = '欢乐英雄'
ALBUM_SHAOYE = '少爷和我'
ALBUM_DAWANG = '大王别慌张'
ALBUM_FEI_CHAI = '废柴兄弟'
ALBUM_LANG_YA_BANG = '琅琊榜'
ALBUM_TANG_DRAMA = '唐人街探案网剧'
ALBUM_IPARTMENT = '爱情公寓'
ALBUM_LONGMEN = '龙门镖局'
ALBUM_TOM_JERRY = '猫和老鼠'
ALBUM_LORD_LOSER = '破事精英'
ALBUM_YIXI = '一年一度喜剧大赛'
ALBUM_MOS = '武林外传'
ALBUM_MOVIE = '电影'
ALBUM_GSKP = '狗剩快跑'
ALBUM_MOVIE_SONG = '影视歌曲'
ALBUM_MOT = '动物管理局'
ALBUM_OPUS = '小品'
ALBUM_BIG_BANG = '生活大爆炸'
ALBUM_ABANDON = '废弃视频'
ALBUM_MUSIC = '音乐'
ALBUM_NOGE = '王牌对王牌'

ALBUM_CATEGORY_DRAMA = '电视剧'
ALBUM_CATEGORY_MOVIE = '电影'
ALBUM_CATEGORY_VARIETY = '综艺'
ALBUM_CATEGORY_MUSIC = '音乐'
ALBUM_CATEGORY_ANIMATION = '动画'

BILI_NAME_FEIFEI = 'feifei'
BILI_NAME_WXNACY = 'wxnacy'
BILI_NAME_WEN = 'wen'
BILI_NAME_IPART = 'ipart'
BILI_NAME_IPART2 = 'ipart2'
BILI_NAME_XINXIN = 'xinxin'
BILI_NAME = os.getenv("BILI_NAME") or "xinxin"


class USER():
    WXNACY = 'wxnacy'
    XINXIN = 'xinxin'
    WEN = 'wen'


BILI_NAMES = [
    BILI_NAME_WEN,
    BILI_NAME_WXNACY,
    BILI_NAME_FEIFEI,
    BILI_NAME_XINXIN,
    BILI_NAME_IPART,
    BILI_NAME_IPART2,
]

MAX_PAGESIZE = 1000000000
MAX_PAGE = 2000

ARCHIVE_STATUS_ALL = 'is_pubing,pubed,not_pubed'
ARCHIVE_STATUS_NOT_PUBED = 'not_pubed'
ARCHIVE_STATUS_PUBED = 'pubed'
