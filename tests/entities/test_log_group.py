import unittest

from server.entities.log_group import LogGroup


class TestLogGroup(unittest.TestCase):
    def test_from_dict(self):
        group_dict = {'logGroupName': 'log-group'}

        log_group = LogGroup.from_dict(group_dict)

        self.assertEqual(log_group.name, 'log-group')

    def test_eq(self):
        group_1 = LogGroup('name')
        group_2 = LogGroup('name')

        self.assertEqual(group_1, group_2)