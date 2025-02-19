from dataclasses import dataclass, field

from mag_tools.model.justify_type import JustifyType
from mag_tools.utils.data.string_format import StringFormat
from mag_tools.utils.data.string_utils import StringUtils

@dataclass
class LogHead:
    BOUNDARY = '----------------------------------------------------------------------'

    version: str = field(init=False, default=2023.1, metadata={'description': '程序版本'})
    bits: str = field(init=False, default=2023.1, metadata={'description': '程序位数'})
    compile_date: str = field(init=False, default='Oct 16 2024', metadata={'description': '编译日期'})
    corp_name: str = field(init=False, default='Ennosoft company of China', metadata={'description': '公司名称'})

    @classmethod
    def from_block(cls, block_lines):
        clazz = cls()

        block_lines = [line.strip() for line in block_lines if len(line.strip()) > 0 and '--' not in line]
        version_nums = StringUtils.pick_numbers(block_lines[0])
        clazz.version = version_nums[0]
        clazz.bits = version_nums[1]

        clazz.compile_date = StringUtils.pick_tail(block_lines[1], 'on').strip()
        clazz.corp_name = StringUtils.pick_tail(block_lines[2], 'by').strip()

        return clazz

    def to_block(self):
        lines = [LogHead.BOUNDARY,
                 StringFormat.pad_value(f'HiSimComp Version {self.version}, {self.bits}bit', len(LogHead.BOUNDARY), JustifyType.CENTER),
                 StringFormat.pad_value(f'Compiled on {self.compile_date}', len(LogHead.BOUNDARY), JustifyType.CENTER),
                 StringFormat.pad_value(f'by {self.corp_name}', len(LogHead.BOUNDARY), JustifyType.CENTER),
                 LogHead.BOUNDARY]

        return lines

if __name__ == '__main__':
    head_str = '''
----------------------------------------------------------------------
                   HiSimComp Version 2023.1, 64bit
                       Compiled on Oct 16 2024
                     by Ennosoft company of China                     
----------------------------------------------------------------------    
    '''
    head_blk = head_str.split('\n')
    head = LogHead.from_block(head_blk)
    print('\n'.join(head.to_block()))