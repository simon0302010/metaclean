import fnmatch

METADATA_OPTIONS = {
    "Everything": None,
    "GPS": [
        "GPSLatitude", "GPSLongitude", "GPSAltitude",
        "GPSLatitudeRef", "GPSLongitudeRef", "GPSAltitudeRef",
        "GPSImgDirection", "GPSDestLatitude", "GPSDestLongitude"
    ],
    "EXIF": [
        "DateTimeOriginal", "Make", "Model", "Orientation",
        "ExposureTime", "FNumber", "ISOSpeedRatings"
    ],
}

def get_fields(option_name, available_tags=None):
    patterns = METADATA_OPTIONS.get(option_name)

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
    return list(METADATA_OPTIONS.keys())