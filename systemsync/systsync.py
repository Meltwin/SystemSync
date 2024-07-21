from argparse import ArgumentParser
from enum import Enum

from systemsync.cli import dump_file, run_configuration


class AvailableCmds(Enum):
    UNKNOWN = ("---", None)
    DUMP = ("dump", dump_file)
    RUN = ("run", run_configuration)


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "cmd", choices=[m.value for m in AvailableCmds if m != AvailableCmds.UNKNOWN]
    )
    args = parser.parse_known_args()[0]
    AvailableCmds(args.cmd).value[1](parser)


if __name__ == "__main__":
    main()
