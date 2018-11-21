import argparse
import subprocess
from modules import module
import yaml
import os

class DeployModule(module.Module):
    def command(self):
        return "deploy"

    def help(self):
        return "Deploys applications."

    def setParser(self, parser: argparse.ArgumentParser):
        parser.add_argument('gluefile', type=argparse.FileType('r'), nargs="?", default="Gluefile.yaml", help='A gluefile.yaml to be deployed.')
        parser.add_argument('-deployables', type=argparse.FileType('r'), nargs="*", required=True)

    def start(self, args):
        glue = loadData(args)
        checkStructure(glue)
        print(glue)

        roles = loadDeployables(args.deployables)
        checkRoles(roles)
        print(roles)

        for machine in glue["machines"]:
            deployMachineRoles(machine, roles)


def deployMachineRoles(machine, roles):
    for want in machine["roles"]:
        role = next(obj for obj in roles if obj["name"]==want)
        deployMachineRole(machine, role)

def deployMachineRole(machine, role):
    # subprocess.call(['C:\\Temp\\a b c\\Notepad.exe', 'C:\\test.txt'])
    # cwd =
    # print(cwd)
    subprocess.call(["/bin/bash","-c",os.getcwd() +"/" +role["deployable"]["bash"]["path"]])

def loadData(args):
    gluefile = args.gluefile
    return parseYml(gluefile)

def checkStructure(data):
    print("checking structure.")
    pass





def loadDeployables(deployables):
    res = []
    for deployable in deployables:
        res.append(parseYml(deployable))
    return res

def checkRoles(roles):
    pass






def parseYml(openedFile):
    print("loading data.")
    try:
        y = yaml.load(openedFile)
        return y
    except yaml.YAMLError as exc:
        print(exc)
        exit(1)
    finally:
        openedFile.close()