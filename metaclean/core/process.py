import os
import sys
import concurrent.futures

from . import exiftool, options

def process_single_image(path, selected_options):
    try:
        metadata = list(exiftool.get_metadata(path).keys())
    except Exception as e:
        print(f"\033[31mFailed to read metadata for {path}: {e}\033[0m", file=sys.stderr)
        return 1

    delete_all = False
    to_delete = set()
    for opt in selected_options:
        fields = options.get_fields(opt, metadata)
        if fields is None:
            delete_all = True
            break
        to_delete.update(fields)

    if delete_all:
        result = exiftool.delete_metadata(path, all=True)
        if not result:
            print(f"Tried to delete all metadata from: {path}")
            return 1
        else:
            print(f"Deleted all metadata from: {path}")
            return 0
    else:
        if not to_delete:
            print(f"No matching tags to delete for {path}")
            return 0
        result = exiftool.delete_metadata(path, all=False, properties=list(to_delete))
        if not result:
            print(f"Tried to delete {len(to_delete)} tags from: {path}")
            return 1
        else:
            print(f"Deleted {len(to_delete)} tags from: {path}")
            return 0

def process_images(filenames, selected_options, is_cancelled):
    errors = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = {executor.submit(process_single_image, path, selected_options): path for path in filenames}
        
        for future in concurrent.futures.as_completed(futures):
            if is_cancelled():
                for f in futures:
                    if not f.done():
                        f.cancel()
                break
            
            try:
                errors += future.result()
            except concurrent.futures.CancelledError:
                pass
    return errors