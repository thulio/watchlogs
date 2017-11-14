import unittest
import mock

from server.repositories.group_repository import list_groups


class TestGroupRepository(unittest.TestCase):
    def test_list_groups(self):
        with mock.patch('server.repositories.group_repository.cloudwatch') as mock_service:
            mock_service.list_groups.return_value = ['group-a', 'group-b']

            groups = list_groups()

            self.assertEqual(groups, ['group-a', 'group-b'])
            self.assertEqual(mock_service.list_groups.call_count, 1)
            self.assertEqual(mock_service.list_groups.call_args_list, [mock.call()])
