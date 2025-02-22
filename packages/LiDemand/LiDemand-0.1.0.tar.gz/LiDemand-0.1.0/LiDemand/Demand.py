

from pathlib import Path
import sys
ROOT = [str(x) for x in Path(__file__).resolve().parents if x.joinpath("LiDemand").exists()]
sys.path.extend(ROOT)


# 需求的基类
# 需求的属性：名称、编号、优先级、描述
class BaseDemand:
    def __init__(self, name, serial_number, priority, description ):
        self._name = name
        self._serialNumber = serial_number
        self._priority = priority
        self._description = description
        

#  需求需要可以映射到测试的用例，所以需要有一个用例的列表
#  需求的属性：名称、编号、优先级、描述、用例列表
# 
class Demand(BaseDemand):
    def __init__(self, name, serial_number, priority, description ):
        super().__init__(name, serial_number, priority, description )
        self._casesArray = []
    def addCase(self, case):
        self._casesArray.append(case)

    def addCases(self, cases):
        for case in cases:
            self.addCase(case)

    def removeCase(self, case):
        self._casesArray.remove(case)

    def getCases(self):
        return self._casesArray
    
    def __str__(self):
        return f"需求名称：{self._name}\n需求编号：{self._serialNumber}\n需求优先级：{self._priority}\n需求描述：{self._description}\n需求绑定的用例列表：{self._casesArray}"