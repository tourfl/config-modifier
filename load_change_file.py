import json


def load_change_file(file: str):
    """
    Input : content of the file as string
    Output: dict with change path as key
    """

    # string operations to get a json-like
    jsonized = "{%s}" % file.replace("\n", ",")

    changes = json.loads(jsonized)

    return changes
