# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-02-28 16:39:32
@describe 批量从视频中提取音频
"""
import json
import os
from datetime import datetime

import ffmpeg


class VideoExtractAudio:
    def __init__(self, in_path: str, output_suffix: str = "mp3"):
        """
        从视频中提取音频
        :param in_path: 视频文件地址或者视频文件目录
        :param output_suffix: 音频文件后缀
        """
        self.in_path = in_path
        self.output_suffix = output_suffix
        self.no = 0

    def extract(self):
        if not self.in_path:
            raise Exception("in_path is not empty")

        abs_in_path = os.path.abspath(self.in_path)
        if os.path.isfile(abs_in_path):
            root, filename = os.path.split(abs_in_path)
            pure_filename, ext = os.path.splitext(filename)
            print(abs_in_path, root, pure_filename, ext)
            self.extract_audio(abs_in_path, os.path.join(root, fr"{pure_filename}.{self.output_suffix}"))
            return

        if os.path.isdir(abs_in_path):
            for root, dirs, files in os.walk(abs_in_path):
                for filename in files:
                    pure_filename, ext = os.path.splitext(filename)
                    self.extract_audio(os.path.join(root, filename), os.path.join(root, fr"{pure_filename}.{self.output_suffix}"))

    def extract_audio(self, in_path: str, out_path: str):
        self.no += 1
        log_msg = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "",
            "no": self.no,
            "cmd": fr"ffmpeg -i {in_path} -vn -map 0:a:0 -loglevel quiet {out_path}",
            "file": in_path,
        }

        try:
            log_msg["status"] = "success"
            ffmpeg.input(in_path).output(out_path, vn=None, map="0:a:0", loglevel="quiet").run(
                overwrite_output=True, capture_stdout=True)
        except Exception as e:
            log_msg["status"] = "failed"
            print(e)
        finally:
            print(json.dumps(log_msg, ensure_ascii=False))


if __name__ == "__main__":
    test_in_path = rf"E:\tools\软件包\视频素材\火影忍者ol手游\背景音乐"
    video_extract_audio = VideoExtractAudio(in_path=test_in_path)
    video_extract_audio.extract()
