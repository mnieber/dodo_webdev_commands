# noqa
import argparse
from dodo_commands.system_commands import DodoCommand
from dodo_commands.framework.util import remove_trailing_dashes


class Command(DodoCommand):  # noqa
    help = ""
    decorators = ["docker"]
    docker_options = [
        '--name=tape',
    ]

    def add_arguments_imp(self, parser):  # noqa
        parser.add_argument(
            'tape_args',
            nargs=argparse.REMAINDER
        )

    def handle_imp(self, tape_args, **kwargs):  # noqa
        webpack = self.get_config("/WEBPACK/webpack", "webpack")

        self.runcmd(
            [webpack, "--config", "webpack-test.config"],
            cwd=self.get_config("/WEBPACK/webpack_dir")
        )

        self.runcmd(
            [
                self.get_config("/TAPE/tape"),
                self.get_config("/TAPE/bundle_file"),
            ] + remove_trailing_dashes(tape_args)
        )
