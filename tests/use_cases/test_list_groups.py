import unittest
import mock

from server.entities.log_group import LogGroup
from server.use_cases import list_groups


class TestListGroupsUseCase(unittest.TestCase):
    def test_execute(self):
        with mock.patch('server.use_cases.list_groups.list_groups') as mock_repository:
            mock_repository.return_value = {'logGroups': [{'logGroupName': 'group-a'}]}

            groups = list_groups.execute()

            self.assertEqual(groups, [LogGroup('group-a')])
