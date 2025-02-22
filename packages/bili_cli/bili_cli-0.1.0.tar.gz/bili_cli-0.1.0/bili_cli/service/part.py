#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import random
from bili_cli import mod, const, dto, tools
from bili_cli.base import BaseModel, MongoQuery

def get_part_by_type_rand_part(user_id, trp: mod.TypeRandPart) -> mod.PartModel:
    rand_album_id = None
    max_duration = 0
    if isinstance(trp, str):
        trp = mod.PartConfig(album_id=rand_album_id)
    elif isinstance(trp, dict):
        trp = mod.PartConfig(**trp)

    rand_album_id = trp.album_id
    max_duration = trp.max_duration

    # 查询片段使用情况
    part_used = mod.PartUsedModel.find_part_used(rand_album_id, user_id)

    # 查找并拼接使用次数的片段列表
    query = MongoQuery.build(mod.PartModel).eq('manage_name', rand_album_id)
    if max_duration > 0:
        query.lte('info.duration', max_duration)
    part_iter = mod.PartModel.find(query)
    part: mod.PartModel
    parts = []
    for part in part_iter:
        part.used_times = part_used.get_part_used_times(part.id)
        parts.append(part)

    # 按照使用次数排序，并拿到最少使用的次数
    parts.sort(key=lambda o: o.used_times)
    min_used_times = parts[0].used_times

    # 计算各自的权重，最少使用次数的片段最高权重
    weights = []
    for part in parts:
        used_times = part.used_times - min_used_times
        w = 10000 - (used_times * 10000)
        if w < 0:
            w = 0
        weights.append(w)

    rand_part = random.choices(parts, weights=weights, k=1)[0]
    part_used.increment(rand_part.id)
    part_used.save()
    return rand_part


if __name__ == "__main__":
    trp = mod.PartConfig(
        album_id=const.MANAGE_NAME_FEI_CHAI,
        max_duration=120
    )
    p = get_part_by_type_rand_part(const.BILI_NAME_WEN, trp)
    print(p)
