from dataclasses import dataclass, field
from typing import Optional

from mag_tools.bean.common.base_data import BaseData


@dataclass
class RealTimeLog(BaseData):
    user_sn: Optional[int] = field(default=None, metadata={"description": "用户序号"})
    user_sn: Optional[int] = field(default=None, metadata={"description": "用户序号"})
