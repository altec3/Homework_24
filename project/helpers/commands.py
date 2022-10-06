import re
from typing import Union, List, Set


class Commands:

    @staticmethod
    def apply_filter(substring: str, file: list) -> List[str]:
        return list(filter(lambda item: item.count(substring), file))

    @staticmethod
    def apply_map(column, file: list) -> List[str]:
        return list(map(lambda item: item.split(" ")[column], file))

    @staticmethod
    def apply_unique(data: List[str]) -> List[str]:
        unique = set(data)
        return list(unique)

    @staticmethod
    def apply_sort(file: list, reverse: bool = False) -> List[str]:
        return sorted(file, reverse=reverse)

    @staticmethod
    def apply_limit(items_count: int, file: list) -> List[str]:
        return [file[item] for item in range(items_count)]

    @staticmethod
    def apply_regex(pattern: str, file: list) -> List[str]:
        return [item for item in file if re.search(pattern=pattern, string=item)]
