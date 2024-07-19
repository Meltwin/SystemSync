from argparse import ArgumentParser
from ..utils.load import load_configuration


def dump_file(parser: ArgumentParser):
    parser.add_argument("file")
    args = parser.parse_args()

    print(load_configuration(args.file))



