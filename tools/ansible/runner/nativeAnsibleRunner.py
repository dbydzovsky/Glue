from tools.ansible.run.iAnsibleRun import IAnsibleRun
from tools.ansible.runner.iAnsibleRunner import IAnsibleRunner
import subprocess

class NativeAnsibleRunner(IAnsibleRunner):
    def execute(self, run: IAnsibleRun):
        print(run.command())
        subprocess.call([run.command()])