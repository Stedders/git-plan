"""Help command

@author Rory Byrne <rory@rory.bio>
"""
from typing import Any

from git_plan.cli.commands.command import Command


class Template(Command):  # pylint: disable=too-few-public-methods
    """Add or edit templates."""

    subcommand = 'template'

    def command(self, **kwargs):
        """Create a new commit"""
        self._cli.help()

    def register_subparser(self, subparsers: Any):
        subparsers.add_parser(Template.subcommand, help='Create or edit custom plan templates.')
