import os
import json
import subprocess

DATA_FILE = "tasks.json"

def run_cmd(cmd):
    """Run a CLI command and return its output."""
    result = subprocess.run(
        ["python", "src/main.py"] + cmd.split(),
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def test_add_and_list():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

    run_cmd('add "Test task"')
    output = run_cmd("list")
    assert "Test task" in output
    assert "❌" in output

def test_mark_done():
    run_cmd('done 1')
    output = run_cmd("list")
    assert "✅" in output
