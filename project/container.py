from project.helpers.command_selector import CommandSelector
from project.helpers.commands_library import CommandsLibrary
from project.services.index import IndexService

cmd_library = CommandsLibrary()
cmd_selector = CommandSelector(commands_library=cmd_library)
index_service = IndexService(command_selector=cmd_selector)
