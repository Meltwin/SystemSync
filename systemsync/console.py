from argparse import ArgumentParser
from enum import Enum

from systemsync.cli import dump_file, run_configuration


class AvailableCmds(Enum):
    UNKNOWN = "---"
    DUMP = "dump"
    RUN = "run"


def main():
    parser = ArgumentParser()
    parser.add_argument("cmd", choices=[m.value for m in AvailableCmds if m != AvailableCmds.UNKNOWN])
    args = parser.parse_known_args()[0]

    match AvailableCmds(args.cmd):
        case AvailableCmds.DUMP:
            dump_file(parser)
        case AvailableCmds.RUN:
            run_configuration(parser)
        case _:
            print("Unknown command")


if __name__ == "__main__":
    main()
