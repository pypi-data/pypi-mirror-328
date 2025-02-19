from dataclasses import dataclass, field
from typing import List, Optional

from mag_tools.utils.data.list_utils import ListUtils

from reservoir_info.bean.simulate.process_stage import ProcessStage

from reservoir_info.bean.simulate.performance_statistics import PerformanceStatistics
from reservoir_info.bean.simulate.log_head import LogHead
from reservoir_info.bean.simulate.pre_processing import PreProcessing

from reservoir_info.bean.simulate.init_ow_model import InitOwModel

@dataclass
class SimulateLog:
    BOUNDARY = '----------------------------------------------------------------------'

    log_head: Optional[LogHead] = field(init=False, default=None, metadata={'description': '日志标题'})
    pre_processing: Optional[PreProcessing] = field(init=False, default=None, metadata={'description': '预处理信息'})
    init_ow_model: Optional[InitOwModel] = field(init=False, default=None, metadata={'description': '初始化油水模型'})
    process_stages: List[ProcessStage] = field(init=False, default_factory=list, metadata={'description': '模拟阶段列表'})
    performance_statistics: Optional[PerformanceStatistics] = field(init=False, default=None, metadata={'description': '性能统计信息'})

    @classmethod
    def from_block(cls, block_lines):
        log = cls()

        block_lines = ListUtils.pick_tail(block_lines, '--')
        head_block = ListUtils.pick_block(block_lines, '--', '--')
        log.log_head = LogHead.from_block(head_block)

        params_block = ListUtils.pick_block(block_lines, 'Console path', '--')

        pre_processing_block = ListUtils.pick_block(block_lines, 'PRE-PROCESSING', '--')
        log.pre_processing = PreProcessing.from_block(pre_processing_block)
        print('\n'.join(log.pre_processing.to_block()))

        init_ow_model_block = ListUtils.pick_block(block_lines, 'INIT OIL-WATER', '--')
        log.init_ow_model = InitOwModel.from_block(init_ow_model_block)
        print('\n'.join(log.init_ow_model.to_block()))

        # 解析模拟步骤数据块
        process_stages_lines = ListUtils.pick_block(block_lines, 'Percent', 'Tecplot stream is closed with returned value')
        process_stages_lines.pop()  # 去掉最后两行
        process_stages_lines.pop()
        process_stages_lines = ListUtils.remove_keyword(process_stages_lines, 'Writing frame')  # 移除‘Writing frame ’信息行

        process_stages_str = '\n'.join(process_stages_lines).replace('\n\n\n', '\n\n').strip()
        process_stages_lines = process_stages_str.split('\n')

        process_stage_blocks = ListUtils.split_by_keyword(process_stages_lines, '')
        for stage_blocks in process_stage_blocks:
            process_stage = ProcessStage.from_block(stage_blocks)
            log.process_stages.append(process_stage)

        performance_statistics_block = ListUtils.pick_tail(block_lines, '-------------------- Performance Statistics --------------------------')
        log.performance_statistics = PerformanceStatistics.from_block(performance_statistics_block)

        return log

    def to_block(self) ->list[str]:
        lines = list()
        lines.extend(self.log_head.to_block())
        lines.append('')
        # 添加参数块，待补充
        lines.extend(self.pre_processing.to_block())
        lines.extend(self.init_ow_model.to_block())

        for process_stage in self.process_stages:
            lines.extend(process_stage.to_block())
            lines.append('')

        lines.extend(self.performance_statistics.to_block())

        return lines


if __name__ == '__main__':
    data_file = 'D:\\HiSimPack\\data\\comp.log'
    with open(data_file, 'r') as f:
        lines_ = [line.strip() for line in f.readlines()]
        log_ = SimulateLog.from_block(lines_)
        print('\n'.join(log_.to_block()))
