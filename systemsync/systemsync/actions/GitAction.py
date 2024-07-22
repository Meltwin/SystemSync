from typing import List, Tuple
from ..data import GitTask
from .IAction import IAction
from ..utils.logger import Logger, LogSource

import os
import subprocess as sp
import re


class GitAction(IAction[GitTask]):
    """
    This class takes a GitTask as input and manage it.
    """

    def __int__(self, task: GitTask):
        super().__init__(task)

    def _run(self):
        # Compute local directory name
        if self._task.dirname is None:
            default_dirname = self._get_repo_default_name()
            if default_dirname is None:
                Logger.error("Can't determine local repository folder name!")
                return
            self._task.dirname = default_dirname
        self._task.dest = os.path.expanduser(self._task.dest)

        # Check if directory already exist, in this case update it
        if not os.path.exists(os.path.join(self._task.dest, self._task.dirname)):
            return self._clone_repo()

        # Check if git repository
        if not self._is_repository():
            return Logger.error(
                LogSource.ACTION, "Folder already exist but isn't a repository!"
            )

        # Check branch
        actual_branch = self._fetch_repo_branch()
        Logger.info(LogSource.ACTION, f"Actual branch is: {actual_branch}")
        if self._task.branch is not None and actual_branch != self._task.branch:
            self._switch_branch()

        # Else, we can just update the repository
        self._update_repo()

    # =========================================================================

    def _switch_branch(self):
        """
        Switch branch inside of the repository
        """
        Logger.info(LogSource.ACTION, "Switching git branch!")
        self._reset_repo()
        self.__run_cmd(" ".join(["git", "checkout", self._task.branch]))

    def _update_repo(self):
        """
        Update the repository based from the task
        """
        Logger.info(LogSource.ACTION, "Updating repository!")

        # Reset to default in case of modifications
        self._reset_repo()

        # Update it
        self.__run_cmd(" ".join(["git", "pull"]))
        self.__run_cmd(" ".join(["touch", "test.txt"]))

    def _clone_repo(self):
        """
        Clone a git repository according to the GitTask.
        """
        # Construct command
        cmd = f"git clone {self._task.repo}"
        if self._task.branch is not None:
            cmd += f" -b {self._task.branch}"

        # Run command
        self.__run_cmd(cmd, False)

    def _fetch_repo_branch(self) -> str:
        """
        Fetch the current branch

        Returns:
            str: the name of the branch where we are
        """
        out, _ = self.__run_cmd('git branch -la | grep -o "^\\*.*"')
        return out.split(" ")[1]

    def _reset_repo(self) -> None:
        """
        Reset the repository (if exist)
        """
        self.__run_cmd(" ".join(["git", "reset", "--hard"]))

    # =========================================================================

    def _is_repository(self) -> bool:
        """
        Check whether a directory is a git repository

        Returns:
            bool: True if the dir is a repository
        """
        git_dir = os.path.join(self._task.dest, self._task.dirname, ".git")
        return os.path.exists(git_dir)

    def _get_repo_default_name(self) -> str | None:
        """
        Get the default repository directory name based on the git url

        Returns:
            str: the dirname
        """
        match = re.findall("\/([a-zA-Z0-9]*).git$", self._task.repo)
        return match[0]

    def __run_cmd(self, cmd: List[str], inside: bool = True) -> Tuple[str, str]:
        """
        Macro to run a command using the subprocess `call` function

        Args:
            cmd (List[str]): the command to run (as a list of arguments)
        """
        if inside:
            wd = os.path.join(self._task.dest, self._task.dirname)
        else:
            wd = self._task.dest

        prog = sp.Popen(cmd, shell=True, cwd=wd, stdout=sp.PIPE, stderr=sp.PIPE)
        prog.wait()
        out, err = prog.communicate()
        return (bytes.decode(out).strip(), bytes.decode(err).strip())
