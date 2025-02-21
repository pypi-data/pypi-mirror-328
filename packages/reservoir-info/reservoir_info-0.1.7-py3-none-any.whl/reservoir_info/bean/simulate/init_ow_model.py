import re
from dataclasses import dataclass, field
from typing import List, Optional

from mag_tools.model.justify_type import JustifyType
from mag_tools.utils.data.string_format import StringFormat
from mag_tools.utils.data.string_utils import StringUtils


@dataclass
class InitOwModel:
    simulate_sn: Optional[int] = field(default=None, metadata={"description": "方案模拟序号"})
    building_matrix_costs: Optional[int] = field(init=False, default=None, metadata={'description': '创建矩阵花费时间，单位：毫秒'})
    sat_reg: Optional[int] = field(init=False, default=None, metadata={'description': '饱和区'})
    eql_reg: Optional[int] = field(init=False, default=None, metadata={'description': '平衡区'})

    @classmethod
    def from_block(cls, block_lines):
        clazz = cls()

        block_lines = [line for line in block_lines if line and not any(substr in line for substr in ('--', 'INIT OIL-WATER'))]
        clazz.building_matrix_costs = StringUtils.pick_number(block_lines[0])
        numbers = StringUtils.pick_numbers(block_lines[1])
        clazz.sat_reg = numbers[0] if numbers and len(numbers) > 0 else None
        clazz.eql_reg = numbers[1] if numbers and len(numbers) > 1 else None

        return clazz

    def to_block(self):
        boundary = '----------------------------------------------------------------------'
        lines = [boundary,
                 StringFormat.pad_value('PRE-PROCESSING', len(boundary), JustifyType.CENTER),
                 f' Building matrix costs {self.building_matrix_costs}ms',
                 f' Reservoir status INIT in SAT_REG {self.sat_reg} EQL_REG {self.eql_reg} complete',
                 boundary]

        return lines

if __name__ == '__main__':
    source_str = '''
----------------------------------------------------------------------
                         INIT OIL-WATER MODEL                         

 Building matrix costs 107.576ms
 Reservoir status INIT in SAT_REG 1 EQL_REG 1 complete
----------------------------------------------------------------------
'''
    init_ow_model = InitOwModel.from_block(source_str.split('\n'))

    block_ = init_ow_model.to_block()
    print('\n'.join(block_))
