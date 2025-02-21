from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.common.base_data import BaseData

from reservoir_info.model.simulate_type import SimulateType


@dataclass
class RealtimeLog(BaseData):
    user_sn: Optional[int] = field(default=None, metadata={"description": "用户序号"})
    simulate_type: SimulateType = field(default=None, metadata={"description": "模拟方式"})
    simulate_id: Optional[str] = field(default=None, metadata={"description": "模拟标识"})
    case_file: Optional[int] = field(default=None, metadata={"description": "用户序号"})
    message: Optional[str] = field(default=None, metadata={"description": "日志消息"})
