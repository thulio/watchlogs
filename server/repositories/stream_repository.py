from server.shared.services import CloudWatchService

cloudwatch = CloudWatchService()


def list_streams(group):
    return cloudwatch.list_streams(group)


def fetch_stream_messages(group, stream, token=None, from_start=True):
    return cloudwatch.fetch_stream(group, stream, token, from_start)
