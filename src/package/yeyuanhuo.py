from ..utils.decorator import log_function_call
from ..utils.event import event_thread
from ..utils.function import (
    RESOURCE_FIGHT_PATH,
    check_click,
    check_scene_multiple_once,
    click,
    finish_random_left_right,
    random_sleep
)
from ..utils.log import logger
from .utils import Package


class YeYuanHuo(Package):
    """业原火副本"""
    scene_name = "业原火副本"
    resource_path = "yeyuanhuo"
    resource_list = [
        "title",  # 标题
        "start",  # 挑战
    ]
    description = "默认为“痴”，可在/data/myresource/yeyuanhuo路径下添加自定义素材"
    fast_time = 13

    @log_function_call
    def __init__(self, n: int = 0) -> None:
        super().__init__(n)

    @log_function_call
    def start(self):
        """挑战开始"""
        check_click(f"{self.resource_path}/start")

    def run(self):
        self.current_resource_list = [
            f"{self.resource_path}/title",
            f"{self.resource_path}/start",
            f"{RESOURCE_FIGHT_PATH}/finish",
            f"{RESOURCE_FIGHT_PATH}/fail",
            f"{RESOURCE_FIGHT_PATH}/victory",
            f"{RESOURCE_FIGHT_PATH}/soul_overflow",
        ]
        _flag_title_msg: bool = True
        logger.num(f"0/{self.max}")
        self.log_current_scene_list()

        while self.n < self.max:
            if event_thread.is_set():
                return
            scene, coor = check_scene_multiple_once(self.current_resource_list)
            if scene is None:
                continue
            scene = self.scene_handle(scene)

            match scene:
                case "title":
                    logger.scene(self.scene_name)
                    _flag_title_msg = False
                    self.start()
                    random_sleep(self.fast_time)
                case "start":
                    click(coor)
                    random_sleep(self.fast_time)
                case "fail":
                    logger.ui("失败，需要手动处理", "warn")
                    break
                case "victory":
                    logger.ui("胜利")
                    random_sleep()
                case "finish":
                    logger.ui("结束")
                    if check_click(f"{RESOURCE_FIGHT_PATH}/soul_overflow", timeout=2):
                        logger.ui("御魂上限", "warn")
                    finish_random_left_right()
                    self.done()
                    random_sleep(2)
                case "soul_overflow":
                    # 正常情况下会在结束界面点击，这是备用方案
                    logger.ui("御魂上限", "warn")
                    click(coor)
                case _:
                    if _flag_title_msg:
                        logger.ui("请检查游戏场景", "warn")
                        _flag_title_msg = False
