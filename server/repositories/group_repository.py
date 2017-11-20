from server.shared.services import CloudWatchService

cloudwatch = CloudWatchService()


def list_groups(token=None):
    if token:
        return cloudwatch.list_groups(token)
    else:
        return cloudwatch.list_groups()
