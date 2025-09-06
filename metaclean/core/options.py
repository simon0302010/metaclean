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

def get_fields(option_name):
    return METADATA_OPTIONS.get(option_name, [])

def list_options():
    return list(METADATA_OPTIONS.keys())