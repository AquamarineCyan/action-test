from src.utils.log import log


class Package:

    scene_name: str = None
    resource_path: str = None
    resource_list: list = []

    def __init__(self, n: int = 0) -> None:
        self.n: int = 0
        self.max: int = n

    def scene_print(self, scene: str = None) -> None:
        """当前场景"""
        if "/" in scene:
            scene = scene.split("/")[-1]
        log.info(f"当前场景: {scene}")

    def done(self) -> None:
        """更新一次完成情况"""
        self.n += 1
        log.num(f"{self.n}/{self.max}")
