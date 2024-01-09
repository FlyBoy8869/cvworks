from collections import namedtuple
from datetime import date

from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY

WORKS = True
OFF = False

#                 Mon    Tue    Wed  Thr  Fri    Sat    Sun
MASK_EVEN_WEEK = (WORKS, WORKS, OFF, OFF, WORKS, WORKS, WORKS)
MASK_ODD_WEEK = (OFF, OFF, WORKS, WORKS, OFF, OFF, OFF)

Schedule = namedtuple("Schedule", "working date")


def mondays_date(a_date: date) -> date:
    """Return Monday's date for the week containing the given date."""
    return a_date - relativedelta(a_date, days=a_date.weekday())


def week_number(a_date: date) -> int:
    """Return the ISO week number for the given date."""
    return a_date.isocalendar().week


def is_week_even(iso_week_number: int) -> bool:
    """Return True if week is even, else False."""
    return iso_week_number % 2 == 0


def dates_for_week(a_date: date) -> tuple[date, ...]:
    """Return a list of datetime.date objects for the week of the given date."""
    return tuple([d.date() for d in rrule(freq=DAILY, count=7, dtstart=a_date)])


def _week_mask(iso_week_number: int) -> tuple[bool, ...]:
    return MASK_EVEN_WEEK if is_week_even(iso_week_number) else MASK_ODD_WEEK


def get_week_schedule(day: date) -> tuple[Schedule, ...]:
    """Christina's schedule for the week containing the given date.

    returns namedtuple Schedule(bool, datetime.date)"""

    mask = _week_mask(week_number(day))

    week_schedule = []
    for index, d in enumerate(dates_for_week(mondays_date(day))):
        week_schedule.append(Schedule(WORKS if mask[index] else OFF, d))
    return tuple(week_schedule)


def working_this_day(day: date) -> bool:
    week_schedule = get_week_schedule(day)
    for d in week_schedule:
        if d.date == day:
            return d.working
