from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from mag_tools.model.process_status import ProcessStatus
from mag_tools.utils.data.list_utils import ListUtils
from mag_tools.utils.data.string_utils import StringUtils


@dataclass
class Performed:
    steps: Optional[int] = field(default=0, metadata={"description": "步骤"})
    rollback_steps: Optional[int] = field(default=0, metadata={"description": "回滚步骤"})
    nri_failure: Optional[int] = field(default=0, metadata={"description": "NRI失败步骤"})
    newton_steps: Optional[int] = field(default=0, metadata={"description": "牛顿步骤"})
    liner_cycles: Optional[int] = field(default=0, metadata={"description": "线性循环"})
    amg_cycles: Optional[int] = field(default=0, metadata={"description": "AMG循环"})
    min_dt: Optional[float] = field(default=0, metadata={"description": "最小DT"})
    max_dt: Optional[float] = field(default=0, metadata={"description": "最大DT"})

    @classmethod
    def from_block(cls, block_lines):
        performed = cls()

        block_lines = ListUtils.remove_keyword(block_lines, "Performance Statistics")
        performed_values = StringUtils.pick_numbers(block_lines[0])
        performed.steps = performed_values[0]
        performed.rollback_steps = performed_values[1]
        performed.nri_failure = performed_values[2]

        performed_newton_steps = StringUtils.pick_numbers(block_lines[1])
        performed.newton_steps = performed_newton_steps[0]

        performed_liner_cycles = StringUtils.pick_numbers(block_lines[2])
        performed.liner_cycles = performed_liner_cycles[0]

        performed_amg_cycles = StringUtils.pick_numbers(block_lines[3])
        performed.amg_cycles = performed_amg_cycles[0]

        min_max_dt = StringUtils.pick_numbers(block_lines[4])
        performed.min_dt = min_max_dt[0]
        performed.max_dt = min_max_dt[1]

        return performed

    def to_block(self):
        lines = list()
        lines.append(f'Performed:  {self.steps} time steps, {self.rollback_steps} rollbacks ({self.nri_failure} NRIFailure)')
        lines.append(f'            {self.newton_steps} Newton steps')
        lines.append(f'            {self.liner_cycles} Liner cycles')
        lines.append(f'            {self.amg_cycles} AMG cycles')
        lines.append(f'Min/Max DT: {self.min_dt}/{self.max_dt} DAY')
        return lines


@dataclass
class PerformanceStatistics:
    performed: Optional[Performed] = field(default=0, metadata={"description": "性能参数"})
    total_time: Optional[float] = field(default=0, metadata={"description": "总模拟时间"})
    property_calc: Optional[float] = field(default=0, metadata={"description": "属性计算时间"})
    flow_terms: Optional[float] = field(default=0, metadata={"description": "流量项计算时间"})
    well_thread: Optional[float] = field(default=0, metadata={"description": "井螺纹计算时间"})
    complete_matrix: Optional[float] = field(default=0, metadata={"description": "完整矩阵计算时间"})
    newton_method: Optional[float] = field(default=0, metadata={"description": "牛顿法计算时间"})
    file_writing: Optional[float] = field(default=0, metadata={"description": "文件写入时间"})
    solver_time: Optional[float] = field(default=0, metadata={"description": "求解时间"})
    pressure_factor: Optional[float] = field(default=0, metadata={"description": "压力因子时间"})
    pressure_solve: Optional[float] = field(default=0, metadata={"description": "压力求解时间"})
    pressure_decouple: Optional[float] = field(default=0, metadata={"description": "压力解耦时间"})
    ilu_factor: Optional[float] = field(default=0, metadata={"description": "ILU因子时间"})
    ilu_solve: Optional[float] = field(default=0, metadata={"description": "ILU求解时间"})
    mv: Optional[float] = field(default=0, metadata={"description": "MV时间"})
    case_file: Optional[str] = field(default=None, metadata={"description": "模型方案文件"})
    parameters: Optional[str] = field(default=None, metadata={"description": "方案参数（json字符串）"})
    status: Optional[ProcessStatus] = field(default=None, metadata={"description": "模拟状态：正在处理、成功或失败"})
    error_message: Optional[str] = field(default=None, metadata={"description": "错误信息"})
    sn: Optional[int] = field(default=None, metadata={"description": "方案模拟序号"})

    @classmethod
    def from_block(cls, block_lines):
        ps = cls()
        block_lines = ListUtils.trim(block_lines)
        performed_block = ListUtils.pick_head(block_lines, '')
        ps.performed = Performed.from_block(performed_block)

        statistics_block = ListUtils.pick_block(block_lines, '', '')
        statistics_block = ListUtils.trim(statistics_block)
        statistics_map = {line.split(':')[0].strip(): line.split(':')[1].strip() for line in statistics_block}
        statistics_map = {k.strip(): StringUtils.pick_number(v) for k,v in statistics_map.items()}

        ps.total_time = statistics_map['Total time']
        ps.property_calc = statistics_map['Property calc']
        ps.flow_terms = statistics_map['Flow terms']
        ps.well_thread = statistics_map['--Well thread']
        ps.complete_matrix = statistics_map['Complete matrix']
        ps.newton_method = statistics_map['Newton method']
        ps.file_writing = statistics_map['File writing']
        ps.solver_time = statistics_map['Solver time']
        ps.pressure_factor = statistics_map['--Factor']
        ps.pressure_solve = statistics_map['--Solve']
        ps.pressure_decouple = statistics_map['--Decouple']
        ps.ilu_factor = statistics_map['--Factor']
        ps.ilu_solve = statistics_map['--Solve']
        ps.mv = statistics_map['--MV']

        case_block = ListUtils.pick_tail(block_lines, '-- Simulation of case')
        ps.case_file = case_block[0].split("'")[1]

        return ps

    def to_block(self):
        lines = list()
        lines.append('-------------------- Performance Statistics ---------------------------')
        lines.extend(self.performed.to_block())
        lines.append('')
        lines.append(f'Total time:           {self.total_time} s')
        lines.append(f'Property calc:        {self.property_calc} s')
        lines.append(f'Flow terms:           {self.flow_terms} s')
        lines.append(f'  --Well thread:      {self.well_thread} s')
        lines.append(f'Complete matrix:      {self.complete_matrix} s')
        lines.append(f'Newton method:        {self.newton_method} s')
        lines.append(f'File writing:         {self.file_writing} s')
        lines.append(f'Solver time:          {self.solver_time} s')
        lines.append('  --Pressure')
        lines.append(f'    --Factor:         {self.pressure_factor} s')
        lines.append(f'    --Solve:          {self.pressure_solve} s')
        lines.append(f'    --Decouple:       {self.pressure_decouple} s')
        lines.append('  --ILU')
        lines.append(f'    --Factor:         {self.ilu_factor} s')
        lines.append(f'    --solve:          {self.ilu_solve} s')
        lines.append(f'  --MV:               {self.mv} s ')
        lines.append('')
        lines.append(f"-- Simulation of case '{self.case_file}' complete --")

        return lines

if __name__ == '__main__':
    per_str = r'''
-------------------- Performance Statistics ---------------------------
Performed:  129 time steps, 0 rollbacks (0 NRIFailure)
            542 Newton steps
            4257 linear cycles
            4257 AMG cycles
Min/Max DT: 0.01/50 DAY

Total time:            1221.4 s
Property calc:        110.864 s
Flow terms:           155.656 s
  --Well thread:     0.301548 s
Complete matrix:      20.7418 s
Newton method:        4.39879 s
File writing:         21.7548 s
Solver time:          901.529 s
  --Pressure:
    --Factor:         288.429 s
    --Solve:          216.593 s
    --Decouple:       105.617 s
  --ILU:
    --Factor:         76.6676 s
    --Solve:          126.038 s
  --MV:               76.8614 s

-- Simulation of case 'D:\HiSimPack\data\Comp\spe10\spe10' complete --    
'''
    ps_ = PerformanceStatistics.from_block(per_str.split('\n'))
    print('\n'.join(ps_.to_block()))