from server.shared.services import CloudWatchService

cloudwatch = CloudWatchService()


def list_streams(group):
    return cloudwatch.list_streams(group)
