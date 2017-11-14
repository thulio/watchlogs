from server.entities.log_stream import LogStream
from server.repositories.stream_repository import list_streams


def execute(group):
    streams = list_streams('/{}'.format(group))
    return [LogStream.from_dict(group, stream) for stream in streams['logStreams']]
