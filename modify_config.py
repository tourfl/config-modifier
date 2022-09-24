import logging

from termcolor import colored


def modify_config(config: dict, changes: dict) -> dict:
    """
    1. operates changes on config
    2. logs
    """
    line = 0
    success = 0

    for str_path, value in changes.items():
        path = parse_path(str_path)
        line += 1

        try:
            modify_value(config, path, value)
            logging.info(colored(f' [{line}] Success! "{str_path}": {value}', "green"))
            success += 1

        except (KeyError, IndexError):
            logging.error(colored(f' [{line}] Invalid path! "{str_path}"', "red"))

    logging.info(f" {success}/{line} changes achieved")

    return config


def parse_path(str_path: str) -> list:
    """
    parses dict keys and list indexes from a string.
    dict keys are point-separated strings, list indexes are integers inside brackets.

    Example:
    input : "test.page1[0].config"
    output: ["test", "page1", 0, "config"]
    """
    path = []

    keys = str_path.split(".")

    # parses list indexes (integer inside brackets)
    for key in keys:

        s = key.split("[")
        path.append(s.pop(0))

        if s:  # means there were actually a left bracket
            val = int(s.pop(0).split("]")[0])  # works too without "]"
            path.append(val)

    return path


def modify_value(config: dict, path: list, value: str):
    """
    modify the config value given the path
    """
    last_key = path.pop()  # keeps the last key to be able to modify the value

    for key in path:  # recursively travels accross path
        config = config[key]

    # modifies the config content, thanks to pass-by-reference python mechanism
    if config[last_key]:
        config[last_key] = value
