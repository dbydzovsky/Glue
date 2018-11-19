import abc

from tools.ansible.run.iAnsibleRun import IAnsibleRun

class IAnsibleRunner(abc.ABC):
    @abc.abstractmethod
    def execute(self, x: IAnsibleRun):
        pass
