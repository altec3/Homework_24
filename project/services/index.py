import os
from typing import Dict

from project.helpers.commands import Commands
from project.helpers.utils import load_file, parse_request
from project.setup.app.config import config


class IndexService(Commands):

    def get_result(self, payload: Dict[str, str]) -> list | bool:
        request = parse_request(payload)
        path = os.path.join(config.DATA_DIR, payload["file_name"])
        try:
            file = load_file(path).split("\n")
        except OSError:
            return False

        result = None
        for item in request:
            match item[0]:
                case "filter":
                    result = self.apply_filter(substring=item[1], file=result or file)
                case "map":
                    try:
                        column = int(item[1])
                        result = self.apply_map(column=column, file=result or file)
                    except ValueError:
                        return False
                case "unique":
                    result = self.apply_unique(data=result or file)
                case "sort":
                    result = self.apply_sort(reverse=False if item[1] == "asc" else True, file=result or file)
                case "limit":
                    try:
                        items_count = int(item[1])
                        result = self.apply_limit(items_count=items_count, file=result or file)
                    except ValueError:
                        return False
                case "regex":
                    result = self.apply_regex(pattern=item[1], file=result or file)
                case _:
                    continue

        return result


if __name__ == "__main__":
    pass
