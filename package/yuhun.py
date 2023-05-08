#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# yuhun.py
"""御魂副本"""

import pyautogui

from utils.coordinate import Coor
from utils.decorator import *
from utils.function import (check_scene_multiple_once, click, function,
                            get_coor_info)
from utils.log import log
from utils.window import window


class YuHun:
    """御魂副本"""

    @log_function_call
    def __init__(self):
        """御魂副本"""
        self.scene_name: str = "御魂副本"
        self.n: int = 0  # 当前次数
        self.max: int = 0  # 总次数
        self.fast_time: int = 13 - 2  # 最快通关速度，用于中途等待
        self.resource_path: str = "yuhun"  # 路径
        self.resource_list: list = [  # 资源列表
            "title_10",  # 魂十
            "title_11",  # 魂土
            "title_12",  # 神罚
            "xiezhanduiwu",  # 组队界面
            "passenger_2",  # 队员2
            "passenger_3",  # 队员3
            "start_team",  # 组队挑战
            "start_single",  # 单人挑战
            "fighting",  # 魂土进行中
            "fighting_linshuanghanxue",  # 凛霜寒雪战斗主题
            "fighting_shenfa",  # 神罚战斗场景
            "finish_damage",  # 结束特征图像
            "finish_damage_2000",  # 结束特征图像-鎏金圣域
            "finish_damage_shenfa",  # 结束特征图像-神罚
            "accept_invitation",  # 接受邀请
        ]

    @log_function_call
    def start(self, mode: str = None) -> None:
        """挑战"""
        if mode == "team":
            function.judge_click(f"{self.resource_path}/start_team")
        if mode == "single":
            function.judge_click(f"{self.resource_path}/start_single")

    @log_function_call
    def result(self) -> bool:
        """结果判断

        返回:
            bool: 结算结果
        """
        while True:
            coor = get_coor_info("victory_gu")  # TODO change "victory_gu" to "victory"
            if coor.is_effective:
                log.ui("胜利")
                return True
            coor = get_coor_info("fail")
            if coor.is_effective:
                log.ui("失败")
                return False


class YuHunTeam(YuHun):
    """组队御魂副本"""

    @log_function_call
    def __init__(self,
                 n: int = 0,
                 flag_driver: bool = False,
                 flag_passengers: int = 2,
                 flag_drop_statistics: bool = False):
        super().__init__()
        """组队御魂副本

        参数:
            n (int): 次数，默认0次
            flag_driver (bool): 是否司机，默认否
            flag_passengers (int): 组队人数，默认2人
            flag_drop_statistics (bool): 是否开启掉落统计，默认否
        """
        self.scene_name: str = "组队御魂副本"
        self.n: int = 0  # 当前次数
        self.max: int = n  # 总次数
        self.resource_list: list = [  # 资源列表
            "xiezhanduiwu",  # 组队界面
            "passenger_2",  # 队员2
            "passenger_3",  # 队员3
            "start_team",  # 组队挑战
            "fighting",  # 魂土进行中
            "fighting_linshuanghanxue",  # 凛霜寒雪战斗主题
            "fighting_shenfa",  # 神罚战斗场景
            "finish_damage",  # 结束特征图像
            "finish_damage_2000",  # 结束特征图像-鎏金圣域
            "finish_damage_shenfa",  # 结束特征图像-神罚
            "accept_invitation",  # 接受邀请
        ]

        self.flag_driver: bool = flag_driver  # 是否为司机（默认否）
        self.flag_passengers: int = flag_passengers  # 组队人数
        self.flag_drop_statistics: bool = flag_drop_statistics  # 是否开启掉落统计

    @log_function_call
    def is_passengers_on_position(self):
        """司机"""
        log.ui("等待队员")
        # 是否3人组队
        if self.flag_passengers == 3:
            while True:
                coor = get_coor_info(f"{self.resource_path}/passenger_3")
                if coor.is_zero:
                    log.ui("队员3就位")
                    return
        else:
            while True:
                coor = get_coor_info(f"{self.resource_path}/passenger_2")
                if coor.is_zero:
                    log.ui("队员2就位")
                    return

    @log_function_call
    def finish(self):
        """结束

        掉落物大体分为2种情况：
        1.正常情况，达摩蛋能被识别
        2.掉落过多情况（指神罚一排紫蛇皮），达摩蛋被遮挡，此时贪吃鬼必定（可能）出现
        """
        self.result()
        function.random_sleep(0.4, 0.8)
        # 结算
        x, y = function.random_finish_left_right(False, is_multiple_drops_x=True)
        coor = Coor(x, y)
        _flag_screenshot = True
        pyautogui.moveTo(coor.x + window.window_left, coor.y + window.window_top, duration=0.25)
        pyautogui.doubleClick()
        while True:
            # 检测到任一图像
            scene, coor = check_scene_multiple_once(["finish", f"{self.resource_path}/finish_2000", "tanchigui"])
            if coor.is_effective:
                if _flag_screenshot and self.flag_drop_statistics:
                    function.screenshot("cache_yuhun")
                    _flag_screenshot = False
                click()
                function.random_sleep(0.6, 1)
            # 所有图像都未检测到，退出循环
            elif coor.is_zero:
                log.ui("结束")
                return

    @run_in_thread
    @time_count
    @log_function_call
    def run(self):
        # 保留必需图像，提高识别效率
        _g_resource_list: list = [
            "xiezhanduiwu",  # 组队界面
            # "start_team",  # 组队挑战
            "fighting",  # 魂土进行中
            "fighting_linshuanghanxue",  # 凛霜寒雪战斗主题
            "fighting_shenfa",  # 神罚战斗场景
            "accept_invitation"  # 接受邀请
        ]
        if self.flag_driver:
            _g_resource_list.append("start_team")
        _resource_list: list = None
        _flag_title_msg: bool = True

        log.num(f"0/{self.max}")
        while self.n < self.max:
            _resource_list = _g_resource_list if _resource_list == None else _resource_list
            scene, coor = check_scene_multiple_once(_resource_list, self.resource_path)
            if scene:
                log.info(f"当前场景: {scene}")
            match scene:
                case "xiezhanduiwu":
                    log.ui('组队界面准备中')
                    if self.flag_driver:
                        self.is_passengers_on_position()
                        self.start("team")
                    # 只判断下列图像，提高效率
                    _resource_list = ["fighting", "fighting_linshuanghanxue", "fighting_shenfa"]
                    _flag_title_msg = False
                case "fighting" | "fighting_linshuanghanxue" | "fighting_shenfa":
                    log.ui("对局进行中")
                    self.finish()
                    self.n += 1
                    log.num(f"{self.n}/{self.max}")
                    _resource_list = None
                    _flag_title_msg = False
                case "accept_invitation":
                    # TODO 新设备第一次接受邀请会有弹窗，需手动勾选“不再提醒”
                    log.ui("接受邀请")
                    click(coor)
                case _:
                    if _flag_title_msg:
                        log.warn("请检查游戏场景")
                        _flag_title_msg = False


class YuHunSingle(YuHun):
    """单人御魂副本"""

    @log_function_call
    def __init__(self, n: int = 0, flag_drop_statistics: bool = False):
        super().__init__()
        """单人御魂副本

        参数:
            n (int): 次数，默认0次
            flag_drop_statistics (bool): 是否开启掉落统计，默认否
        """
        self.scene_name: str = "御魂副本"
        self.n: int = 0  # 当前次数
        self.max: int = n  # 总次数
        self.resource_list: list = [  # 资源列表
            "title_10",  # 魂十
            "title_11",  # 魂土
            "title_12",  # 神罚
            "start_single",  # 单人挑战
            "fighting",  # 魂土进行中
            "fighting_linshuanghanxue",  # 凛霜寒雪战斗主题
            "fighting_shenfa",  # 神罚战斗场景
            # "finish_damage",  # 结束特征图像
            # "finish_damage_2000",  # 结束特征图像-鎏金圣域
            # "finish_damage_shenfa",  # 结束特征图像-神罚
        ]
        self.flag_drop_statistics: bool = flag_drop_statistics  # 是否开启掉落统计

    @log_function_call
    def finish_fast(self):  # FIXME
        """结束"""
        self.result()
        function.random_sleep(0.4, 0.8)
        # 结算
        x, y = function.random_finish_left_right(False, is_multiple_drops_x=True)
        coor = Coor(x, y)
        _flag_screenshot = True
        pyautogui.moveTo(coor.x + window.window_left, coor.y + window.window_top, duration=0.25)
        pyautogui.doubleClick()
        while True:
            # 检测到任一图像
            scene, coor = check_scene_multiple_once(["finish", f"{self.resource_path}/finish_2000", "tanchigui"])
            if coor.is_effective:
                if _flag_screenshot and self.flag_drop_statistics:
                    function.screenshot("cache_yuhun")
                    _flag_screenshot = False
                click()
                function.random_sleep(0.6, 1)
            # 所有图像都未检测到，退出循环
            elif coor.is_zero:
                log.ui("结束")
                return

    def finish_slow(self):
        """
        结束 等待自动掉落
        """
        self.result()
        function.random_sleep(0.4, 0.8)
        # 结算
        x, y = function.random_finish_left_right(False, is_multiple_drops_x=True)
        coor = Coor(x, y)
        _flag_screenshot = True
        pyautogui.moveTo(coor.x + window.window_left, coor.y + window.window_top, duration=0.25)
        # pyautogui.doubleClick()
        while True:
            # 检测到任一图像
            scene, coor = check_scene_multiple_once(["finish", f"{self.resource_path}/finish_2000", "tanchigui"])
            if coor.is_effective:
                if _flag_screenshot and self.flag_drop_statistics:
                    function.screenshot("cache_yuhun")
                    _flag_screenshot = False
                click()
                function.random_sleep(0.6, 1)
            # 所有图像都未检测到，退出循环
            elif coor.is_zero:
                log.ui("结束")
                return

    @run_in_thread
    @time_count
    @log_function_call
    def run(self):
        """单人"""
        _g_resource_list: list = [
            "title_10",  # 魂十
            "title_11",  # 魂土
            "title_12",  # 神罚
            "start_single",  # 单人挑战
            "fighting",  # 魂土进行中
            "fighting_linshuanghanxue",  # 凛霜寒雪战斗主题
            "fighting_shenfa"  # 神罚战斗场景
        ]
        _resource_list: list = None
        _flag_title_msg: bool = True

        log.num(f"0/{self.max}")
        while self.n < self.max:
            _resource_list = _g_resource_list if _resource_list == None else _resource_list
            scene, (x, y) = function.check_scene_multiple_once(_resource_list, self.resource_path)
            if scene:
                log.ui(f"scene: {scene}")
            match scene:
                case "title_10" | "title_11" | "title_12":
                    self.start("single")
                    function.random_sleep(self.fast_time, self.fast_time+1)
                    _flag_title_msg = False
                case "start_single":
                    function.click(x, y)
                    function.random_sleep(self.fast_time, self.fast_time+1)
                    # 只判断下列图像，提高效率
                    _resource_list = ["fighting", "fighting_linshuanghanxue", "fighting_shenfa"]
                    _flag_title_msg = False
                case "fighting" | "fighting_linshuanghanxue" | "fighting_shenfa":
                    log.ui("对局进行中")
                    self.finish_slow()
                    self.n += 1
                    log.num(f"{self.n}/{self.max}")
                    _resource_list = None
                    _flag_title_msg = False
                case _:
                    if _flag_title_msg:
                        log.warn("请检查游戏场景")
                        _flag_title_msg = False
