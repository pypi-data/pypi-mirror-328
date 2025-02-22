#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import schedule
import inspect
import time
import psutil
import os
from datetime import datetime
from collections import defaultdict
from typing import Callable
from bili_cli.bili import get_bilis, BaseBili
from bili_cli.video import ffmpeg_utils
from bili_cli.part import manage as pm
from bili_cli import manage as bm
from bili_cli.manage import refresh_archive_ext, refresh_episode_archive
from bili_cli.api import DEFAULT_QY_API
from bili_cli.config.celerys import celery_app
from wpy.path import walkfile
from bili_cli.tools import time_statistics
from bili_cli.cmd.archive import refresh_archive
from bili_cli.cmd.season import refresh as refresh_season

BILIS = get_bilis()


#  @time_statistics
#  def save_income():
    #  for bili in BILIS:
        #  try:
            #  incomes = bili.get_daliy_income(days=30)
            #  logger.info(f"{bili.log_prefix()} income {[o.income for o in incomes]}")
        #  except Exception as e:
            #  print(e)


def _iter_bili_save(func: Callable[[BaseBili], int], inclue_names: list = [], **kwargs):
    print(func)
    data = defaultdict(int)
    for bili in BILIS:
        name = bili.Meta.NAME
        if inclue_names and name not in inclue_names:
            continue
        print(name)
        try:
            data[name] += func(bili, **kwargs)
        except Exception as e:
            print(name, e)
    return data


def save_reply(bili_name: str = '', page=5):

    def _save_reply(bili: BaseBili, page: int):
        total = 0
        for i in range(page):
            page = i+1
            res = bili.get_replys(page, pagesize=50)
            count = len(res.list)
            total += count
            print(f"{bili.Meta.NAME} {page} replys {count}")
        return total
    inclue_names = []
    if bili_name:
        inclue_names.append(bili_name)
    return _iter_bili_save(_save_reply, inclue_names=inclue_names, page=page)


def move_screenshot():
    #  res = ScheApi.default().get("/api/move_screenshot")
    res = bm.move_screenshot()
    print('move_screenshot', res)


@time_statistics
def init_part_info():
    dir = os.path.join(pm.get_third_part_root(), "split")
    for ts in walkfile(dir):
        if not ts.endswith('.ts'):
            continue
        ffmpeg_utils.get_or_create_video_info(ts, recreate=True)


def send_downline():
    DEFAULT_QY_API.send_parting_line(f"视频下线通知 {datetime.now()}")

    data = {}
    for bili in BILIS:
        count = bili.batch_send_archive_downline_message()
        data[bili.Meta.NAME] = count
    return data


@celery_app.task
def heart(page=1):
    from datetime import datetime
    print(datetime.now().time())
    rss = psutil.Process(os.getpid()).memory_info().rss
    print(f"程序占用内存：{rss / 1024 / 1024} M")
    print(f"page = {page}")
    return rss


def job(page=1):
    from datetime import datetime
    print(datetime.now())


#  schedule.every(10).seconds.do(job)
#  schedule.every(10).minutes.do(job)
#  schedule.every().hour.do(job)
#  schedule.every().day.at("10:30").do(job)
#  schedule.every(5).to(10).minutes.do(job)
#  schedule.every().monday.do(job)
#  schedule.every().wednesday.at("13:15").do(job)
#  schedule.every().minute.at(":17").do(job)

def main():
    import sys
    args = sys.argv[1:]
    if args:
        func_name = args[0]
        for name, func in inspect.getmembers(
                sys.modules[__name__], inspect.isfunction):
            if name == func_name:
                func(*args[1:])
    else:
        #  refresh_archive_ext()
        #  refresh_episode_archive()
        #  time.sleep(5)
        schedule.every(9).seconds.do(heart, page=2)
        schedule.every(5).seconds.do(move_screenshot)
        #  schedule.every(5).hours.do(save_income)
        #  schedule.every().day.at("00:02").do(save_income)
        #  schedule.every().day.at("10:02").do(save_income)
        schedule.every().day.at("04:02").do(init_part_info)
        schedule.every(2).hours.do(save_reply, page=10)
        schedule.every(10).minutes.do(save_reply, page=2)
        schedule.every(30).minutes.do(refresh_archive, total_page=1, print_data=False)
        schedule.every(6).hours.do(refresh_archive, print_data=False)
        schedule.every(11).minutes.do(refresh_archive_ext)
        schedule.every(12).minutes.do(refresh_episode_archive)
        schedule.every(59).minutes.do(send_downline)
        schedule.every(25).minutes.do(refresh_season, print_data=False)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()
