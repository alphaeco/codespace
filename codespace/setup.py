import os
import sys

userpath = os.path.expanduser("~/.codebase")


def writeFirstConfig():
    return True





def check_setup():
    print("Checking for Codespace Config: {}".format(userpath))

    # create the config database is not existing
    if not os.path.exists(userpath):
        print("[+] creating codespace files...")

        try:
            os.makedirs(userpath)
        except IOError:
            print("[-] IOError, an error occured while creating database")
            return False

        # not put a blank config file in dir


    return True 
