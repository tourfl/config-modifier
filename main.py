import logging
import argparse

import json

from load_change_file import load_change_file
from modify_config import modify_config

CONFIG_PATH_DEFAULT = "./inputs/config1.json"
CHANGE_PATH_DEFAULT = "./inputs/changes1.txt"


def main():
    """
    1. parses command line arguments
    2. reads files
    3. achieves modifications
    """
    logging.basicConfig(format="%(message)s", level=logging.INFO)

    parser = argparse.ArgumentParser(description="config modification script")
    parser.add_argument(
        "--config",
        help="input file containing config",
    )
    parser.add_argument(
        "--changes",
        help="input file containing changes",
    )

    args = parser.parse_args()

    config_path = args.config or CONFIG_PATH_DEFAULT
    changes_path = args.changes or CHANGE_PATH_DEFAULT

    # loads config
    with open(config_path) as file:
        config = json.load(file)

    # loads changes
    with open(changes_path) as file:
        changes = load_change_file(file.read())

    modify_config(config, changes)

    print(json.dumps(config, indent=4))


if __name__ == "__main__":
    main()
