class LogGroup(object):
    def __init__(self, name, streams=None):
        self.name = name
        self.streams = streams

    @classmethod
    def from_dict(cls, group_dict):
        return LogGroup(group_dict['logGroupName'])

    def __eq__(self, other):
        return self.name == other.name
