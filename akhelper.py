#!/usr/bin/env python3

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    import sys
    import util.early_logs
    import util.unfuck_https_proxy
    import Arknights.configure_launcher
    import automator.launcher
    sys.exit(automator.launcher.main(sys.argv))
