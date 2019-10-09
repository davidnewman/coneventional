import pytest

import coneventional.event as event


class TestEvent:

    def test_full_init(self):
        e = event.Event('pto', 'Going to the dentist', 'tester@foo.com')

        assert e.type == 'pto'
        assert e.scope == 'tester@foo.com'
        assert e.description == 'Going to the dentist'

    def test_event_string_rep(self):
        e = event.Event('pto', 'Going to the dentist', 'tester@foo.com')
        s = str.format('{}', e)

        assert s == 'pto(tester@foo.com): Going to the dentist'

    def test_event_string_rep_no_scope(self):
        e = event.Event('pto', 'Going to the dentist')
        s = str.format('{}', e)

        assert s == 'pto: Going to the dentist'

    def test_event_readonly(self):
        e = event.Event('pto', 'Going to the dentist', 'tester@foo.com')

        with pytest.raises(AttributeError):
            e.type = 'wfh'

        with pytest.raises(AttributeError):
            e.scope = 'mickey@disney.com'

        with pytest.raises(AttributeError):
            e.description = 'Global domination'

        assert e.type == 'pto'
        assert e.scope == 'tester@foo.com'
        assert e.description == 'Going to the dentist'

    def test_event_fails_with_no_type(self):
        with pytest.raises(event.EventConstructorError) as excinfo:
            event.Event('', 'Going to the dentist')

        assert 'type required' == excinfo.value.message

    def test_event_fails_with_no_description(self):
        with pytest.raises(event.EventConstructorError) as excinfo:
            event.Event('pto', None)

        assert 'description required' == excinfo.value.message

    def test_parse_full_event(self):
        e = event.Event.parse('pto(tester@foo.com): Going to the dentist')

        assert e.type == 'pto'
        assert e.scope == 'tester@foo.com'
        assert e.description == 'Going to the dentist'

    def test_parse_event_without_scope(self):
        e = event.Event.parse('pto: Going to the dentist')

        assert e.type == 'pto'
        assert e.scope is None
        assert e.description == 'Going to the dentist'

    def test_event_parse_fails_with_no_type(self):
        with pytest.raises(event.EventParseError) as excinfo:
            event.Event.parse(': Going to the dentist')

        assert 'could not parse conventional event' == excinfo.value.message

    def test_event_parse_fails_with_no_description(self):
        with pytest.raises(event.EventConstructorError) as excinfo:
            event.Event.parse('pto:')

        assert 'description required' == excinfo.value.message
