
class SplitVideo():
    TS_COMMON_DIR = "/Users/wxnacy/Movies/视频制作/公共素材/切片"
    TS_EXCESSIVES: list = [
        #  os.path.join(TS_COMMON_DIR, "公用/可以点下一P了.ts"),
        #  os.path.join(TS_COMMON_DIR, "公用/小品《同桌的你》赵本山、小沈阳、王小利、李琳.ts"),
        #  os.path.join(TS_COMMON_DIR, "公用/经典《新白娘子传奇》.ts"),
        #  os.path.join(TS_COMMON_DIR, "公用/感官诉说.ts"),
        os.path.join(TS_COMMON_DIR, "xinxin/切换视频xinxin.ts"),
        #  os.path.join(TS_COMMON_DIR, "wxnacy/切换视频wxnacy.ts"),
    ]
    TS_DIRS: list = [
        #  os.path.join(TS_COMMON_DIR, "龙门镖局切片"),
        #  os.path.join(TS_COMMON_DIR, "破事精英"),
        #  os.path.join(TS_COMMON_DIR, "毛骗"),
        #  os.path.join(TS_COMMON_DIR, "潜伏"),
        #  os.path.join(TS_COMMON_DIR, "鹊刀门传奇"),
        #  os.path.join(TS_COMMON_DIR, "IG"),
        #  os.path.join(TS_COMMON_DIR, "漫长的季节"),
        #  os.path.join(TS_COMMON_DIR, "兰闺喜事"),
        #  os.path.join(TS_COMMON_DIR, "爱情公寓"),
        #  os.path.join(TS_COMMON_DIR, "猫和老鼠"),
    ]
    ext_ts_list: list = []
    name: str
    filename: str
    begin_time: int
    split_time: int = 150
    tmp_dir: str
    tmp_file: str
    ts_filter_name: str = ""

    @classmethod
    def load(cls, filename, begin_time, tmp_dir=""):
        c = cls()
        c.name = filename
        c.filename = os.path.basename(filename).rsplit('.', 1)[0]
        c.begin_time = begin_time
        if not tmp_dir:
            c.tmp_dir = os.path.basename(filename) + str(time.time())
        c.tmp_dir = tmp_dir
        try:
            os.mkdir(c.tmp_dir)
        except Exception:
            pass
        duration = get_duration(c.name)
        tmpfile = os.path.join(c.tmp_dir, "tmp.mp4")
        cut_video(c.name, tmpfile, c.begin_time, duration-c.begin_time)
        c.tmp_file = tmpfile
        return c

    def append_ext_ts(self, ts):
        self.ext_ts_list.append(ts)

    def append_ts_dir(self, ts_dir):
        self.TS_DIRS.append(ts_dir)

    def set_split_time(self, ts):
        self.split_time = ts
        return self

    def set_ts_filter_name(self, name):
        self.ts_filter_name = name
        return self

    def filter_ts(self, dir) -> list:
        return [o for o in os.listdir(dir) if o.endswith(".ts")]

    def run(self):
        ts_files = to_ts_and_split(
            self.tmp_file, self.tmp_file, self.split_time)
        print(ts_files)
        ts_dirs = self.TS_DIRS
        if self.ts_filter_name:
            ts_dirs = [o for o in self.TS_DIRS if self.ts_filter_name not in o]
        print(ts_dirs)
        #  return
        for i, name in enumerate(ts_files):
            num = name.rsplit("_", 1)[-1].split(".")[0]
            name = os.path.join(self.tmp_dir, name)
            names = [name]
            names.extend(self.TS_EXCESSIVES)
            for tmp_ts_dir in ts_dirs:
                ts_path = os.path.join(
                    tmp_ts_dir, self.filter_ts(tmp_ts_dir)[i])
                names.append(ts_path)
            names.extend(self.ext_ts_list)
            #  print(namesk)
            concat_ts_to_mp4(names, os.path.join(
                self.tmp_dir, f"{self.filename}-{num}.mp4"))
            os.remove(name)
        os.remove(self.tmp_file)
