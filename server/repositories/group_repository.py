from server.shared.services import CloudWatchService

cloudwatch = CloudWatchService()


def list_groups():
    return cloudwatch.list_groups()
