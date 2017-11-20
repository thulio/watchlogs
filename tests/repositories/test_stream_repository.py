import unittest
import mock

from server.repositories.stream_repository import list_streams, fetch_stream_messages


class TestStreamRepository(unittest.TestCase):
    def test_list_groups(self):
        with mock.patch('server.repositories.stream_repository.cloudwatch') as mock_service:
            mock_service.list_streams.return_value = ['stream-a', 'stream-b']

            streams = list_streams('some-group')

            self.assertEqual(streams, ['stream-a', 'stream-b'])
            self.assertEqual(mock_service.list_streams.call_count, 1)
            self.assertEqual(mock_service.list_streams.call_args_list, [mock.call('some-group', None)])

    def test_fetch_stream_from_beggining(self):
        with mock.patch('server.repositories.stream_repository.cloudwatch') as mock_service:
            mock_service.fetch_stream.return_value = {'messages': ['Stream message']}

            messages = fetch_stream_messages('some-group', 'some-stream')

            self.assertEqual(messages, {'messages': ['Stream message']})
            self.assertEqual(mock_service.fetch_stream.call_count, 1)
            self.assertEqual(mock_service.fetch_stream.call_args_list,
                             [mock.call('some-group', 'some-stream', None, True)])
