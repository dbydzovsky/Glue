import abc
import argparse

class Module(abc.ABC):
    @abc.abstractmethod
    def command(self):
        pass

    @abc.abstractmethod
    def help(self):
        pass

    @abc.abstractmethod
    def setParser(self, parser: argparse.ArgumentParser):
        pass

    @abc.abstractmethod
    def start(self, args):
        pass