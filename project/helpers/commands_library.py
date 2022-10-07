import re
from typing import List, Union, Optional


class CommandsLibrary:

    @staticmethod
    def get_filter(param: str, data: List[str]) -> List[str]:
        return list(filter(lambda item: item.count(param), data))

    @staticmethod
    def get_map(param: Union[int, str], data: List[str]) -> Optional[List[str]]:
        if not isinstance(param, int):
            try:
                param = int(param)
            except ValueError:
                return None
        return list(map(lambda item: item.split(" ")[param], data))

    @staticmethod
    def get_unique(data: List[str], *args) -> List[str]:
        unique = set(data)
        return list(unique)

    @staticmethod
    def get_sort(data: List[str], param: str) -> List[str]:
        reverse = False if param == "asc" else True
        return sorted(data, reverse=reverse)

    @staticmethod
    def get_limit(param: Union[int, str], data: List[str]) -> Optional[List[str]]:
        if not isinstance(param, int):
            try:
                param = int(param)
            except ValueError:
                return None
        return [data[item] for item in range(param)]

    @staticmethod
    def get_regex(param: str, data: List[str]) -> List[str]:
        return [item for item in data if re.search(pattern=param, string=item)]
