import re


class Event:
    """A structured event with a type, scope, and description"""

    def __init__(self, type, description, scope=None):
        if type is None or type.strip() == '':
            raise EventConstructorError('type required')

        if description is None or description.strip() == '':
            raise EventConstructorError('description required')

        self._type = type
        self._scope = scope
        self._description = description

    @property
    def type(self):
        return self._type

    @property
    def description(self):
        return self._description

    @property
    def scope(self):
        return self._scope

    def __str__(self):
        """Format Event as a string"""

        result = ''
        if self._scope:
            result = str.format('{}({}): {}', self._type, self._scope, self._description)
        else:
            result = str.format('{}: {}', self._type, self._description)

        return result.rstrip()

    @classmethod
    def parse(cls, value):
        p = re.compile(r'(?P<type>\w+){1}(\((?P<scope>[^\(\)\[\]\{\}]+)\))?:(?P<desc>.*){1}')
        m = p.fullmatch(value)

        if m is None:
            raise EventParseError('could not parse conventional event', value)

        type = m.group('type')
        scope = m.group('scope')
        description = m.group('desc').strip()

        return cls(type, description, scope)


class EventConstructorError(Exception):
    """Indicates an error occured constructing an Event.
    This typically happens due to bad formating of the Event attributes such
    as type, scope, etc."""

    def __init__(self, message):
        self.message = message


class EventParseError(Exception):
    """Indicates that an error occured trying to parse a string into an Event."""

    def __init__(self, message, value):
        self.message = message
        self.value = value
