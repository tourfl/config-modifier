import logging
import argparse

import json

from load_change_file import load_change_file
from modify_config import modify_config

CONFIG_FILE_DEFAULT = "./inputs/config1.json"
CHANGE_FILE_DEFAULT = "./inputs/changes1.txt"


def main():
    """
    1. parses command line arguments
    2. read files
    3. achieves modifications
    """
    logging.basicConfig(level=logging.INFO)

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

    config_file_path = args.config or CONFIG_FILE_DEFAULT
    change_file_path = args.changes or CHANGE_FILE_DEFAULT

    # load config file
    with open(config_file_path) as config_file:
        config = json.load(config_file)

    # load changes file
    with open(change_file_path) as change_file:
        changes = load_change_file(change_file.read())

    modify_config(config, changes)

    print(json.dumps(config, indent=4))


if __name__ == "__main__":
    main()
