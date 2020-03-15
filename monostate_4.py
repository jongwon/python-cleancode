"""Clean Code in Python - Chapter 9: Common Design Patterns

> Monostate Pattern: Borg
"""
from log import logger


class SharedAllMixin:
    def __init__(self, *args, **kwargs):
        try:
            self.__class__._attributes
        except AttributeError:
            self.__class__._attributes = {}

        self.__dict__ = self.__class__._attributes
        super().__init__(*args, **kwargs)


class BaseFetcher:
    def __init__(self, source):
        self.source = source


class TagFetcher(SharedAllMixin, BaseFetcher):
    def pull(self):
        logger.info("pulling from tag %s", self.source)
        return f"Tag = {self.source}"


class BranchFetcher(SharedAllMixin, BaseFetcher):
    def pull(self):
        logger.info("pulling from branch %s", self.source)
        return f"Branch = {self.source}"



if __name__ == '__main__':
    t1 = TagFetcher(0.1)
    b1 = BranchFetcher(0.2)
    b2 = BranchFetcher(0.3)

    print(t1.pull())
    print(b1.pull())
