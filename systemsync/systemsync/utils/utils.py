from typing import List, Tuple
import subprocess as sp


def execute_command(
    cmd: str | List[str],
    wd: str | None = None,
    print_stderr: bool = True,
) -> Tuple[str, str]:
    """
    Macro to run a command using the subprocess `call` function

    Args:
        cmd (List[str]): the command to run (as a list of arguments)
        cwd (str): the working directory where to run this command
        print_stderr: print the stderr in the console if there's any
    Returns: a tuple
        stdout (str): the stdout output of the command
        stderr (str): the stderr output of the command
    """
    cmd = " ".join(cmd) if type(cmd) is list else cmd
    prog = sp.Popen(cmd, shell=True, cwd=wd, stdout=sp.PIPE, stderr=sp.PIPE)
    prog.wait()
    out, err = prog.communicate()
    out = bytes.decode(out).strip()
    err = bytes.decode(err).strip()

    if len(err) > 0 and print_stderr:
        print(err)

    return (out, err)
