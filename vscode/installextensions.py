#!/usr/bin/env python3

import itertools
import subprocess
import sys


def main():
    args = (("--install-extension", line.strip()) for line in sys.stdin)
    args = itertools.chain.from_iterable(args)
    subprocess.run(["code", *args])


if __name__ == "__main__":
    main()
