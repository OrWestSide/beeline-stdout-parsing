from pprint import pprint
from typing import List


class IORepository:
    @staticmethod
    def read(path: str) -> List[str]:
        with open(path, 'r') as f:
            data = f.readlines()
        return data

    @staticmethod
    def write_dict(data: dict, path: str):
        with open(path, 'w') as f:
            pprint(data, stream=f)
