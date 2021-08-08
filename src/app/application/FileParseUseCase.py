import re
from typing import List

from app.domain.FileParse import FileParse
from app.infrastructure.FileParseUtils import query_execution_time_regex, \
    task_execution_time_regex, detail_summary_metrics
from app.infrastructure.IORepository import IORepository
from app.constants import QUERY_EXECUTION_SUMMARY, INFO_PREFIX, \
    TASK_EXECUTION_SUMMARY, COMPLETED_COMMAND_EXECUTED


class FileParseUseCase:
    def __init__(self, io_repo: IORepository):
        self.io_repo = io_repo
        self.query_execution_time_regex = query_execution_time_regex()
        self.task_execution_time_regex = task_execution_time_regex()
        self.detail_summary_metrics = detail_summary_metrics()

    def _read_data(self, _path: str) -> List[str]:
        return self.io_repo.read(_path)

    def _save_file(self, _data: dict, _path: str) -> None:
        self.io_repo.write_dict(_data, _path)

    def _parse_file(self, data: List[str], operation) -> None:
        self._parse_query_execution_summary(
            data, operation.query_execution_summary
        )
        self._parse_task_execution_summary(
            data, operation.task_execution_summary
        )
        self._parse_detail_metrics(
            data, operation.detailed_metrics
        )

    def _parse_query_execution_summary(
            self, data: List[str], _path: str
    ) -> None:
        query_execution_summary = {}
        for i in range(len(data)):
            if QUERY_EXECUTION_SUMMARY in data[i]:
                i += 4
                while '-' not in data[i]:
                    metric = self.query_execution_time_regex.findall(
                        data[i].lstrip(INFO_PREFIX).strip()
                    )
                    query_execution_summary[
                        metric[0][0].strip()
                    ] = metric[0][1].strip()
                    i += 1
                break
        self._save_file(query_execution_summary, _path)

    def _parse_task_execution_summary(
            self, data: List[str], _path: str
    ) -> None:
        task_execution_summary = {}
        for i in range(len(data)):
            if TASK_EXECUTION_SUMMARY in data[i]:
                i += 4
                while '-' not in data[i]:
                    key_metric = self.task_execution_time_regex.findall(
                        data[i].lstrip(INFO_PREFIX).strip()
                    )[0]

                    dur, cpu, gc, input_rec, output_rec = re.sub(
                        ' +',
                        '\t',
                        data[i].lstrip(INFO_PREFIX).strip().lstrip(
                            key_metric
                        ).strip()
                    ).split('\t')

                    task_execution_summary[key_metric] = {
                        "DURATION(ms)": dur.replace('.', ''),
                        "CPU_TIME(ms)": cpu.replace(',', ''),
                        "GC_TIME(ms)": gc.replace(',', ''),
                        "INPUT_RECORDS": input_rec.replace(',', ''),
                        "OUTPUT_RECORDS": output_rec.replace(',', '')
                    }
                    i += 1
                break
        self._save_file(task_execution_summary, _path)

    def _parse_detail_metrics(
            self, data: List[str], _path: str
    ) -> None:
        detail_metrics = {}
        for i in range(len(data)):
            if TASK_EXECUTION_SUMMARY in data[i]:
                i += 4
                while '-' not in data[i]:
                    i += 1
                i += 2

                _tmp = {}
                _key = None
                while COMPLETED_COMMAND_EXECUTED not in data[i]:
                    metric = self.detail_summary_metrics.findall(
                        data[i].lstrip(INFO_PREFIX)
                    )
                    if len(metric) == 0:
                        if not _key:
                            _key = data[i].lstrip(INFO_PREFIX).strip()[:-1]
                        detail_metrics[_key] = _tmp.copy()
                        _tmp.clear()

                        _key = data[i].lstrip(INFO_PREFIX).strip()[:-1]
                    else:
                        _tmp[metric[0][0]] = metric[0][1]
                    i += 1
                break
        self._save_file(detail_metrics, _path)

    def execute(self, operation: FileParse) -> None:
        file_data = self._read_data(operation.input_file)
        self._parse_file(file_data, operation)
