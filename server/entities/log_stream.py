class LogStream(object):
    def __init__(self, group, name):
        self.group = group
        self.name = name

    @classmethod
    def from_dict(cls, group, stream_dict):
        return LogStream(group, stream_dict['logStreamName'])

    def __eq__(self, other):
        return self.group == other.group and self.name == other.name
