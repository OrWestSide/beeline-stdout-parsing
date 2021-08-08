from app.infrastructure.BeelineAssignmentArgumentParser import BeelineAssignmentArgumentParser
from app.domain.FileParse import FileParse
from app.application.FileParseUseCase import FileParseUseCase
from app.infrastructure.IORepository import IORepository

if __name__ == '__main__':
    arguments = BeelineAssignmentArgumentParser.parse()
    file_parse: FileParse = FileParse(
        input_file=arguments.input_file,
        query_execution_summary=arguments.query_execution_summary,
        task_execution_summary=arguments.task_execution_summary,
        detailed_metrics=arguments.detailed_metrics
    )
    uc: FileParseUseCase = FileParseUseCase(
        io_repo=IORepository()
    )
    uc.execute(file_parse)
    # qes_file_path = arguments.QueryExecutionSummary

    # with open(file, 'r') as f:
    #     print(f.readlines())
