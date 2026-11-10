#!/usr/bin/env python3
"""Read and verify pinned originals. Standard library only; never executes upstream code."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

SKILL = Path(__file__).resolve().parents[1]


def digest(root):
    rows = []
    for path in sorted(Path(root).rglob('*')):
        if path.is_symlink():
            raise ValueError('Unexpected symlink: ' + str(path))
        if path.is_file():
            rows.append([path.relative_to(root).as_posix(),
                         hashlib.sha256(path.read_bytes()).hexdigest(),
                         bool(path.stat().st_mode & 0o111)])
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()


def catalog():
    return json.loads((SKILL / 'sources.lock.json').read_text())


def library_root():
    settings = SKILL / 'installation.json'
    if not settings.is_file():
        raise ValueError('Not installed. Run install.py first.')
    return (SKILL / json.loads(settings.read_text())['library']).resolve()


def verify(root, entry):
    if root.is_symlink():
        raise ValueError('Unexpected release symlink: ' + str(root))
    for rel in entry['entrypoints'] + entry['license_paths']:
        if not (root / rel).is_file():
            raise ValueError('Missing entrypoint/license: ' + rel)
    if digest(root) != entry['tree_sha256']:
        raise ValueError('Content hash mismatch: ' + str(root))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['status', 'resolve', 'check-updates'])
    parser.add_argument('id', nargs='?')
    args = parser.parse_args()
    entries = catalog()
    if args.id and args.id not in entries:
        parser.error('Unknown source ID')
    selected = {args.id: entries[args.id]} if args.id else entries
    if args.action == 'resolve' and not args.id:
        parser.error('resolve requires a source ID')
    root = library_root()
    results = {}
    for key, entry in selected.items():
        release = root / key / entry['commit']
        verify(release, entry)
        result = {'commit': entry['commit'], 'verified': True,
                  'source': entry['source'], 'path': str(release),
                  'entrypoints': [str(release / p) for p in entry['entrypoints']]}
        if args.action == 'check-updates':
            proc = subprocess.run(['git', '-c', 'core.hooksPath=/dev/null',
                                   'ls-remote', entry['source'], 'HEAD'],
                                  capture_output=True, text=True, timeout=90)
            if proc.returncode:
                raise ValueError('Cannot check upstream: ' + key)
            latest = proc.stdout.split()[0]
            result.update(latest=latest, update_available=latest != entry['commit'])
        results[key] = result
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
