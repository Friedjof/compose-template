import yaml
from pathlib import Path


class Compose:
    def __init__(self, compose_file: Path) -> None:
        self.compose_file: Path = compose_file
        self.volumes: set[Path] = self.get_relativ_volume_paths()
        self.envs: set[Path] = self.get_env_files()

    def read_compose_file(self) -> dict:
        with open(self.compose_file, "r") as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def get_volumes(self) -> set[str]:
        volumes = []
        for service in self.read_compose_file()["services"].values():
            volumes.extend(service.get("volumes", []))
        return set(volumes)

    def get_volume_paths(self) -> set[Path]:
        paths: list[Path] = []
        for volume in self.get_volumes():
            paths.append(Path(volume.split(":")[0]))
        return set(paths)

    def get_relativ_volume_paths(self) -> set[Path]:
        paths: list[Path] = []
        for volume in self.get_volumes():
            path: Path = Path(volume.split(":")[0])
            if self.path_is_relative(path):
                paths.append(path)
        return set(paths)

    def get_env_files(self) -> set[Path]:
        envs: list[Path] = []
        for service in self.read_compose_file()["services"].values():
            for env_file in service.get("env_file", []):
                if self.path_is_relative(Path(env_file)):
                    envs.append(Path(env_file))
        return set(envs)

    @staticmethod
    def path_is_relative(path: Path):
        return not str(path).startswith("/")
