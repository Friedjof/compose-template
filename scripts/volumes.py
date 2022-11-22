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

    # exit if no volumes are defined or all volumes are already created
    if not manager.compose.volumes:
        print("No volumes defined")
        exit(0)
    elif all([v.exists() for v in manager.compose.volumes]):
        print("All volumes already exist")
        exit(0)

    print("In the given docker-compose file are the following volumes defined:")
    print("-" * 20)

    for n, volume in enumerate(manager.compose.volumes):
        print(f"{n + 1}. {volume}")

    print("-" * 20)

    print("Do you want to create these volumes? [y/n]", end=" ")
    if input() == "y":
        manager.create_volumes()
        print("Volumes created.")
    else:
        print("Volumes not created.")
    print("-" * 20)
