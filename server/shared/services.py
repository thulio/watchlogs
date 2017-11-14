import boto3


class CloudWatchService:
    def __init__(self):
        self._client = None

    def list_groups(self):
        return self.client.describe_log_groups()

    def list_streams(self, group_name):
        return self.client.describe_log_streams(logGroupName=group_name)

    @property
    def client(self):
        if not self._client:
            self._client = boto3.client('logs')

        return self._client
