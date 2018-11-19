from tools.ansible.run.iAnsibleRun import IAnsibleRun


class AnsiblePlaybookRun(IAnsibleRun):
    __command__: str = "ansible-playbook"
    def command(self):
        return self.__command__
