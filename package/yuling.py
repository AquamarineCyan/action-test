#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# yuling.py
"""御灵副本"""

from utils.decorator import *
from utils.function import function
from utils.log import log


class YuLing:
    """御灵副本"""

    def __init__(self, n: int = 0) -> None:
        self.scene_name: str = "御灵副本"
        self.n: int = 0  # 当前次数
        self.max: int = n  # 总次数
        self.resource_path: str = "yuling"  # 路径
        self.resource_list: list = [  # 资源列表
            "title",  # 限时活动特征图像
            "tiaozhan"  # 挑战
        ]

    def title(self) -> bool:
        """场景"""
        flag_title = True  # 场景提示
        while True:
            if function.judge_scene(f"{self.resource_path}/title.png", self.scene_name):
                return True
            elif flag_title:
                flag_title = False
                log.warn("请检查游戏场景", True)

    def start(self) -> None:
        """挑战开始"""
        function.judge_click(f"{self.resource_path}/tiaozhan.png")

    @run_in_thread
    @time_count
    @log_function_call
    def run(self) -> None:
        if self.title():
            log.num(f"0/{self.max}")
            function.random_sleep(1, 3)
            while self.n < self.max:
                function.random_sleep(1, 2)
                # 开始
                self.start()
                # 结束
                function.result()
                function.random_sleep(1, 2)
                # 结算
                function.random_finish_left_right(is_multiple_drops_y=True)
                function.random_sleep(1, 3)
                self.n += 1
                log.num(f"{self.n}/{self.max}")
                # TODO 强制等待，后续优化
                if self.n == 12 or self.n == 25 or self.n == 39 or self.n == 59 or self.n == 73:
                    function.random_sleep(10, 20)
        log.ui(f"已完成 {self.scene_name} {self.n}次")
