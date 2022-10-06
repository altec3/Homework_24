from typing import Optional


class Commands:

    @staticmethod
    def apply_filter(substring: str, file: Optional[list]):
        return filter(lambda item: item.count(substring), file)

    @staticmethod
    def apply_map(column, file: Optional[list]):
        return map(lambda item: item.split(" ")[column], file)

    @staticmethod
    def apply_unique(data: Optional[list]):
        return set(data)

    @staticmethod
    def apply_sort(file: Optional[list], reverse: bool = False):
        return sorted(file, reverse=reverse)

    @staticmethod
    def apply_limit(items_count: int, file: Optional[list]):
        return [file[item] for item in range(items_count)]
