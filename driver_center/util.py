import subprocess


def fetch_file(path):
    with open(path, "r") as f:
        return {path: f.read()}


def run_cmd(cmd, **kwargs):
    kwargs.setdefault("shell", True)
    cmd = "LANG=C " + cmd
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, **kwargs)
    return {cmd: p.communicate()[0]}
