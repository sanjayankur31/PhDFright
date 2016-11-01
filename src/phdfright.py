#!/usr/bin/env python3
"""
Remind me how long I have left and scare me.

File: phdfright.py

Copyright 2016 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import datetime
from config import THESIS_SUBMISSION_DATE, CONFERENCES_DEADLINES
from config import JOURNAL_DEADLINES, MISC_DEADLINES


def calculatedeltas(submission_date):
    """Calculate delta metrics."""
    today = datetime.datetime.today()
    print("{0:>30s}: {1:<10d} days".format(
        "Days remaining", (submission_date - today).days))
    print("{0:>30s}: {1:<10f} weeks".format(
        "Weeks remaining", (submission_date - today).days/7.))
    print("{0:>30s}: {1:<10f} months".format(
        "Months remaining", (submission_date - today).days/(7.*4.)))
    print("{0:>30s}: {1:<10f} years".format(
        "Years remaining", (submission_date - today).days/(365.)))
    print("{0:>30s}: {1:<10f} days".format(
        "Working days remaining", 5. * (submission_date - today).days/(7.)))


print("{0:>40s}".format("*** THESIS ***"))
print()
print("- {0}: {1:<10s}".format(
    "Planned submission date", THESIS_SUBMISSION_DATE.ctime()))
print()
calculatedeltas(THESIS_SUBMISSION_DATE)
print("{0:>40s}".format("--------------"))
print()

print("{0:>40s}".format("*** CONFERENCES ***"))
for conf, deadline in CONFERENCES_DEADLINES.items():
    print()
    print("- {0}: {1:<10s}".format(conf, deadline.ctime()))
    print()
    calculatedeltas(deadline)
    print("{0:>40s}".format("--------------"))

print()
print("{0:>40s}".format("*** JOURNALS ***"))
for conf, deadline in JOURNAL_DEADLINES.items():
    print()
    print("- {0}: {1:<10s}".format(conf, deadline.ctime()))
    print()
    calculatedeltas(deadline)
    print("{0:>40s}".format("--------------"))

print()
print("{0:>40s}".format("*** OTHERS ***"))
for conf, deadline in MISC_DEADLINES.items():
    print()
    print("- {0}: {1:<10s}".format(conf, deadline.ctime()))
    print()
    calculatedeltas(deadline)
    print("{0:>40s}".format("--------------"))
