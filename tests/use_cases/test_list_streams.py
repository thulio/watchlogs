import unittest
import mock

from server.entities.log_stream import LogStream
from server.use_cases import list_streams


class TestListStreamsUseCase(unittest.TestCase):
    def test_execute(self):
        with mock.patch('server.use_cases.list_streams.list_streams') as mock_repository:
            mock_repository.return_value = {'logStreams': [{'logStreamName': 'stream-a'}]}

            streams = list_streams.execute('some-group')

            self.assertEqual(streams, [LogStream('some-group', 'stream-a')])
