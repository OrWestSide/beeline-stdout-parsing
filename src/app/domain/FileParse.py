
class FileParse:
    def __init__(
        self,
        input_file: str = None ,
        query_execution_summary: str = None,
        task_execution_summary: str = None,
        detailed_metrics: str = None
    ):
        self.input_file = input_file
        self.query_execution_summary = query_execution_summary
        self.task_execution_summary = task_execution_summary
        self.detailed_metrics = detailed_metrics
