import fnmatch

METADATA_OPTIONS = {
    "Everything (Absolutely Everything)": None,
    "File": [
        "FileModifyDate", "FileAccessDate", "FileInodeChangeDate",
        "FilePermissions", "MIMEType", "FileType", "FileTypeExtension"
    ],
    "Image": [
        "ExifImageWidth", "ExifImageHeight", "JFIFVersion",
        "BitsPerSample", "ColorComponents", "YCbCrSubSampling",
        "ImageDescription"
    ],
    "EXIF": [
        "Make", "Model", "Orientation", "Software", "ModifyDate",
        "DateTimeOriginal", "CreateDate", "ExposureTime", "FNumber",
        "ISO", "ShutterSpeed", "Aperture", "ExposureCompensation",
        "ExposureProgram", "MeteringMode", "Flash", "FocalLength",
        "FocalLength35efl", "WhiteBalance", "ColorSpace", "ExifVersion",
        "SubSec*"
    ],
    "GPS": [
        "GPS*"
    ],
    "IPTC (captions / credits)": [
        "Headline", "Caption-Abstract", "ImageDescription", "Credit",
        "Source", "City", "State", "Country", "Creator", "Copyright",
        "CreatorTool", "CaptionWriter", "AuthorsPosition", "Title", "Rights",
        "Instructions"
    ],
    "Thumbnail": [
        "ThumbnailImage", "ThumbnailOffset", "ThumbnailLength",
        "PreviewImage", "PreviewImageValid", "PreviewImageStart", "PreviewImageLength"
    ],
    "ICC (color profile)": [
        "Profile*", "ICCProfileName", "ProfileCMMType", "ProfileVersion",
        "ProfileFileSignature", "ProfileDescription", "ProfileCreator",
        "ProfileDateTime", "ProfileConnectionSpace", "ProfileID"
    ],
    "Technical": [
        "Compression", "EncodingProcess", "JPEGInterchangeFormat*",
        "CompressionFactor", "BitsPerSample", "ColorComponents",
        "YCbCrPositioning", "YCbCrSubSampling"
    ],
    "MakerNotes": [
        "MakerNote*", "Warning*"
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