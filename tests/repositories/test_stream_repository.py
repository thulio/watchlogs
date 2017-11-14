import unittest
import mock

from server.repositories.stream_repository import list_streams


class TestStreamRepository(unittest.TestCase):
    def test_list_groups(self):
        with mock.patch('server.repositories.stream_repository.cloudwatch') as mock_service:
            mock_service.list_streams.return_value = ['stream-a', 'stream-b']

            streams = list_streams('some-group')

            self.assertEqual(streams, ['stream-a', 'stream-b'])
            self.assertEqual(mock_service.list_streams.call_count, 1)
            self.assertEqual(mock_service.list_streams.call_args_list, [mock.call('some-group')])
