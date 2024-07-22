from argparse import ArgumentParser
from enum import Enum

from systemsync.cli import dump_file, run_configuration


class AvailableCmds(Enum):
    UNKNOWN = "---"
    DUMP = "dump"
    RUN = "run"


cmd_mapping = {
    AvailableCmds.UNKNOWN: None,
    AvailableCmds.DUMP: dump_file,
    AvailableCmds.RUN: run_configuration,
}


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "cmd", choices=[m.value for m in AvailableCmds if m != AvailableCmds.UNKNOWN]
    )
    args = parser.parse_known_args()[0]
    cmd_mapping[AvailableCmds(args.cmd)](parser)


if __name__ == "__main__":
    main()
