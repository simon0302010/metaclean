import sys
from . import exiftool, options

def process_images(filenames, selected_options):
    for path in filenames:
        try:
            metadata = list(exiftool.get_metadata(path).keys())
        except Exception as e:
            print(f"\033[31mFailed to read metadata for {path}: {e}\033[0m", file=sys.stderr)
            continue
        
        delete_all = False
        to_delete = set()
        for opt in selected_options:
            fields = options.get_fields(opt, metadata)
            if fields is None:
                delete_all = True
                break
            to_delete.update(fields)

        if delete_all:
            exiftool.delete_metadata(path, all=True)
            print(f"Deleted all metadata from: {path}")
            return True
        else:
            if not to_delete:
                print(f"No matching tags to delete for {path}")
                continue
            exiftool.delete_metadata(path, all=False, properties=list(to_delete))
            print(f"Deleted {len(to_delete)} tags from: {path}")
            return True