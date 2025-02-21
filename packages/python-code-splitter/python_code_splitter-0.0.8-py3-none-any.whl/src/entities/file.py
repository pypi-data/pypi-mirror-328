from dataclasses import dataclass
from pathlib import Path

from src.consts import GIT_COMMIT
from src.entities.block import Block
from src.utils import git


@dataclass(frozen=True)
class File:
    path: Path
    blocks: list[Block]

    def move(self, to: Path) -> Path:
        if to.exists():
            raise FileExistsError(f"Error: File '{to}' already exists.")
        git(f"mv {self.path} {to}")
        git(f"add {to}")
        git(f'commit -m "[Auto] git mv {self.path} {to}"')
        if not GIT_COMMIT:
            self.path.rename(to)
        return to

    def move_to_init(self) -> Path:
        init_file_path = self.path.parent / self.path.stem / "__init__.py"
        return self.move(to=init_file_path)
