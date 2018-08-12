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

import importlib
import os
from typing import List

from core.command.command import Command


class AbstractPlugin(object):
    """ Base-class to all plugins. """

    def __init__(self, name: str, type: str, author: str, dependencies: List[str]=None):
        """
        Initializes a plugin.
        :param name: the name of the plugin.
        :param type: the type of the plugin (either DECODER, ENCODER, HASHER or SCRIPT).
        :param author: the author of the plugin.
        :param dependencies: the dependencies of the plugin (either None or a list of strings).
        """
        assert(name is not None and len(name) > 0), "Name is required and should not be None or Empty"
        assert(type in [Command.Type.DECODER, Command.Type.ENCODER, Command.Type.HASHER, Command.Type.SCRIPT]), \
            "Type is required and should be either 'DECODER', 'ENCODER', 'HASHER' or 'SCRIPT'"
        assert(author is not None and len(author) > 0), "Author is required and should not be None or Empty"
        self._name = name
        self._type = type
        self._author = author
        self._dependencies = dependencies

    def name(self) -> str:
        """ Returns the name of the plugin. """
        return self._name

    def type(self) -> str:
        """ Returns the type of the plugin (either DECODER, ENCODER, HASHER or SCRIPT). """
        return self._type

    def title(self) -> str:
        """ Returns the title of the plugin which is usually displayed to the user. """
        return "{} {}".format(self._name, self._type.capitalize())

    def author(self) -> str:
        """ Returns the author of the plugin. """
        return self._author

    def check_dependencies(self) -> List[str]:
        """
        Checks whether all specified dependencies can be loaded.
        :return: a list of unresolved dependencies, or an empty list if all dependencies could be resolved.
        """
        unresolved_dependencies = []
        if self._dependencies:
            for dependency in self._dependencies:
                try:
                    importlib.import_module(dependency)
                except Exception as e:
                    unresolved_dependencies.append(dependency)
        return unresolved_dependencies

    def run(self, *args, **kwargs) -> str:
        """ The main method of the plugin which must be implemented by the plugin. """
        raise NotImplementedError("Method must be implemented from upper class")

    def _run_lines(self, text: str, callback):
        """ Helper method which executes a callback for each line of text. """
        lines = []
        for text_line in text.splitlines():
            result = []
            for text_part in text_line.split(" "):
                if text_part:
                    result.append(callback(text_part))
            lines.append(' '.join(result))
        return os.linesep.join(lines)

    def select(self, *args, **kwargs) -> str:
        """
        This method is usually called when the plugin gets selected for execution.
        In its simplest form it may just call the run method. But it can also be used to ask the user for additional
        parameters (e.g. by displaying dialogs).
        """
        return self.run(*args)

    def __key(self):
        return (self._name, self._type)

    def __eq__(x, y):
        return x.__key() == y.__key()

    def __hash__(self):
        return hash(self.__key())


class DecoderPlugin(AbstractPlugin):

    def __init__(self, name: str, author: str, dependencies: List[str]=None):
        """
        Initializes a plugin.
        :param name: the name of the plugin.
        :param author: the author of the plugin.
        :param dependencies: the dependencies of the plugin (either None or a list of strings).
        """
        super(__class__, self).__init__(name, Command.Type.DECODER, author, dependencies)

    def can_be_decoded(self, input) -> bool:
        """
        Returns whether it might be possible to decode the specified input with this plugin.
        This methods needs to be implemented by a decoder-plugin to be able to be used with the "Smart decode"
        functionality.
        """
        return False

class EncoderPlugin(AbstractPlugin):

    def __init__(self, name: str, author: str, dependencies: List[str] = None):
        """
        Initializes a plugin.
        :param name: the name of the plugin.
        :param author: the author of the plugin.
        :param dependencies: the dependencies of the plugin (either None or a list of strings).
        """
        super(__class__, self).__init__(name, Command.Type.ENCODER, author, dependencies)


class HasherPlugin(AbstractPlugin):

    def __init__(self, name: str, author: str, dependencies: List[str] = None):
        """
        Initializes a plugin.
        :param name: the name of the plugin.
        :param author: the author of the plugin.
        :param dependencies: the dependencies of the plugin (either None or a list of strings).
        """
        super(__class__, self).__init__(name, Command.Type.HASHER, author, dependencies)


class ScriptPlugin(AbstractPlugin):

    def __init__(self, name: str, author: str, dependencies: List[str] = None):
        """
        Initializes a plugin.
        :param name: the name of the plugin.
        :param author: the author of the plugin.
        :param dependencies: the dependencies of the plugin (either None or a list of strings).
        """
        super(__class__, self).__init__(name, Command.Type.SCRIPT, author, dependencies)