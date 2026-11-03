"""Unpack the Zenodo RAR signal archives into data/extracted/Dataset_{A,B,C}/.

Usage: python analysis/extract.py data/raw data/extracted
"""
import glob
import os
import sys

import libarchive

raw_dir, out_dir = sys.argv[1], sys.argv[2]
for path in sorted(glob.glob(os.path.join(raw_dir, "*.rar"))):
    name = "Dataset_" + os.path.splitext(path)[0][-1]
    target = os.path.join(out_dir, name)
    os.makedirs(target, exist_ok=True)
    count = 0
    with libarchive.file_reader(path) as archive:
        for entry in archive:
            if entry.isdir:
                continue
            with open(os.path.join(target, os.path.basename(entry.pathname)), "wb") as fh:
                for block in entry.get_blocks():
                    fh.write(block)
            count += 1
    print(f"{name}: {count} files")
