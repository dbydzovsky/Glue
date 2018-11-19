import argparse

from modules import module
from tools.ansible.run.ansiblePlaybookRun import AnsiblePlaybookRun
from tools.ansible.runner.nativeAnsibleRunner import NativeAnsibleRunner


class DeployModule(module.Module):
    def command(self):
        return "deploy"

    def help(self):
        return "Deploys an application."

    def setParser(self, parser: argparse.ArgumentParser):
        parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

    def start(self, args):
        print(args.integers[0])
        run = AnsiblePlaybookRun()
        runner = NativeAnsibleRunner()

        runner.execute(run)