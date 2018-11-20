import argparse

from modules import module
import yaml

class DeployModule(module.Module):
    def command(self):
        return "deploy"

    def help(self):
        return "Deploys applications."

    def setParser(self, parser: argparse.ArgumentParser):
        parser.add_argument('-f', type=argparse.FileType('r'), nargs="?", default="Gluefile.yaml", help='A gluefile.yaml to be deployed.')

    def start(self, args):
        data = loadData(args)
        checkStructure(data)
        print(data)



def checkStructure(data):
    print("checking structure.")
    pass



def loadData(args):
    gluefile = args.f

    print("loading data.")
    try:
        y = yaml.load(gluefile)
        return y
    except yaml.YAMLError as exc:
        print(exc)
        exit(1)
    finally:
        gluefile.close()