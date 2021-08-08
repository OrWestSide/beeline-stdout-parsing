import re


def query_execution_time_regex():
    return re.compile(r'(.*?)(\d+.*?)$')


def task_execution_time_regex():
    return re.compile(r'(\w+ \d+)')


def detail_summary_metrics():
    return re.compile(r'(.*): (.*)')
