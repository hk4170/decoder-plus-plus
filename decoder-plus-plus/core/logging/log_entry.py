# vim: ts=8:sts=8:sw=8:noexpandtab
#
# This file is part of Decoder++
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class LogEntry(object):
    """ Defines a log entry including time, type and message. """

    def __init__(self, time: str, type: str, message: str):
        """
        Initializes a log entry including time, type and message.
        :param time: The time (hour:minute:second) of the log entry (e.g. 00:00:00).
        :param type: The type of the log entry (e.g. INFO, ERROR, ...).
        :param message: The message of the log entry (e.g. 'Hello, world!').
        """
        self._time = time
        self._type = type
        self._message = message

    def time(self) -> str:
        """ Returns the time (hour:minute:second) of the log entry (e.g. 00:00:00). """
        return self._time

    def type(self) -> str:
        """ Returns the type of the log entry (e.g. INFO, ERROR, ...). """
        return self._type

    def message(self) -> str:
        """ Returns the message of the log entry (e.g. 'Hello, world!'). """
        return self._message
