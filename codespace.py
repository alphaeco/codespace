#!/usr/bin/python3

import os                                # dependency for codebase
from codespace.setup import check_setup  # for codebase database check

if __name__ == '__main__':

    # check for codespace setup
    #  - create if if not
    setup = check_setup()

    # if setup check has failed
    if not setup:
        print("Error: error initiating database")
        sys.exit()

    # if setup is successful -> load config file
    if setup:
        from codespace.config import load_config
        from codespace.base import CodeSpace

        config = load_config()

        codeSpace = CodeSpace(config)
        codeSpace.run()

