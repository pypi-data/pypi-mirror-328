from datetime import datetime
from os.path import join
from unittest import TestCase
from unittest.mock import patch

from khalorg.khal.args import EditArgs, NewArgs
from khalorg.khal.helpers import set_tzinfo
from khalorg.org.agenda_items import OrgAgendaItem

from tests import static
from tests.agenda_items import AllDay, Recurring, Valid
from tests.helpers import (
    get_module_path,
    read_org_test_file,
)
from tests.test_khal.helpers import Mixin

FORMAT = '%Y-%m-%d %a %H:%M'


def test_config_khal():
    return join(get_module_path(static), 'test_config_khal')


@patch('khalorg.khal.args.find_configuration_file', new=test_config_khal)
class TestArgs(Mixin, TestCase):

    def test_load_from_org(self):
        """
        When loaded from the org file valid.org, the resulting cli
        args must be the same as: Valid.command_line_args
        .
        """
        actual: NewArgs = NewArgs()
        actual.load_from_org(self.agenda_item)
        expected: dict = Valid.command_line_args
        message: str = (
            f'\nActual: {actual}\n Expected: {expected}'
        )
        self.assertEqual(actual, expected, msg=message)

    def test_load_from_org_recurring(self):
        """ Same as test_load_from_org but then with a recurring time stamp."""
        args: list = Recurring.get_args()
        agenda_item: OrgAgendaItem = OrgAgendaItem(*args)
        actual: NewArgs = NewArgs()
        actual.load_from_org(agenda_item)
        expected: dict = Recurring.command_line_args
        self.assertEqual(actual, expected)

    def test_load_from_org_all_day_event(self):
        """
        Test case for loading an all-day event from Org AgendaItem.

        This test case verifies that the method `load_from_org` of the
        `NewArgs` class is able to load an all-day event from an
        `OrgAgendaItem` object and produce the expected output. The test checks
        whether the loaded event matches the expected event.

        Raises
        ------
            AssertionError: If the loaded event does not match the expected
            event.

        """
        args: list = AllDay.get_args()
        agenda_item: OrgAgendaItem = OrgAgendaItem(*args)
        actual: NewArgs = NewArgs()
        actual.load_from_org(agenda_item)
        expected: dict = AllDay.command_line_args
        message: str = (
            f'\n\nActual: {actual}\n\nExpected: {expected}'
        )
        self.assertEqual(actual, expected, msg=message)

    def test_optional(self):
        """ When adding an option, it can be retrieved using Args.optional. """
        key = '--url'
        value: str = 'www.test.com'
        args: NewArgs = NewArgs()
        args[key] = value
        self.assertEqual(value, args.optional[key])

    def test_positional(self):
        """
        When adding an positional arg, it can be retrieved using
        Args.optional.
        """
        key = 'foo'
        value: str = 'bar'
        args: NewArgs = NewArgs()
        args[key] = value
        self.assertEqual(value, args.positional[key])

    def test_as_list(self):
        """
        Args.as_list contatinates all Args in a list. The dictionary key of
        an option is prepended before its value. Of the positional args, only
        its value is retained (obviously). Later, all arguments are split based
        on a whitespace. Statements surrounded by quotes are not (yet)
        supported.
        """
        args: NewArgs = NewArgs()
        args['--url'] = 'www.test.com'
        args['--until'] = '2024-01-01 Mon 01:00'
        args['start'] = datetime(2023, 1, 1).strftime(FORMAT)

        expected: list = [
            '--url',
            'www.test.com',
            '--until',
            '2024-01-01 Mon 01:00',
            '2023-01-01 Sun 00:00']

        actual: list = args.as_list()
        self.assertEqual(actual, expected)


@patch('khalorg.khal.args.find_configuration_file', new=test_config_khal)
class TestEditArgs(Mixin, TestCase):

    def test(self):
        """
        For the agenda item `/test/static/agenda_items/recurring.org` the
        EditArgs should be equal to `expected`.
        """
        timezone = self.calendar.config['locale']['default_timezone']
        start = set_tzinfo(datetime(2023, 1, 1, 1, 0), timezone)
        end = set_tzinfo(datetime(2023, 1, 1, 2, 0), timezone)
        until = datetime(2023, 1, 2)
        expected: EditArgs = EditArgs(
            start=start,
            end=end,
            rrule={
                'FREQ': ['WEEKLY'],
                'UNTIL': [until]},
            uid='123',
            url='www.test.com',
            summary='Meeting',
            location='Somewhere',
            attendees=[
                'test@test.com',
                'test2@test.com'],
            categories=['Something'],
            description='Hello,\n\n  Lets have a meeting.\n\n  Regards,\n\n\n  Someone',
        )

        org_str: str = read_org_test_file('recurring.org')
        actual: EditArgs = EditArgs()
        org_item: OrgAgendaItem = OrgAgendaItem()

        org_item.load_from_str(org_str)
        actual.load_from_org(org_item)

        message: str = (
            f"\n\nActual is:\n{actual}"
            f"\n\nExpected is:\n{expected}"
        )
        self.assertTrue(actual == expected, msg=message)
