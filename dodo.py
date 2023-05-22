import random

from doit.tools import title_with_actions
from pathlib import Path

IDENTIFIER = random.randint(1, 1000)

name = __file__

print(__file__)


directory_name = f"test_deploy_{IDENTIFIER}"
inner_identifier = f"inner_id_{IDENTIFIER}"


def task_default():

    return {
        "actions": ["echo ran", f"mkdir -P /tmp/test_pp_{inner_identifier}"],
        "verbosity": 2,
        "title": title_with_actions,
    }
