import boto3


class CloudWatchService:
    def __init__(self):
        self._client = None

    def list_groups(self):
        return self.client.describe_log_groups()

    def list_streams(self, group_name):
        return self.client.describe_log_streams(logGroupName=group_name)

    def fetch_stream(self, group_name, stream_name, token=None, from_start=True):
        if token:
            return self.client.get_log_events(logGroupName=group_name,
                                              logStreamName=stream_name,
                                              startFromHead=from_start,
                                              nextToken=token)
        else:
            return self.client.get_log_events(logGroupName=group_name,
                                              logStreamName=stream_name,
                                              startFromHead=from_start)

    @property
    def client(self):
        if not self._client:
            self._client = boto3.client('logs')

        return self._client
