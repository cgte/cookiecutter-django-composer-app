import random

from doit.tools import title_with_actions
from pathlib import Path

IDENTIFIER = random.randint(1, 1000)


cookiecutter_source_directory = f"{Path(__file__).parent!s}"

directory_name = f"test_deploy_{IDENTIFIER}"
inner_identifier = f"inner_id_{IDENTIFIER}"


destination_directory = f"/tmp/test_pp_{inner_identifier}"


def task_default():

    return {
        "actions": [
            "echo ran",
            "",
            f"mkdir -p {destination_directory}/{IDENTIFIER}",
            f"cookiecutter {cookiecutter_source_directory} --no-input --output-dir {destination_directory} app_name=external_app_name",
        ],
        "verbosity": 2,
        "title": title_with_actions,
    }
