from dataclasses import dataclass
from typing import Dict, List

from coma import command
import coma


@command("test1")
class Test:
    def __init__(self):
        pass

    def run(self):
        print("test1, self is", self)


@command("test2")
def test():
    print("test2")


@command("test3")
def test(extras3_dict: dict, extras3_list: list):
    print("test3")


@command("test4")
def test(extras4_dict: Dict, extras4_list: List[str]):
    print("test4")


@command("test5")
def test(bad: str):
    print("Failed test5")


@dataclass
class Config:
    x: int = 1


@command("test6")
class Test6:
    def __init__(self, test6_cfg: Config, test6_extras: Dict):
        self.cfg = test6_cfg
        self.extras = test6_extras

    def run(self):
        print(self.cfg)
        print(self.extras)


if __name__ == "__main__":
    coma.register("test7", lambda x: print("Failed test7"), test7_bad=int)

    try:
        coma.wake()
    except ValueError:
        import sys

        want_to_fail = ["test5", "test7"]
        if any(test_name in sys.argv for test_name in want_to_fail):
            for test_name in want_to_fail:
                if test_name in sys.argv:
                    print(test_name)
        else:
            raise
