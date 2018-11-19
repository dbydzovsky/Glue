# cli.py
import argparse
import sys

from modules.deploy.deployModule import DeployModule

modules = [
    DeployModule()
]

mainParser = argparse.ArgumentParser(description='Start an application.')
mainSubparsers = mainParser.add_subparsers(help='sub-command help')

for module in modules:
    parser = mainSubparsers.add_parser(module.command(), help=module.help())
    module.setParser(parser)

parsedArgs = mainParser.parse_args()

moduleName = sys.argv[1]
module = next(obj for obj in modules if obj.command()==moduleName)
module.start(parsedArgs)