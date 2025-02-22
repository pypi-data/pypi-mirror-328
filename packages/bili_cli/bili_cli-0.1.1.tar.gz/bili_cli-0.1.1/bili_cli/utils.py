#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import re
import os
import shutil
from bili_cli import mod, const
from bili_cli.config.celerys import celery_app


def match_part(reg: re.Pattern | str, title: str) -> mod.MatchPart:
    if isinstance(reg, str):
        reg = re.compile(reg)
    m = reg.match(title)
    if m:
        d = m.groupdict()
        if d and d.get("ep") and d.get("season"):
            p = mod.MatchPart()
            p.album = d.get("album")
            p.episode = d.get("episode")
            p.ab = d.get("ab")
            for k in ('season', 'ep', 'part'):
                val = d.get(k)
                if val:
                    setattr(p, k, int(val))
            return p


def is_match_str(reg: re.Pattern | str, title: str) -> bool:
    if isinstance(reg, str):
        reg = re.compile(reg)
    m = reg.match(title)
    if m:
        return True
    return False


def format_continuous_part_ids(id) -> list:
    parse_ids = []
    id_s, id_e = id.split('-')
    part_s = match_part(const.COMMON_PART_ID_REG, id_s)
    part_e = match_part(const.COMMON_PART_ID_REG, id_e)
    for p in range(part_s.part, part_e.part+1):
        part_s.part = p
        parse_ids.append(part_s.part_id)
    return parse_ids


@celery_app.task
def move_file_to_dir(path, dir):
    shutil.move(path, dir)


def is_init_env() -> bool:
    if os.getenv('BILI_INIT'):
        return True
    return False


if __name__ == "__main__":
    print(is_init_env())
