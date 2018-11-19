import abc


class IAnsibleRun(abc.ABC):
    @abc.abstractmethod
    def command(self):
        pass

