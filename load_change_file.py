import json


def load_change_file(file: str):
    """
    Input : content of the file as string with one change per line
    Output: dict containing changes with pathes as keys
    """

    # some changes to get a json-like string
    file = file.replace("\n", ",")

    changes = json.loads("{%s}" % file)

    return changes
