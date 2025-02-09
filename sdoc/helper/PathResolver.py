from pathlib import Path

from sdoc.Exception.SDocException import SDocException


class PathResolver:
    """
    Utility class for safely resolving paths.
    """
    # ------------------------------------------------------------------------------------------------------------------
    _home: Path | None = None
    """
    The home folder of the current project.
    """

    _main: Path | None = None
    """
    The home folder of the current project.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def resolve_path(parent_file: str, local_file: str) -> str:
        """
        Resolves a path from a parent file to a path relative to the CWD.

        :param parent_file: The parent file.
        :param local_file: The file referenced in the parent file.
        """
        parent_path = Path(parent_file).parent
        local_path = Path(local_file)
        if local_path.is_absolute():
            full_path = PathResolver._home.joinpath(str(local_path).lstrip('/')).resolve()
        else:
            full_path = parent_path.joinpath(local_path).resolve()

        if not full_path.is_relative_to(PathResolver._home):
            raise SDocException(f"Path '{full_path}' is not under '{PathResolver._home}'.")

        return str(full_path.relative_to(PathResolver._home))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def set_home(main: str) -> None:
        """
        Set the home folder of the current project.

        :param main: The path to the root SDoc file.
        """
        resolved = Path.cwd().resolve()

        if PathResolver._home is not None and PathResolver._home != resolved:
            raise RuntimeError('Home folder is set already.')

        PathResolver._home = resolved
        PathResolver._main = Path(main).resolve().parent

# ----------------------------------------------------------------------------------------------------------------------
