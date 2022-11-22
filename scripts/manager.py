import os
from pathlib import Path
from glob import glob

from compose import Compose


class Manager:
    def __init__(self,  compose: Compose) -> None:
        self.compose: Compose = compose

    def create_volumes(self) -> None:
        for volume in self.compose.volumes:
            if not volume.exists():
                print(f"Creating volume {volume}")
                volume.mkdir(parents=True, exist_ok=True)

    def create_envs(self) -> None:
        env_templates: dict[str, Path] = {env.stem: env for env in self.get_env_templates()}
        env_files: dict[str, Path] = {env.stem: env for env in self.compose.envs}

        for f in set(env_templates.keys()) & set(env_files.keys()):
            self.create_file_from_template(env_templates[f], env_files[f])

        for f in set(env_files.keys()) - set(env_templates.keys()):
            if not env_files[f].exists():
                print(f"Warning: No template for {f} found. Creating empty file ({env_files[f]}).")
                env_files[f].touch(exist_ok=True)

    @staticmethod
    def create_file_from_template(template: Path, file: Path) -> None:
        if not file.exists():
            with open(template, "r") as f:
                template_content = f.read()
            with open(file, "w") as f:
                f.write(template_content)
        else:
            print(f"File {file} already exists. Not overwriting.")

    @staticmethod
    def get_env_templates() -> set[Path]:
        return set([Path(f) for f in glob(f"env/*.env-template")])

    @staticmethod
    def path_is_valid(path: str) -> bool:
        return not path.startswith("/")
