#!/usr/bin/env python3
"""
Config file that holds information on dates.

File: config.py

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

THESIS_SUBMISSION_DATE = datetime.datetime(2017, 10, 1, 12, 00)

CONFERENCES_DEADLINES = {
    'CNS 2017 in Antwerp': datetime.datetime(2017, 3, 6, 00, 00),
}

JOURNAL_DEADLINES = {
}

MISC_DEADLINES = {
    'CNS 2017 Travel grant application submission':
    datetime.datetime(2017, 3, 6, 00, 00),
    'CNS 2017 Registration':
    datetime.datetime(2017, 5, 18, 00, 00),
}
