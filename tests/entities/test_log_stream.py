import unittest

from server.entities.log_stream import LogStream


class TestLogstream(unittest.TestCase):
    def test_from_dict(self):
        stream_dict = {'logStreamName': 'stream-name'}

        log_stream = LogStream.from_dict('some-group', stream_dict)

        self.assertEqual(log_stream.name, 'stream-name')

    def test_eq(self):
        stream_1 = LogStream('some-group', 'name')
        stream_2 = LogStream('some-group', 'name')
        stream_3 = LogStream('some-other-group', 'name')

        self.assertEqual(stream_1, stream_2)
        self.assertNotEqual(stream_1, stream_3)
