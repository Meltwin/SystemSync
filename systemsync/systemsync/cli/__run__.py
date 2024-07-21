from argparse import ArgumentParser
from ..utils.load import load_configuration
from ..actions import IAction, ActionFactory


def run_configuration(parser: ArgumentParser):
    parser.add_argument("file")
    args = parser.parse_args()
    config = load_configuration(args.file)

    print(f"Syncing configuration {config.name} v{config.version}")
    for p in config.projects:
        print(f"+ Running project {p.name} [{len(p.tasks)} tasks]")
        for t in p.tasks:
            print(f"\t- Running task {t}")

            action = ActionFactory.action_from_task(t)
            action.run()
