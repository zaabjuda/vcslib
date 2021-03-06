# -*- coding: utf-8 -*-

VERSION = (0, 5, 2, 'dev')

__version__ = '.'.join((str(each) for each in VERSION[:4]))

__all__ = [
    'get_version', 'get_repo', 'get_backend',
    'VCSError', 'RepositoryError', 'ChangesetError'
]

import sys
from managevcs.backends import get_repo, get_backend
from managevcs.exceptions import VCSError, RepositoryError, ChangesetError


def get_version():
    """
    Returns shorter version (digit parts only) as string.
    """
    return '.'.join((str(each) for each in VERSION[:3]))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    from managevcs.cli import ExecutionManager
    manager = ExecutionManager(argv)
    manager.execute()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
