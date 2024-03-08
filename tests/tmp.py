from typing import Any


class Info:
    def __init__(self, pppp="", llll=""):
        self.pppp = pppp
        self.llll = llll


class Base:
    @staticmethod
    def makeRegistrar():
        registry: dict[str, (Any, Info)] = {}

        def registerParam(option: Info):
            def registrar(func):
                print("ppp")
                registry[func.fget.__name__] = (func, option)
                return func  # normally a decorator returns a wrapped function,
                # but here we return func unmodified, after registering it

            return registrar

        registerParam.all = registry
        return registerParam

    reg = makeRegistrar()

    def widget(self):
        registry: dict[str, (Any, Info)] = self.reg.all
        print(registry)
        for info in registry:
            print(registry[info][0].fset.__name__)
            print(registry[info][1].pppp)


class Child(Base):
    @property
    def name(self):
        return "child"

    @Base.reg(Info(pppp="my name is child"))
    @name.setter
    def name(self, value):
        print(f"{value} is")


if __name__ == "__main__":
    child = Child()
    child.name = "lala"
    child.widget()
