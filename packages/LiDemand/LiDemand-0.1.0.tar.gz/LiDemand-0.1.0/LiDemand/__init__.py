


from pathlib import Path
import sys
ROOT = [str(x) for x in Path(__file__).resolve().parents if x.joinpath("LiDemand").exists()]
sys.path.extend(ROOT)

from LiDemand.Demand import Demand
from LiDemand.DemandManage import DemandManager

__all__ = ["Demand", "DemandManager"]