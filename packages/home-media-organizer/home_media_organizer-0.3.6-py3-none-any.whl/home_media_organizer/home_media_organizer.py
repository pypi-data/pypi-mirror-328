import argparse
import fnmatch
import os
import sys
import threading
from queue import Queue
from typing import Any, Callable, Dict, Generator, List

import rich
from exiftool import ExifToolHelper  # type: ignore
from tqdm import tqdm  # type: ignore

from .media_file import date_func


def iter_files(
    args: argparse.Namespace, items: List[str] | None = None
) -> Generator[str, None, None]:
    def allowed_filetype(filename: str) -> bool:
        if args.file_types and not any(fnmatch.fnmatch(filename, x) for x in args.file_types):
            return False
        if os.path.splitext(filename)[-1] not in date_func:
            return False
        return True

    # if file is selected based on args.matches,, args.with_exif, args.without_exif
    def allowed_metadata(metadata: Dict) -> bool:
        for cond in args.without_exif or []:
            if "=" in cond:
                k, v = cond.split("=")
                if "*" in k:
                    raise ValueError(
                        f"Invalid condition {cond}: '*' is not allowed when key=value is specified."
                    )
                if k in metadata and metadata[k] == v:
                    return False
            elif "*" in cond:
                if any(fnmatch.fnmatch(x, cond) for x in metadata.keys()):
                    return False
            else:
                if cond in metadata:
                    return False
        match = True
        for cond in args.with_exif or []:
            if "=" in cond:
                k, v = cond.split("=")
                if "*" in k:
                    raise ValueError(
                        f"Invalid condition {cond}: '*' is not allowed when key=value is specified."
                    )
                if k not in metadata or metadata[k] != v:
                    match = False
            elif "*" in cond:
                if not any(fnmatch.fnmatch(x, cond) for x in metadata.keys()):
                    match = False
            else:
                if cond not in metadata:
                    match = False
        return match

    for item in items or args.items:
        # if item is an absolute path, use it directory
        # if item is an relative path, check current working directory first
        # if not found, check the search path
        if os.path.isabs(item):
            pass
        elif os.path.exists(item):
            item = os.path.abspath(item)
        elif args.search_paths:
            search_paths = (
                [args.search_paths] if isinstance(args.search_paths, str) else args.search_paths
            )
            for path in search_paths:
                if os.path.exists(os.path.join(path, item)):
                    item = os.path.abspath(os.path.join(path, item))
                    break
            else:
                if len(search_paths) == 1:
                    rich.print(
                        f"[red]{item} not found in current directory or {search_paths[0]}[/red]"
                    )
                else:
                    rich.print(
                        f"[red]{item} not found in current directory or any directory under {', '.join(search_paths)}[/red]"
                    )
                sys.exit(1)
        else:
            rich.print(f"[red]{item} not found in current directory[/red]")
            sys.exit(1)
        if os.path.isfile(item):
            if not allowed_filetype(item):
                continue
            if args.with_exif or args.without_exif:
                with ExifToolHelper() as e:
                    metadata = {
                        x: y
                        for x, y in e.get_metadata(os.path.abspath(item))[0].items()
                        if not x.startswith("File:")
                    }
                if not allowed_metadata(metadata):
                    continue
            yield item
        else:
            if not os.path.isdir(item):
                rich.print(f"[red]{item} is not a filename or directory[/red]")
                continue
            for root, _, files in os.walk(item):
                if args.with_exif or args.without_exif:
                    # get exif atll at the same time
                    qualified_files = [os.path.join(root, f) for f in files if allowed_filetype(f)]
                    if not qualified_files:
                        continue
                    with ExifToolHelper() as e:
                        all_metadata = e.get_metadata(files=qualified_files)
                        for qualified_file, metadata in zip(qualified_files, all_metadata):
                            if allowed_metadata(
                                {x: y for x, y in metadata.items() if not x.startswith("File:")}
                            ):
                                yield qualified_file
                else:
                    for f in files:
                        if allowed_filetype(f):
                            yield os.path.join(root, f)


class Worker(threading.Thread):
    def __init__(self: "Worker", queue: Queue[Any], task: Callable) -> None:
        threading.Thread.__init__(self)
        self.queue = queue
        self.task = task
        self.daemon = True

    def run(self: "Worker") -> None:
        while True:
            item = self.queue.get()
            if item is None:
                break
            self.task(item)
            self.queue.task_done()


def process_with_queue(args: argparse.Namespace, func: Callable) -> None:
    q: Queue[str] = Queue()
    # Create worker threads
    num_workers = args.jobs or 10
    for _ in range(num_workers):
        t = Worker(q, func)
        t.start()

    for item in (pbar := tqdm(iter_files(args))):
        pbar.set_description(f"Processing {os.path.basename(item)}")
        q.put(item)
    q.join()
