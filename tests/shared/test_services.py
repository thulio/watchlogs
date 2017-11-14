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

    def test_list_streams(self):
        client = mock.Mock()
        client.describe_log_streams.return_value = {'logStreams': [{'logStreamName': 'stream-name'}]}

        service = CloudWatchService()
        service._client = client

        streams = service.list_streams('some-group')

        self.assertEqual(streams, {'logStreams': [{'logStreamName': 'stream-name'}]})
        self.assertEqual(client.describe_log_streams.call_count, 1)
        self.assertEqual(client.describe_log_streams.call_args_list, [mock.call(logGroupName='some-group')])

    def test_client_setup(self):
        with mock.patch('server.shared.services.boto3') as mock_boto:
            mock_boto.client.return_value = mock.Mock()
            service = CloudWatchService()
            assert service.client

            self.assertEqual(mock_boto.client.call_count, 1)
            self.assertEqual(mock_boto.client.call_args_list, [mock.call('logs')])