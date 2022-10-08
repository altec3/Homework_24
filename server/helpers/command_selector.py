from server.helpers.commands_library import CommandsLibrary


class CommandSelector:

    def __init__(self, commands_library: CommandsLibrary):
        self._commands_library = commands_library

    def get_command(self, command: str):
        match command:
            case "filter":
                return self._commands_library.get_filter
            case "map":
                return self._commands_library.get_map
            case "unique":
                return self._commands_library.get_unique
            case "sort":
                return self._commands_library.get_sort
            case "limit":
                return self._commands_library.get_limit
            case "regex":
                return self._commands_library.get_regex
            case _:
                return None
