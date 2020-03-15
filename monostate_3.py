"""Clean Code in Python - Chapter 9: Common Design Patterns

> Monostate Pattern: BORG
"""
from log import logger


class BaseFetcher:
    def __init__(self, source):
        self.source = source


class TagFetcher(BaseFetcher):
    _attributes = {}

    def __init__(self, source):
        self.__dict__ = self.__class__._attributes
        super().__init__(source)

    def pull(self):
        logger.info("pulling from tag %s", self.source)
        print(self.__class__._attributes)
        return f"Tag = {self.source}"


class BranchFetcher(BaseFetcher):
    _attributes = {}

    def __init__(self, source):
        self.__dict__ = self.__class__._attributes
        super().__init__(source)

    def pull(self):
        logger.info("pulling from branch %s", self.source)
        return f"Branch = {self.source}"


if __name__ == '__main__':
    t1 = TagFetcher(0.1)
    print(t1.pull())

    b1 = BranchFetcher(0.2)
    b2 = BranchFetcher(0.3)

    t1 = TagFetcher(0.4)

    print(t1.pull())
    print(b1.pull())
