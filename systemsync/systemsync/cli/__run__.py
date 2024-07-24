from argparse import ArgumentParser
from ..utils.config import load_configuration, compute_vars
from ..actions import ActionFactory


def run_configuration(parser: ArgumentParser):
    parser.add_argument("file")
    args = parser.parse_args()
    config = load_configuration(args.file)

    print(f"Syncing configuration {config.name} v{config.version}")
    for p in config.projects:
        print(f"+ Running project {p.name} [{len(p.tasks)} tasks]")

        vars = compute_vars(p)
        for k, v in vars.items():
            print(f"\t- Var {k} = '{v}' [{type(v).__name__}]")

        for t in p.tasks:
            action = ActionFactory.action_from_task(t, vars)
            print(f"\t- Running task {action._task}...")
            if action.run():
                print("\t    Action finished!")
            else:
                print("\t    Aborted..")
