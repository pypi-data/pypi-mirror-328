#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import shutil
import subprocess
import time
import pydantic
import random
import ffmpeg
from typing import List, Callable, Tuple, Union, Optional
from datetime import timedelta
from bili_cli.const import CACHE_DIR, PART_DIR
from bili_cli.video.models import Part
from bili_cli import tools
from bili_cli.mod import Video
from bili_cli.tools import logger


def get_or_create_video_info(path, recreate=False) -> Video:
    basename = os.path.basename(path).rsplit(".", 1)[0]
    id = f"{basename}-{tools.md5(path)}"
    video = Video.find_by_id(id)
    if recreate:
        video = None
    if not video:
        video = get_video_info(path)
        video.id = id
        video.save()
    return video


def get_video_info(path) -> Video:
    probe = ffmpeg.probe(path)
    format = probe['format']
    #  print(format)
    data = {}
    data.update(format)
    #  print(probe['streams'])
    video_stream = list(
        filter(lambda o: o['codec_type'] == 'video', probe['streams']))[0]
    #  print(video_stream)
    data.update(video_stream)

    item = Video(**data)
    print(item)
    return item


def get_duration(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    return float(result.stdout)


def split_video(filename, output_prefix: str, begin: int, split_time: int):
    duration = get_duration(filename)
    total = int((duration-begin)/split_time)+1
    results = []
    for i in range(total):
        bt = timedelta(seconds=begin+(i*split_time))
        out = output_prefix+f".{i+1}.mp4"
        cmds = ["ffmpeg",
                "-ss", str(bt),
                "-t", str(timedelta(seconds=split_time)),
                "-i", filename,
                "-c", "copy", out]
        print(
            f"split video {os.path.basename(filename)} {bt} to {os.path.basename(out)}")
        subprocess.run(cmds, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        results.append(out)
    return results


def cut_part(filename: str, output: str, part: Part):
    """剪切片段"""
    cmds = ["ffmpeg",
            "-ss", str(part.start),
            "-t", str(part.time),
            "-i", filename,
            "-c", "copy", output]
    subprocess.run(cmds, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def cut_video(filename: str, output: str, begin: float, split_time: float):
    bt = timedelta(seconds=begin)
    cmds = ["ffmpeg",
            "-ss", str(bt),
            "-t", str(timedelta(seconds=split_time)),
            "-i", filename,
            "-c", "copy", output]
    subprocess.run(cmds, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def to_ts(filename: str, out: str = ""):
    if not out:
        out = filename.rsplit(".", 1)[0] + ".ts"
    #  cmd = f"ffmpeg -y -i {filename} -c copy -vbsf h264_mp4toannexb {out}"
    cmd = f"ffmpeg -i {filename} -codec copy -bsf:v h264_mp4toannexb -f mpegts {out}"
    logger.info(f"mp4 to ts {cmd}")
    subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return out


def to_ts_and_split(filename: str, prefix: str, split_time: int):
    ts_path = to_ts(filename)
    m3u8_path = prefix + ".m3u8"
    cmd = f"ffmpeg -i {ts_path} -c copy -map 0 -f segment -segment_list {m3u8_path} -segment_time {split_time} {prefix}_%3d.ts"
    subprocess.run(cmd.split(), stdout=subprocess.PIPE,
                   stderr=subprocess.STDOUT)
    os.remove(m3u8_path)
    dir = os.path.dirname(prefix) or "./"
    prefix_name = os.path.basename(prefix)
    names = [o for o in os.listdir(dir) if o.startswith(prefix_name+"_")]
    names.sort()
    print("=" * 100)
    print(names)
    print("=" * 100)
    os.remove(ts_path)
    return names


def split_and_to_ts(filename, output_prefix: str, begin: int, split_time: int):
    files = split_video(filename, output_prefix, begin, split_time)
    results = []
    for name in files:
        ts_name = to_ts(name)
        results.append(ts_name)
        os.remove(name)
    return results


def concat_video(names: list, output: str):
    # 拼接视频列表
    lines = []
    for name in names:
        lines.append(f"file '{name}'\n")
    concat_text_file = os.path.join(CACHE_DIR, str(time.time()))
    with open(concat_text_file, 'w') as f:
        f.writelines(lines)
    cmd = f"ffmpeg -f concat -safe 0 -i {concat_text_file} -c copy {output}"
    subprocess.run(cmd.split())
    os.remove(concat_text_file)


def concat_mp4_by_ts(paths: list, output: str):
    ts_list = []
    for path in paths:
        ts = to_ts(path)
        ts_list.append(ts)
    concat_ts_to_mp4(ts_list, output)
    for ts in ts_list:
        os.remove(ts)


def concat_ts_to_mp4(names: list, output: str):
    if not output.endswith(".mp4"):
        output += ".mp4"
    lines = []
    for name in names:
        lines.append(f"file '{name}'\n")
    #  tmpfile = os.path.expanduser(f"~/Downloads/{time.time()}")
    tmpfile = os.path.join(CACHE_DIR, str(time.time()))
    with open(tmpfile, 'w') as f:
        f.writelines(lines)
    cmd = f"ffmpeg -f concat -safe 0 -i {tmpfile} -c copy -bsf:a aac_adtstoasc {output}"
    subprocess.run(cmd.split())
    os.remove(tmpfile)


def format_parts(
    part_data: List[Union[List, Tuple]],
    *,
    duration: Optional[float] = None
) -> List[Part]:
    parts = []
    last_index = len(part_data) - 1
    for i, (start, t) in enumerate(part_data):
        p = Part(start=start, time=t)
        if p.start.seconds == 0 and i != 0 and i != last_index:
            raise ValueError(f"start can not == 0 on index: {i}")
        if p.time.seconds == 0:
            raise ValueError("time can not == 0")
        if p.start.seconds == 0 and i == last_index:
            if not duration:
                raise ValueError("last index start is 0 and duration can not == 0")
            p.start = timedelta(seconds=duration - p.time.total_seconds())

        parts.append(p)
    return parts


def reverse_parts(parts: List[Part], duration: float) -> List[Part]:
    """对视频片段去反"""
    tmp_parts = []
    tmp_parts.append(Part.load(0, 0))
    tmp_parts.extend(parts)
    if parts[-1].start.total_seconds() + parts[-1].time.total_seconds() < duration:
        tmp_parts.append(Part.load(duration, duration + 10))

    leng = len(tmp_parts)
    res = []
    for i in range(leng):
        j = i + 1
        if j == leng:
            break
        p1 = tmp_parts[i]
        p2 = tmp_parts[j]
        ps = p2 - p1
        #  print(ps)
        if not ps:
            continue
        res.append(ps)
    return res


def remove_unnecessary_part(
    filename: str,
    output: str,
    remove_parts: List[Union[Part, List, Tuple]],
    *,
    duration: float = 0,
    tmp_dir=""
):
    """ 删除多余片段"""
    is_remove_tmp = True
    # 如果是传值的临时文件夹，不进行清理
    if tmp_dir:
        is_remove_tmp = False
    if not duration:
        duration = int(get_duration(filename))

    # 对移除片段做格式化
    if not isinstance(remove_parts[0], Part):
        remove_parts = format_parts(remove_parts, duration=duration)
    logger.info(f"remove parts: {remove_parts}")

    # 反转片段，获取要留下的片段
    parts: List[Part] = reverse_parts(remove_parts, duration)
    logger.info(f"leave parts: {parts}")

    if not tmp_dir:
        tmp_dir = os.path.join(
            CACHE_DIR, os.path.basename(filename) + str(time.time()))
    try:
        os.makedirs(tmp_dir)
    except Exception:
        pass
    part_paths = []
    for i, part in enumerate(parts):
        print(part)
        part_output = os.path.basename(filename).replace(".mp4", f"-{i}.mp4")
        part_output = os.path.join(tmp_dir, part_output)
        print(part_output)
        cut_video(filename, part_output, part.start.total_seconds(), part.time.total_seconds())
        part_ts = to_ts(part_output)
        part_paths.append(part_ts)

    #  raise Exception()
    #  concat_video(part_paths, output)
    concat_ts_to_mp4(part_paths, output)
    if is_remove_tmp:
        shutil.rmtree(tmp_dir)


def reduce_resolution(input, output, scale):
    """降低分辨率"""
    scale_dict = {
        1080: "1920:1080"
    }
    scale = scale_dict.get(scale) or scale
    cmd = f"ffmpeg -i {input} -vf scale={scale} {output} -hide_banner"
    print(cmd)
    subprocess.run(cmd.split())


def m3u8_to_mp4(m3u8_path, name):
    dir_name = os.path.dirname(m3u8_path)
    dir_name = os.path.dirname(dir_name)
    to_path = os.path.join(dir_name, f"{name}.mp4")
    cmd = f"ffmpeg -allowed_extensions ALL -i {m3u8_path} -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 {to_path}"

    subprocess.run(cmd.split())


def image_to_mp4(image_rex, framerate: int, output):
    #  cmd = f"ffmpeg -r {r} -i {image_rex} -c:v libx264 -vf 'fps=24,format=yuv420p' {output}"
    #  subprocess.run(cmd.split())
    #  subprocess.run([
    #  "ffmpeg -r {r}",
    #  f"-i {image_rex}", "-c:v libx264",
    #  "-vf 'fps=24,format=yux420p'",
    #  f"out_part"
    #  ])
    ffmpeg.input(
        image_rex, pattern_type='sequence', framerate=framerate
    ).output('pipe:', format='rawvideo', pix_fmt='yuv420p', r=24
             ).run(overwrite_output=True)


def add_countdown_watermark(input: str, output: str, text: str = "倒计时：", countdown=5, position_type="center_top"):
    cache_dir = os.path.join(CACHE_DIR, str(time.time()))
    os.makedirs(cache_dir)
    #  print(cmd)
    info = get_video_info(input)
    duration = info.duration
    split_time = duration-countdown
    print(duration, split_time)
    parts = to_ts_and_split(input, os.path.join(
        cache_dir, "countdown"), split_time)
    # 计算水印位置
    fontsize = 100
    x = 0
    y = 0
    width = info.width
    height = info.height
    if position_type == "center_top":
        x = int(width/2) - (len(text) * fontsize + int(fontsize)/2) / 2
        y = int(height*0.1)
    #  return
    part = [o for o in parts if o.endswith("_001.ts")][0]
    part = os.path.join(cache_dir, part)
    for i in range(countdown):
        content = text + str(countdown-i)
        b = i
        e = b+1
        out_part = part.replace(".ts", f"{i}.ts")
        cmd = f"ffmpeg -i {part} -vf drawtext=fontsize={fontsize}:fontfile=lazy.ttf:text='{content}':x={x}:y={y}:fontcolor=red:enable='between(t,{b},{e})' {out_part}"
        print(cmd)
        part = out_part
        subprocess.run(cmd.split())

    ts_list = [
        os.path.join(cache_dir, "countdown_000.ts"),
        part
    ]
    print(ts_list)
    concat_ts_to_mp4(ts_list, output)


class SplitVideo(pydantic.BaseModel):

    bili_name: str = pydantic.Field(title="站点名称")
    path: str = pydantic.Field(title="视频地址")
    filename: str = pydantic.Field("", title="视频名称")
    tmp_dir: str = pydantic.Field("", title="临时文件夹")
    tmp_file: str = pydantic.Field("", title="临时文件")
    duration: float = pydantic.Field(0, title="视频长度")
    start_time: int = pydantic.Field(0, title="分割开始时间")
    split_time: int = pydantic.Field(0, title="分割时间")
    common_ts_list: list = pydantic.Field([], title="公用切片列表")
    random_ts_list: list = pydantic.Field([], title="随机切片列表")
    suffix_ts_list: list = pydantic.Field([], title="随机切片列表")

    get_suffix: Callable = pydantic.Field(None)

    def load(self):
        self.filename = os.path.basename(self.path).rsplit('.', 1)[0]
        if not self.tmp_dir:
            self.tmp_dir = os.path.join(
                CACHE_DIR, os.path.basename(self.path) + str(time.time()))
        try:
            os.makedirs(self.tmp_dir)
        except Exception:
            pass
        if not self.duration:
            self.duration = get_duration(self.path)
        self.tmp_file = os.path.join(self.tmp_dir, "tmp.mp4")
        part_dir = os.path.join(PART_DIR, self.bili_name)
        default_common_ts = os.path.join(
            part_dir, f"{self.bili_name}-common.ts")
        if os.path.exists(default_common_ts):
            self.common_ts_list = [default_common_ts]
        for _part in os.listdir(part_dir):
            if 'part' in _part and _part.endswith(".ts"):
                self.random_ts_list.append(os.path.join(part_dir, _part))
        return self

    def run(self):
        # 切割临时视频文件
        cut_video(self.path, self.tmp_file, self.start_time,
                  self.duration - self.start_time)
        # 将视频切割为 ts 文件
        ts_files = to_ts_and_split(
            self.tmp_file, self.tmp_file, self.split_time)
        print(ts_files)
        #  return
        for i, name in enumerate(ts_files):
            #  num = name.rsplit("_", 1)[-1].split(".")[0]
            name = os.path.join(self.tmp_dir, name)
            names = [name]
            names.extend(self.common_ts_list)
            if self.get_suffix:
                names.extend(self.get_suffix())
            else:
                random.shuffle(self.random_ts_list)
                names.extend(self.random_ts_list)
            concat_ts_to_mp4(names, os.path.join(
                self.tmp_dir, f"{self.filename}.{i+1}.mp4"))
            os.remove(name)
        os.remove(self.tmp_file)


#  def save_ipartment_data():
    #  from wpy.path import walkfile, write_dict
    #  for path in walkfile("/Users/wxnacy/Movies/电视剧/爱情公寓搞笑切片"):
        #  if not path.endswith(".mp4"):
        #  continue
        #  id = os.path.basename(path).rsplit(".", 1)[0].split('-')[0]
        #  print(id)
        #  video = get_video_info(path)
        #  write_dict(os.path.join(
        #  "/Users/wxnacy/Downloads/bili_cli/data/ipartment/part", id+".json"), video.__dict__)

def mkv_to_mp4(path: str):
    from ffmpeg.nodes import OutputStream
    stream: OutputStream = ffmpeg.input(path)
    #  stream.audio.
    print(stream.audio)
    audio = stream.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
    video = stream.video.hflip()
    out = ffmpeg.output(audio, video, "/Users/wxnacy/Downloads/out.mp4")
    ffmpeg.run(out)
    #  print(stream.)


def concat_audio_to_video(source_video: str, source_audio: str, out_video: str):
    #  cmds = ["ffmpeg",
    #  "-i", source_video,
    #  "-i", source_audio,
    #  "-vcodec copy",
    #  "-acodec copy",
    #  out_video]
    #  subprocess.run(cmds, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    video_stream = ffmpeg.input(source_video)
    audio_stream = ffmpeg.input(source_audio)

# 合并视频和音频到一个输出文件
    stream = ffmpeg.output(video_stream, audio_stream, out_video, vcodec='copy', acodec='copy')
    #  stream = ffmpeg.output(
        #  video_stream,
        #  audio_stream,
        #  out_video,
        #  vcodec='copy',  # 复制视频流，不进行转码
        #  acodec='aac',  # 将音频转码为 AAC 格式
        #  format='mp4',  # 输出格式为 mp4
        #  #  filter_complex='[0:v][1:a]concat=n=1:v=1:a=1'  # 使用 concat 过滤器合并视频和音频
    #  )

    # 执行合并操作
    ffmpeg.run(stream)


if __name__ == "__main__":
    #  concat_video([
        #  '/Users/wxnacy/Movies/音乐/歌3.1.1-可爱女人.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.1.2-完美主义.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.1.3-星晴.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.1.4-娘子.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.1.5-斗牛.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.1.6-黑色幽默.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.1.7-伊斯坦堡.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.1.8-印第安老斑鸠.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.1.9-龙卷风.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.1.10-反方向的钟.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.2.1-爱在西元前.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.2.2-爸，我回来了.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.2.3-简单爱.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.2.4-忍者.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.2.5-开不了口.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.2.6-上海一九四三.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.2.7-对不起.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.2.8-威廉古堡.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.2.9-双截棍.mp4',
        #  '/Users/wxnacy/Movies/音乐/歌3.2.10-安静.mp4',
        #  ], '/Users/wxnacy/Movies/音乐/jay.mp4')
    #  dirname = '/Volumes/Getea/Movies/视频制作/电视剧/爱情公寓/插曲合集/1成品'
    #  video_list = []
    #  for name in os.listdir(dirname):
        #  if not name.endswith('.mp4'):
            #  continue
        #  path = os.path.join(dirname, name)
        #  print(path)
        #  video_list.append(path)

    #  concat_video(video_list, '/Users/wxnacy/Movies/音乐/爱情公寓.mp4')
    cut_video(
        "/Volumes/ZhiTai/影片/漫威里不仅有台词和特效，还有炸裂的眼神！.mp4",
        "/Volumes/ZhiTai/影片/test.mp4",
        0,
        10,
        )
