#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# huodong.py
"""限时活动"""


from ..utils.decorator import log_function_call
from ..utils.event import event_thread
from ..utils.function import (
    RESOURCE_FIGHT_PATH,
    check_click,
    check_scene,
    check_scene_multiple_once,
    click,
    finish_random_left_right,
    get_coor_info,
    random_sleep
)
from ..utils.log import logger
from ..utils.mythread import WorkTimer
from .utils import Package


class HuoDong(Package):
    """限时活动"""
    scene_name = "限时活动"
    resource_path = "huodong"
    resource_list: list = [
        "title",
        "start",
    ]
    description = "适配活动「藏金阁楼」\
                    可自行替换 resource/huodong 下的素材"

    @log_function_call
    def __init__(self, n: int = 0) -> None:
        super().__init__(n)
        self._flag_timer_check_start: bool = False

    def title(self) -> bool:
        """场景"""
        flag_title = True  # 场景提示
        while True:
            if event_thread.is_set():
                return
            if check_scene(f"{self.resource_path}/title", self.scene_name):
                return True
            elif flag_title:
                flag_title = False
                logger.ui("请检查游戏场景", "warn")

    def start(self) -> None:
        """开始"""
        check_click(f"{self.resource_path}/start")

    @log_function_call
    def timer_check_start(self):
        coor = get_coor_info(f"{self.resource_path}/title")
        if coor.is_effective:
            self._flag_timer_check_start = True

    def run(self) -> None:
        _g_resource_list: list = [
            f"{self.resource_path}/title",
            f"{RESOURCE_FIGHT_PATH}/finish",
            f"{RESOURCE_FIGHT_PATH}/fail",
            f"{RESOURCE_FIGHT_PATH}/victory",
        ]
        _flag_title_msg: bool = True
        logger.num(f"0/{self.max}")
        logger.info(f"_g_resource_list:{_g_resource_list}")

        while self.n < self.max:
            if event_thread.is_set():
                return
            scene, coor = check_scene_multiple_once(_g_resource_list)
            if scene is None:
                continue

            scene = self.scene_handle(scene)

            if self._flag_timer_check_start:
                self._flag_timer_check_start = False
                logger.ui("进入挑战失败", "error")
                break

            match scene:
                case "title":
                    logger.scene("藏金阁楼")
                    _flag_title_msg = False
                    self.start()
                    random_sleep()
                    _timer = WorkTimer(3, self.timer_check_start)
                    _timer.start()
                case "fail":
                    _timer.cancel()
                    logger.ui("失败", "error")
                    break
                case "victory":
                    _timer.cancel()
                    logger.ui("胜利")
                    random_sleep(0.4, 0.8)
                case "finish":
                    _timer.cancel()
                    logger.ui("结束")
                    random_sleep(0.4, 0.8)
                    finish_random_left_right(is_multiple_drops_y=True)
                    random_sleep(0.4, 0.8)
                    while True:
                        if event_thread.is_set():
                            return
                        coor = get_coor_info(f"{RESOURCE_FIGHT_PATH}/finish")
                        # 未重复检测到，表示成功点击
                        if coor.is_zero:
                            self.done()
                            break
                        click()
                        random_sleep(0.4, 0.8)
                case _:
                    if _flag_title_msg:
                        logger.ui("请检查游戏场景", "warn")
                        _flag_title_msg = False
