from pathlib import Path
import argparse

from compose import Compose
from manager import Manager

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create volumes for docker-compose'
    )
    parser.add_argument(
        'compose_file', type=str,
        help='Path to docker-compose file',
        default='docker-compose.yml'
    )
    args = parser.parse_args()

    compose_file: Path = Path(args.compose_file)

    compose = Compose(compose_file)
    manager = Manager(compose=compose)

    # exit if no envs are defined or all envs are already created
    if not manager.compose.envs:
        print("No envs defined")
        exit(0)
    elif all([v.exists() for v in manager.compose.envs]):
        print("All envs already exist")
        exit(0)

    print("In the given docker-compose file are the following env files defined:")
    print("-" * 20)

    for n, env in enumerate(manager.compose.envs):
        print(f"{n + 1}. {env}")

    print("-" * 20)

    print("Do you want to create these env files? [y/n]", end=" ")
    if input() == "y":
        manager.create_envs()
        print("Env files created.")
    else:
        print("Env files not created.")
    print("-" * 20)
