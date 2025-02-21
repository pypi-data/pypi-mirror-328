import os
import argparse
import importlib.metadata
from phycat.PhycatSession import PhycatSession
from cliify.ui.prompt_toolkit import SplitConsole


args = None
parser = None
session = PhycatSession()

version = importlib.metadata.version("phycat")



banner_text =f"Phycat v{version}"

# Initialize the argument parser
def init_args():
    global parser
    parser = argparse.ArgumentParser("Tool to interact with replicant message broker")
    parser.add_argument('-c', '--connect', type=str, help='Stack Base Address', default=None)
    parser.add_argument('-s', '--server', type=str, help='Server Config', default=None)
    parser.add_argument('-l','--log-level', type=str, help='Log Level', default="info")



def main():
    global args
    global session
    global parser

    init_args()
    args = parser.parse_args()

    home_path = os.path.expanduser('~')
    app = SplitConsole(session, banner_text, os.path.join(home_path, '.phycat-history'), exitCallback=session.close)

    if args.connect:
        session.connect(args.connect)

    app.start()


if __name__ == '__main__':
   main()