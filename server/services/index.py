import os
from typing import Dict, List, Optional

from server.helpers.command_selector import CommandSelector
from server.helpers.utils import load_file, parse_request
from server.setup.app.config import config


class IndexService:

    def __init__(self, command_selector: CommandSelector):
        self._command_selector = command_selector

    def get_result(self, payload: Dict[str, str]) -> Optional[List[str]]:

        request: List[tuple] = parse_request(payload)
        path: str = os.path.join(config.DATA_DIR, payload["file_name"])

        try:
            file: List[str] = load_file(path).split("\n")
        except OSError:
            return None

        result = None
        for item in request:
            command = self._command_selector.get_command(item[0])
            result = command(param=item[1], data=result or file)

        return result


if __name__ == "__main__":
    pass
