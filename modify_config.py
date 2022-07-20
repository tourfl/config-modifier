import logging


def modify_config(config: dict, changes: dict) -> dict:
    """
    operates changes on config
    """
    line = 0
    c = 0  # changes achieved

    for str_path, value in changes.items():
        path = parse_path(str_path)  # path is a list of string or integer
        line += 1

        try:
            modify_value(config, path, value)
            logging.info(" [%i] Successful transformation: %s", line, str_path)
            c += 1

        except (KeyError, IndexError):
            logging.error(" [%i] Invalid path: %s", line, str_path)
            # add some logging

    logging.info(" %i/%i changes achieved", c, line)

    return config


def parse_path(str_path: str) -> list:
    """
    parses the point-separated string
    also parses the integer inside brackets

    Example:
    input : "test.page1[0].config"
    output: ["test", "page1", 0, "config"]
    """
    # the list to be filled
    path = []

    # parses point-separated keys
    keys = str_path.split(".")

    # parses integers inside brackets
    for key in keys:

        # split, if exist, the left bracket
        s = key.split("[")
        path.append(s.pop(0))

        # find the integer value
        if s:  # means there were actually a left bracket
            val = int(s.pop(0).split("]")[0])  # works as well if there were no "]"
            path.append(val)

    return path


def modify_value(config: dict, path: list, value: str):
    """
    modify the config value given the path
    """
    last_key = path.pop()  # keeps the last key to be able to modify the content

    for key in path:  # recursively travels accross path
        config = config[key]

    # modifies the config content, thanks to pass-by-reference python mechanism
    if config[last_key]:
        config[last_key] = value
