from server.helpers.command_selector import CommandSelector
from server.helpers.commands_library import CommandsLibrary
from server.services.index import IndexService

cmd_library = CommandsLibrary()
cmd_selector = CommandSelector(commands_library=cmd_library)
index_service = IndexService(command_selector=cmd_selector)
