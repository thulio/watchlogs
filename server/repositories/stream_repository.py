from server.shared.services import CloudWatchService

cloudwatch = CloudWatchService()


def list_streams(group, token=None):
    return cloudwatch.list_streams(group, token)


def fetch_stream_messages(group, stream, token=None, from_start=True):
    return cloudwatch.fetch_stream(group, stream, token, from_start)
