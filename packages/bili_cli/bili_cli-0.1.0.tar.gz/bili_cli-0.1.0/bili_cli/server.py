#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


import time
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from bili_cli.part.base import Part
from bili_cli.part.manage import get_manage
from bili_cli import mod, dto
from bili_cli.main import BILI_WEN, BILI_XINXIN, BILI_WXNACY, BILI_IPART
from bili_cli.const import BILI_NAME
from bili_cli import const, make, sche
from bili_cli.bili import get_bili
from bili_cli.config import get_album, get_albums
from bili_cli.manage import Manage, init_db
from bili_cli import manage as bm
from bili_cli.base import MongoQuery
from .routes import include_router
from .middlewares import LoggerMiddleware
from .config import settings


app = FastAPI()

#  IPART = IpartmentManage(bili_name="xinxin").load()

#  app.mount("/static/part", StaticFiles(directory=IPART.part_dir), name="part")

origins = [
    "http://localhost:9527",
    "http://192.168.1.6:9527",
    "http://192.168.0.112:9527",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggerMiddleware)

include_router(app)


@app.get("/album/{album_id}/season")
def get_album_seasons(album_id):
    album = get_album(album_id)
    seasons = album.get_seasons()
    return dto.BaseResDTO(data={"seasons": seasons, "total": len(seasons)})


@app.get("/manage")
def get_manages():
    from bili_cli.part.manage import get_manages
    res = []
    for manage in get_manages():
        res.append(dto.ManageResDTO(
            id=manage.Config.name, title=manage.Config.title))

    return dto.BaseResDTO(data={"manages": res, "total": len(res)})


@app.get("/manage/split")
def split_video(
    path: str,
    manage_name: str = const.MANAGE_NAME_IPARTMENT,
    bili_name: str = BILI_NAME,
    prefix: str = "",
    start_time: int = 0,
    split_time: int = 0,
    count: int = 5,
    is_remove_bed: bool = True,
    is_average: bool = True,
    with_suffix: bool = True,
    use_custom_title: bool = False,
):
    from bili_cli.part.manage import split_video
    req = dto.SplitReqDTO.default()
    req.manage_name = manage_name
    req.bili_name = bili_name
    req.path = path
    req.prefix = prefix
    req.start_time = start_time
    req.split_time = split_time
    req.count = count
    req.is_remove_bed = is_remove_bed
    req.is_average = is_average
    req.with_suffix = with_suffix
    req.use_custom_title = use_custom_title
    paths = split_video(req)
    return dto.BaseResDTO(data=paths)


@app.get("/chart/income")
def chart_incomes(
):
    from bili_cli.dto import INCOME_CHART_RES_MAP
    from bili_cli.bili.bili import get_bili
    #  bilis = [BILI_WEN, BILI_WXNACY, BILI_XINXIN, BILI_IPART]
    series = []
    dates = []
    query = MongoQuery.build(mod.DaliyIncomModel).sort('date', 'desc').pagesize(7)
    for name in const.BILI_NAMES:
        bili = get_bili(name)
        result = bili.find_page_items(query)
        data = result.data
        data.sort(key=lambda o: o.date)
        dto = INCOME_CHART_RES_MAP[bili.Meta.NAME]
        dto.data = [o.amt for o in data]
        series.append(dto)
        #  income_res = []
        if not dates:
            for day in data:
                key = day.date.date().isoformat()
                dates.append(key)
    amts = [o.data for o in series]
    total_res = INCOME_CHART_RES_MAP['total']
    total_res.data = list(map(lambda o: sum(o), list(zip(*amts))))
    series.append(total_res)

    data = {
        "series": series,
        "dates": dates
    }

    return {"data": data}


@app.get("/chart/incomes")
def chart_income(
):
    from bili_cli.dto import INCOME_CHART_RES_MAP
    bilis = [BILI_WEN, BILI_WXNACY, BILI_XINXIN, BILI_IPART]
    series = []
    dates = []
    for bili in bilis:
        data = bili.get_daliy_income(days=7, with_play=True)
        dto = INCOME_CHART_RES_MAP[bili.name]
        dto.data = [o.amt for o in data]
        series.append(dto)
        #  income_res = []
        if not dates:
            for day in data:
                key = day.date.date().isoformat()
                dates.append(key)
    amts = [o.data for o in series]
    total_res = INCOME_CHART_RES_MAP['total']
    total_res.data = list(map(lambda o: sum(o), list(zip(*amts))))
    series.append(total_res)

    data = {
        "series": series,
        "dates": dates
    }

    return {"data": data}


@app.get("/video/config")
async def get_video_configs(
    bili_name: str = const.BILI_NAME_WXNACY,
    manage_name: str = const.MANAGE_NAME_IPARTMENT,
    season: int | str = "0",
    page: int = 1, pagesize: int = 10,
):
    if season:
        season = int(season)

    q = (
        MongoQuery.build(make.VideoConfig).eq('album_id', manage_name)
        .pagesize(pagesize).page(page)
    )
    if season:
        q.eq('season', season)
    print(q)
    print(q.conditions)
    #  return q.conditions
    data = await make.VideoConfig.find_page_items(q)
    configs = [o.load() for o in data.data]

    return dto.BaseResDTO(data={"configs": configs, "total": data.total})


@app.get("/video/config/{id}.json")
def get_video_config_json(
    id: str,
    bili_name: str = const.BILI_NAME_WXNACY,
):
    #  from bili_cli import sche
    item = make.get_config(bili_name, id)
    return dto.BaseResDTO(data=item)


@app.get("/video/config/make")
def make_video_config(
    id: str,
    manage_name: str,
    bili_name: str,
):
    res = bm.make_video_by_config(manage_name, bili_name, id)
    return dto.BaseResDTO(data=res)


@app.post("/archive/update")
def update_archive(
    req: dto.ArchiveEditDTO,
    bili_name: str = const.BILI_NAME_WXNACY,
):
    bili = get_bili(bili_name)
    print(bili.Meta.NAME)
    return bili.update_archive(req)


@app.get("/archive/reply/top")
def reply_archive_top(
    bvid: str,
    bili_name: str = const.BILI_NAME_WXNACY,
    #  manage_name: str = const.MANAGE_NAME_IPARTMENT,
):
    bili = get_bili(bili_name)
    arc: mod.ArcAuditModel = bili.find_by_id(bvid, mod.ArcAuditModel)
    m = Manage.build(arc.ext.album_id, bili_name)
    res = m.reply_archive(bvid, message="")
    if res.is_success:
        print(res.reply.rpid, res.reply.content.message)
        return m.bili.reply_top(res.reply.rpid, 1)
    else:
        return res


@app.get("/archive/reply/card")
def reply_archive(
    bvid: str,
    bili_name: str = const.BILI_NAME_WXNACY,
    #  manage_name: str = const.MANAGE_NAME_IPARTMENT,
):
    bili = get_bili(bili_name)
    arc: mod.ArcAuditModel = bili.find_archive(bvid)
    m = Manage.build(arc.ext.album_id, bili_name)
    return m.reply_archive_card(bvid)


@app.get("/archive/reply")
def reply_archive(
    bvid: str,
    message: str = "",
    bili_name: str = const.BILI_NAME_WXNACY,
    #  manage_name: str = const.MANAGE_NAME_IPARTMENT,
):
    bili = get_bili(bili_name)
    arc: mod.ArcAuditModel = bili.find_by_id(bvid, mod.ArcAuditModel)
    if not arc.ext.album_id:
        if not message:
            return dto.BaseResDTO.default_error(message="找不到归属，无法快评")
        else:
            return bili.reply_add(arc.bvid, message)
    m = Manage.build(arc.ext.album_id, bili_name)
    return m.reply_archive(bvid, message=message)


@app.get("/archive/refresh/ext")
def refresh_archive_ext(
    bvid: str,
    manage_name: str,
    bili_name: str,
):
    bili = get_bili(bili_name)
    m = Manage.build(manage_name, bili_name)
    arc: mod.ArcAuditModel = bili.find_by_id(bvid, mod.ArcAuditModel)
    res = m.refresh_archive_ext(arc)
    res = m.refresh_archive_history_id(arc)
    return dto.BaseResDTO(data=res)


@app.get("/archive/refresh_by_season")
def refresh_archive_by_season(
    season_title: str,
    manage_name: str,
    bili_name: str,
):
    bili = get_bili(bili_name)
    result = bili.find_archives(season_title_eq=season_title)
    data = []
    for arch in result.data:
        if arch.is_lock:
            continue
        res = bili.get_archive(arch.bvid)
        title = res.arc_audit.title
        item = {
            "title": title,
            "state": res.arc_audit.archive.state,
            "state_desc": res.arc_audit.archive.state_desc,
        }
        print(time)
        data.append(item)
        time.sleep(20)

    return dto.BaseResDTO(data=data)


@app.get("/archive/submit/card")
def submit_archive_card(
    bvid: str,
    bili_name: str,
):
    bili = get_bili(bili_name)
    return bili.submit_archive_card(bvid)


@app.get("/archive/card/{bvid}.json")
def get_archive_card_json(
    bvid: str,
    bili_name: str = const.BILI_NAME_WXNACY,
):
    #  from bili_cli import sche
    bili = get_bili(bili_name)
    return bili.get_allcards(bvid)


@app.get("/archive/real")
def get_real_archives(
    page: int = 1, pagesize: int = 10,
    bili_name: str = "wxnacy",
    title: str = "", status: str = const.ARCHIVE_STATUS_ALL,
):

    bili = get_bili(bili_name)
    items = bili.get_archives(page=page, pagesize=pagesize, status=status)
    res = {"archives": items, "total": len(items)}
    return dto.BaseResDTO(data=res)


@app.get("/archive")
def get_archives(
    page: int = 1, pagesize: int = 10,
    manage_name: str = "ipartment",
    bili_name: str = "wxnacy", sort: str = "-ptime",
    title: str = "", status: str = "all",
    season_title: str = ""
):

    bili = get_bili(bili_name)
    state = []
    if status:
        if status == 'pubed':
            state = [0]
        elif status == 'not_pubed':
            state = [-4]
        elif status == 'is_pubing':
            state = [-6, -30, -40]
    result = bili.find_archives(
        title_like=title, season_title_eq=season_title,
        state_in=state, sort=sort,
        page=page, pagesize=pagesize
    )
    res = {"archives": result.data, "total": result.total}
    return dto.BaseResDTO(data=res)


@app.get("/history/{id}.json")
def get_history_json(
    id: str,
):
    item = mod.HistoryModel.find_by_id(id)
    return dto.BaseResDTO(data=item)


@app.get("/season/{id}/sort")
def sort_season(
    id: int,
    bili_name: str = const.BILI_NAME_WXNACY,
):

    bili = get_bili(bili_name)
    bili.season_ep_sort_auto(id)
    return dto.BaseResDTO()


#  @app.get("/season/refresh")
#  def refresh_season(
    #  bili_name: str = const.BILI_NAME_WXNACY,
#  ):
    #  from bili_cli import sche
    #  #  bili = get_bili(bili_name)
    #  return sche.save_season(bili_name)


@app.get("/season/remove_error_episode")
def refresh_season_error_episode(
    id: int,
    bili_name: str,
):

    bili = get_bili(bili_name)
    data = bili.season_remove_error_state_ep(id)
    return dto.BaseResDTO(data=data)


@app.get("/season/create")
def create_season(
    title: str,
    bili_name: str = const.BILI_NAME_WXNACY,
):
    #  from bili_cli import sche
    bili = get_bili(bili_name)
    sea_d = bili.create_season_by_config(title)
    return dto.BaseResDTO(data=sea_d)


@app.get("/season")
def get_seasons(
    page: int = 1, pagesize: int = 10,
    bili_name: str = const.BILI_NAME_WXNACY,
    sort: str = "-mtime",
    keyword: str = ""
):
    bili = get_bili(bili_name)
    items = bili.get_season_configs()
    res = {"seasons": items, "total": len(items)}
    return dto.BaseResDTO(data=res)


@app.get("/section")
def get_sections(season_id: str, bili_name: str):
    bili = get_bili(bili_name)
    q = Query.build(mod.SectionModel).sort('order', 'asc')
    q.eq('season_id', season_id)
    result = bili.find(q)
    res = {"sections": result.data, "total": result.total}
    return dto.BaseResDTO(data=res)


@app.get("/section/del")
def delete_section(section_id: str, bili_name: str):
    bili = get_bili(bili_name)
    return bili.member_api.section_del(section_id)


@app.get("/reply/add")
def reply_add(
    message: str, oid: int, rpid: int = 0,
    bili_name: str = const.BILI_NAME_WXNACY,
):
    bili = get_bili(bili_name)
    return bili.reply_add(oid, message, rpid)


@app.get("/reply/{rpid}.json")
def get_reply_json(
    rpid: int,
    bili_name: str = const.BILI_NAME_WXNACY,
):
    bili = get_bili(bili_name)
    res = bili.find_by_id(str(rpid), mod.ReplyModel)
    return dto.BaseResDTO(data=res)


@app.get("/reply/real/{rpid}.json")
def get_real_reply_json(
    rpid: int,
    bili_name: str = const.BILI_NAME_WXNACY,
):
    bili = get_bili(bili_name)
    replys = bili.get_replys(1, 50)
    items = replys.data.get("list")
    item = {}
    for item in items:
        if item.get("rpid") == rpid:
            return dto.BaseResDTO(data=item)

    return dto.BaseResDTO()


@app.get("/reply/like")
def reply_like(
    rpid: int, action: int,
    bili_name: str = const.BILI_NAME_WXNACY,
):
    bili = get_bili(bili_name)
    return bili.reply_like(rpid, action)


@app.get("/reply/top")
def reply_top(
    rpid: int, action: int,
    bili_name: str = const.BILI_NAME_WXNACY,
):
    bili = get_bili(bili_name)
    return bili.reply_top(rpid, action)


@app.get("/reply/del")
def reply_del(
    rpid: int,
    bili_name: str = const.BILI_NAME_WXNACY,
):
    bili = get_bili(bili_name)
    return bili.reply_del(rpid)


@app.get("/reply/refresh")
def reply_refresh(
    bili_name: str = const.BILI_NAME_WXNACY,
):
    data = sche.save_reply(bili_name=bili_name, page=1)
    return dto.BaseResDTO(data=data)


@app.get("/part/mixture")
def make_mixture(
    bili_name: str, id: str = "", minute=30,
    manage_name: str = const.MANAGE_NAME_IPARTMENT,
):
    from bili_cli.part.manage import make_mixture
    from bili_cli.dto import MixtureReqDTO
    ids = []
    if id:
        ids = id.split(",")
    req = MixtureReqDTO(
        manage_name=manage_name,
        bili_name=bili_name,
        minute=minute,
        ids=ids,
    )
    data = make_mixture(req)
    return data.history[0]


@app.get("/part/story")
def make_story(
    bili_name: str, id: str = "",
    manage_name: str = const.MANAGE_NAME_IPARTMENT,
):
    from bili_cli.part.manage import make_story
    from bili_cli.dto import MixtureReqDTO
    ids = []
    if id:
        ids = id.split(",")
    req = MixtureReqDTO(
        manage_name=manage_name,
        bili_name=bili_name,
        ids=ids,
    )
    data = make_story(req)
    return data.history[0]


@app.get("/part/{id}.json")
def get_part_json(
    id: str, manage_name: str = "ipartment",
    bili_name: str = ""
):
    m = get_manage(manage_name, bili_name)
    part = m.get_part_by_id(id)
    return dto.BaseResDTO(data=part)


@app.get("/part/list")
def part_list(
    page: int = 1, pagesize: int = 10, season: int | str = -1,
    episode: int | str = 0, name: str = "", manage_name: str = "ipartment",
    bili_name: str = "", sort: str = "+order"
):
    try:
        episode = int(episode)
    except Exception:
        episode = 1
    try:
        season = int(season)
    except Exception:
        season = -1

    manage = get_manage(manage_name, bili_name)

    query = (MongoQuery.default().page(page).pagesize(pagesize)
             .eq('manage_name', manage_name)
             .sort('order', 'asc')
             )
    if season != -1:
        #  query['season'] = season
        query.eq('season', season)
    if episode:
        query.eq('ep', episode)
    if name:
        query.like('name', name)
    print('-' * 100)
    print(query.conditions)
    print(query.to_query_ext())
    query_res = mod.PartModel.find_page_items(query)

    for item in query_res.data:
        item.path = manage.get_part_ts(item)
    return dto.BaseResDTO(data={"items": query_res.data, "total": query_res.total})


@app.get("/api/refresh_db")
def refresh_db():
    #  sche.
    print('refresh db')
    init_db()
    return dto.BaseResDTO()


@app.get("/api/move_screenshot")
def move_screenshot():
    print('api move_screenshot')
    res = bm.move_screenshot.delay()
    return dto.BaseResDTO(data=res.id)


@app.post("/part")
def update_part(
    part: Part
):

    ipart = get_manage(part.manage_name, 'xinxin')
    return ipart.save_part(part)


@app.get("/preview")
def preview(
    path: str
):
    import subprocess
    import os
    if os.path.exists(path):
        cmds = ["/usr/bin/qlmanage", "-p", path]
        subprocess.run(cmds, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return {"data": True}
    return {"data": False}


@app.get("/open")
def open(
    path: str
):
    # open -a 指定软件 path
    import subprocess
    import os
    if os.path.exists(path):
        cmds = ["open", path]
        subprocess.run(cmds, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return {"data": True}
    return {"data": False}


@app.get("/show-in-finder")
def show_in_finder(
    path: str
):
    from bili_cli.tools import _show_in_finder
    return {"data": _show_in_finder(path)}


def main():
    import uvicorn
    # workers 和 reload 不能共存
    uvicorn.run("bili_cli.server:app",
                host=settings.SERVER_HOST,
                port=settings.SERVER_PORT,
                reload=True)
    #  uvicorn.run("bili_cli.server:app", host="0.0.0.0", port=8006, workers=4)
