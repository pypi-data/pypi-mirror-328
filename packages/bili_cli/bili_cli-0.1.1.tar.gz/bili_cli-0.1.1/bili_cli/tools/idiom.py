#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os
from typing import List
import pydantic
from wpy.path import read_dict, write_dict
from wpy.functools import clock
from bili_cli.const import DATA_DIR
from pypinyin import lazy_pinyin
from bili_cli.base import BaseModel
from pydantic import TypeAdapter



ORIGIN_DATA_PATH = os.path.expanduser(
    "~/Documents/Projects/third/chinese-xinhua/data/idiom.json")
IDIOM_PATH = os.path.join(DATA_DIR, "idiom.json")

class IdiomModel(BaseModel):
    word: str = pydantic.Field(title="成语")
    pinyin: str = pydantic.Field("", title="拼音")
    pinyin_list: list = pydantic.Field([], title="拼音")

class Idiom(BaseModel):
    idioms: List[IdiomModel] = pydantic.Field([], title="成语列表")

    def load(self):
        idioms = read_dict(IDIOM_PATH)
        ta = TypeAdapter(List[IdiomModel])
        self.idioms = ta.validate_python(idioms)
        print(self.idioms[0])
        return self

    #  @clock(fmt="[{T:0.8f}s] {F}")
    def find_idioms(self, text, convert_pinyin=False) -> List[IdiomModel]:
        """
        判定文本是否包含成语
        :convert_pinyin 是否转为拼音判定
        """

        if convert_pinyin:
            text += " " + ''.join(lazy_pinyin(text))

        res = []
        idiom: IdiomModel
        for idiom in self.idioms:
            if idiom.word in text or idiom.pinyin in text:
                res.append(idiom)
        return res


@clock()
def init_idiom():
    idioms = read_dict(ORIGIN_DATA_PATH)
    data = []
    for idiom in idioms:
        item = {}
        item['word'] = idiom['word']
        item['pinyin_list'] = lazy_pinyin(idiom['word'])
        item['pinyin'] = ''.join(item['pinyin_list'])
        data.append(item)
        #  print(item)
    write_dict(IDIOM_PATH, data)



if __name__ == "__main__":
    i = Idiom().load()
    items = i.find_idioms("无中生有 qiaosheruhuang")
    print(items)
    #  init_idiom()
