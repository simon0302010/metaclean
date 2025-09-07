import json
import fnmatch
import importlib.resources


with importlib.resources.open_text("metaclean.data", "options.json") as options_file:
    metadata_options = json.load(options_file)

def get_fields(option_name, available_tags=None):
    patterns = metadata_options.get(option_name)

    if patterns is None:
        return None

    if available_tags is None:
        return list(patterns)

    matched = set()
    for pat in patterns:
        if any(ch in pat for ch in "*?[]"):
            for t in available_tags:
                if fnmatch.fnmatchcase(t, pat):
                    matched.add(t)
        else:
            if pat in available_tags:
                matched.add(pat)

    return list(matched)


def list_options():
    return list(metadata_options.keys())
