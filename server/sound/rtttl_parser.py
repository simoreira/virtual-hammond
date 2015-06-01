import re

class RtttlParser:
    def __init__(self, rtttl):
        self.rtttl = rtttl

    def is_valid(self):
        # name     = get_name()
        # defaults = get_defaults()
        # notes    = get_notes()

        # if re.match(r'^(d=\d{1,2},o=\d,b=\d{1,3})?$', defaults) and ...

    def get_rtttl_parts(self):
        return self.rtttl.split(':')

    def get_name(self):
        return get_rtttl_parts()[0]

    def get_defaults(self):
        return get_rtttl_parts()[1]

    def get_notes(self):
        return get_rtttl_parts()[2]

    def parse(self):
        pass
