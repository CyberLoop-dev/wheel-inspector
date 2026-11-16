#!/usr/bin/env python3
"""Inspect Python wheel metadata without installing or executing the package."""
import argparse
import configparser
import json
import sys
import zipfile
from email.parser import Parser
from pathlib import Path


def inspect_wheel(path):
    path = Path(path)
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        metadata_files = [n for n in names if n.endswith(".dist-info/METADATA")]
        if len(metadata_files) != 1:
            raise ValueError("expected exactly one .dist-info/METADATA file")
        prefix = metadata_files[0].rsplit("/", 1)[0]
        metadata = Parser().parsestr(archive.read(metadata_files[0]).decode("utf-8", "replace"))
        wheel_path = prefix + "/WHEEL"
        record_path = prefix + "/RECORD"
        entry_path = prefix + "/entry_points.txt"
        scripts = {}
        if entry_path in names:
            config = configparser.ConfigParser()
            config.read_string(archive.read(entry_path).decode("utf-8", "replace"))
            if config.has_section("console_scripts"):
                scripts = dict(config.items("console_scripts"))
        return {
            "file": path.name,
            "name": metadata.get("Name"),
            "version": metadata.get("Version"),
            "summary": metadata.get("Summary", ""),
            "requires_python": metadata.get("Requires-Python"),
            "requires_dist": metadata.get_all("Requires-Dist", []),
            "console_scripts": scripts,
            "dist_info": {
                "metadata": True,
                "wheel": wheel_path in names,
                "record": record_path in names
            },
            "file_count": len(names),
            "files": names
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wheel", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--list-files", action="store_true")
    args = parser.parse_args()
    try:
        report = inspect_wheel(args.wheel)
    except (OSError, zipfile.BadZipFile, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"{report['name']} {report['version']}")
        print(report["summary"] or "No summary supplied.")
        print(f"Requires Python: {report['requires_python'] or 'not declared'}")
        print("Dependencies:")
        for requirement in report["requires_dist"]:
            print(f"  - {requirement}")
        print("Console scripts:")
        for name, target in report["console_scripts"].items():
            print(f"  - {name} = {target}")
        print("dist-info:", ", ".join(k for k, v in report["dist_info"].items() if v))
        if args.list_files:
            print("Files:")
            for item in report["files"]:
                print(f"  {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
