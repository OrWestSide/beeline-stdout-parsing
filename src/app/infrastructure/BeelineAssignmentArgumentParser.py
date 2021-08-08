import argparse


class BeelineAssignmentArgumentParser:
    @staticmethod
    def parse() -> argparse.Namespace:
        parser = argparse.ArgumentParser(description='Beeline Assignment')
        parser.add_argument(
            '-i',
            '--input-file',
            default='beeline_consent_query_stderr.txt',
            help='Input file paths'
        )
        parser.add_argument(
            '-qes',
            '--query-execution-summary',
            default='QueryExecutionSummary.txt',
            help='Query Execution Summary file output path'
        )
        parser.add_argument(
            '-tes',
            '--task-execution-summary',
            default='TaskExecutionSummary.txt',
            help='Task Execution Summary file output path'
        )
        parser.add_argument(
            '-dm',
            '--detailed-metrics',
            default='DetailedMetrics.txt',
            help='Detailed Metrics file output path'
        )

        return parser.parse_args()
