
from pathlib import Path
import sys
ROOT = [str(x) for x in Path(__file__).resolve().parents if x.joinpath("LiDemand").exists()]
sys.path.extend(ROOT)

from LiDemand.Demand import Demand

# 需求管理器
# 需求管理器需要管理所有的需求，所以需要有一个需求的列表
class DemandManager:
    def __init__(self):
        self._demands = []


    def __getitem__(self, index):
        # 在这里实现权限或范围检查等逻辑
        if index < 0 or index >= len(self._demands):
            raise IndexError("list index out of range")
        return self._data[index]

    def __setitem__(self, index, demand:Demand):
        # 在这里实现修改后的逻辑
        if index < 0 or index >= len(self._data):
            raise IndexError("list index out of range")
        self._data[index] = demand

    def __len__(self):
        return len(self._demands)


    # 添加需求 到需求管理器
    def add_demand(self, demand:Demand):
        self._demands.append(demand)

    def remove_demand(self, demand:Demand):
        self._demands.remove(demand)

    def get_demand_by_index(self, index):
        return self._demands[index]

    def get_demand_by_serial_number(self, serial_number):
        for demand in self._demands:
            if demand._serialNumber == serial_number:
                return demand
        return None

    def get_demand_by_name(self, name):
        for demand in self._demands:
            if demand._name == name:
                return demand
        return None

    def get_demands_by_priority(self, priority):
        return [demand for demand in self._demands if demand._priority == priority]
    




def DamandManagerInit(demand_list:list):
    dm = DemandManager()
    for demand in demand_list:
        dm.add_demand(demand)
    return dm


#def DamandManagerInit(demand_file):
##    dm = DemandManager()
 #   ...
 #   return dm


if __name__ == '__main__':
    demand_list = [Demand('demand_name', 'serial_1', '高', "description"), 
                   Demand('demand_name', 'serial_2', '中', "description"), 
                   Demand('demand_name', 'serial_3', '低', "description")]
    dm = DamandManagerInit(demand_list)
    print(dm.get_demand_by_serial_number('serial_1'))