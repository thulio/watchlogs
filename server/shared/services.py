import boto3


class CloudWatchService:
    def __init__(self):
        self._client = None

    def list_groups(self, token=None):
        if token:
            response = self.client.describe_log_groups(nextToken=token)

            if self.finished(token, response.get('nextToken', '')):
                return {}
            else:
                return response

        else:
            return self.client.describe_log_groups()

    def list_streams(self, group_name, token=None):
        if token:
            response = self.client.describe_log_streams(logGroupName=group_name, nextToken=token)

            if self.finished(token, response.get('nextToken', '')):
                return {}
            else:
                return response

        else:
            return self.client.describe_log_streams(logGroupName=group_name)

    def fetch_stream(self, group_name, stream_name, token=None, from_start=True):
        if token:
            response = self.client.get_log_events(logGroupName=group_name,
                                                  logStreamName=stream_name,
                                                  startFromHead=from_start,
                                                  nextToken=token)

            if self.finished(token, response.get('nextToken', '')):
                return {}
            else:
                return response

        else:
            return self.client.get_log_events(logGroupName=group_name,
                                              logStreamName=stream_name,
                                              startFromHead=from_start)

    @property
    def client(self):
        if not self._client:
            self._client = boto3.client('logs')

        return self._client

    @staticmethod
    def finished(current_token, next_token):
        return current_token == next_token
