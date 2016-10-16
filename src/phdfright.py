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

SUBMISSION_YEAR = 2017
SUBMISSION_MONTH = 10
SUBMISSION_DAY = 1

today = datetime.datetime.today()
submission_date = datetime.datetime(
    SUBMISSION_YEAR, SUBMISSION_MONTH, SUBMISSION_DAY)
days_remaining = (submission_date - today).days
years_remaining = int(days_remaining/365)
weeks_remaining = int(days_remaining/7)
working_days_remaining = int(weeks_remaining*5)
months_remaining = int(weeks_remaining/4)

print("You have a total of {} days left to submit.".format(days_remaining))

if years_remaining < 1:
    print("That is less than a year!!")

print("That is only {} months!".format(months_remaining))
print("That is only {} weeks!".format(weeks_remaining))
print("That is really only {} working days!".format(working_days_remaining))

print()
print("So I strongly suggest you get cracking!")
