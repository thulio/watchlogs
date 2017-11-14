from server.entities.log_group import LogGroup
from server.repositories.group_repository import list_groups


def execute():
    log_groups = list_groups()
    return [LogGroup.from_dict(group) for group in log_groups['logGroups']]
