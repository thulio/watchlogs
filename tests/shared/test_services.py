import unittest

import mock

from server.shared.services import CloudWatchService


class TestCloudWatchService(unittest.TestCase):
    def test_list_groups(self):
        client = mock.Mock()
        client.describe_log_groups.return_value = {'logGroups': [{'logGroupName': 'group-name'}]}

        service = CloudWatchService()
        service._client = client

        groups = service.list_groups()

        self.assertEqual(groups, {'logGroups': [{'logGroupName': 'group-name'}]})
        self.assertEqual(client.describe_log_groups.call_count, 1)
        self.assertEqual(client.describe_log_groups.call_args_list, [mock.call()])

    def test_list_groups_with_token(self):
        client = mock.Mock()
        client.describe_log_groups.return_value = {'logGroups': [{'logGroupName': 'group-name'}]}

        service = CloudWatchService()
        service._client = client

        groups = service.list_groups('next-token')

        self.assertEqual(groups, {'logGroups': [{'logGroupName': 'group-name'}]})
        self.assertEqual(client.describe_log_groups.call_count, 1)
        self.assertEqual(client.describe_log_groups.call_args_list, [mock.call(nextToken='next-token')])

    def test_list_groups_end_of_pagination(self):
        client = mock.Mock()
        client.describe_log_groups.return_value = {'logGroups': [{'logGroupName': 'group-name'}],
                                                   'nextToken': 'next-token'}

        service = CloudWatchService()
        service._client = client

        groups = service.list_groups('next-token')

        self.assertEqual(groups, {})
        self.assertEqual(client.describe_log_groups.call_count, 1)
        self.assertEqual(client.describe_log_groups.call_args_list, [mock.call(nextToken='next-token')])

    def test_list_streams(self):
        client = mock.Mock()
        client.describe_log_streams.return_value = {'logStreams': [{'logStreamName': 'stream-name'}]}

        service = CloudWatchService()
        service._client = client

        streams = service.list_streams('some-group')

        self.assertEqual(streams, {'logStreams': [{'logStreamName': 'stream-name'}]})
        self.assertEqual(client.describe_log_streams.call_count, 1)
        self.assertEqual(client.describe_log_streams.call_args_list, [mock.call(logGroupName='some-group')])

    def test_list_streams_with_token(self):
        client = mock.Mock()
        client.describe_log_streams.return_value = {'logStreams': [{'logStreamName': 'stream-name'}]}

        service = CloudWatchService()
        service._client = client

        streams = service.list_streams('some-group', 'next-token')

        self.assertEqual(streams, {'logStreams': [{'logStreamName': 'stream-name'}]})
        self.assertEqual(client.describe_log_streams.call_count, 1)
        self.assertEqual(client.describe_log_streams.call_args_list,
                         [mock.call(logGroupName='some-group', nextToken='next-token')])

    def test_list_streams_end_of_pagination(self):
        client = mock.Mock()
        client.describe_log_streams.return_value = {'logStreams': [{'logStreamName': 'stream-name'}],
                                                    'nextToken': 'next-token'}

        service = CloudWatchService()
        service._client = client

        streams = service.list_streams('some-group', 'next-token')

        self.assertEqual(streams, {})
        self.assertEqual(client.describe_log_streams.call_count, 1)
        self.assertEqual(client.describe_log_streams.call_args_list,
                         [mock.call(logGroupName='some-group', nextToken='next-token')])

    def test_client_setup(self):
        with mock.patch('server.shared.services.boto3') as mock_boto:
            mock_boto.client.return_value = mock.Mock()
            service = CloudWatchService()
            assert service.client

            self.assertEqual(mock_boto.client.call_count, 1)
            self.assertEqual(mock_boto.client.call_args_list, [mock.call('logs')])

    def test_fetch_stream_without_token(self):
        client = mock.Mock()
        client.get_log_events.return_value = {
            'messages': ['Stream message']
        }

        service = CloudWatchService()
        service._client = client

        messages = service.fetch_stream('some-group', 'some-stream')

        self.assertEqual(len(messages), 1)
        self.assertEqual(client.get_log_events.call_count, 1)
        self.assertEqual(client.get_log_events.call_args_list, [mock.call(logGroupName='some-group',
                                                                          logStreamName='some-stream',
                                                                          startFromHead=True)])

    def test_fetch_stream_with_token(self):
        client = mock.Mock()
        client.get_log_events.return_value = {
            'messages': ['Stream message']
        }

        service = CloudWatchService()
        service._client = client

        messages = service.fetch_stream('some-group', 'some-stream', 'next-token')

        self.assertEqual(len(messages), 1)
        self.assertEqual(client.get_log_events.call_count, 1)
        self.assertEqual(client.get_log_events.call_args_list, [mock.call(logGroupName='some-group',
                                                                          logStreamName='some-stream',
                                                                          nextToken='next-token',
                                                                          startFromHead=True)])

    def test_fetch_stream_end_of_pagination(self):
        client = mock.Mock()
        client.get_log_events.return_value = {
            'messages': ['Stream message'],
            'nextToken': 'next-token'
        }

        service = CloudWatchService()
        service._client = client

        messages = service.fetch_stream('some-group', 'some-stream', 'next-token')

        self.assertEqual(messages, {})
        self.assertEqual(client.get_log_events.call_count, 1)
        self.assertEqual(client.get_log_events.call_args_list, [mock.call(logGroupName='some-group',
                                                                          logStreamName='some-stream',
                                                                          nextToken='next-token',
                                                                          startFromHead=True)])

    def test_finished(self):
        current_token = 'some-token'
        next_token = 'other-token'
        same_token = 'some-token'

        self.assertFalse(CloudWatchService.finished(current_token, next_token))
        self.assertTrue(CloudWatchService.finished(current_token, same_token))
