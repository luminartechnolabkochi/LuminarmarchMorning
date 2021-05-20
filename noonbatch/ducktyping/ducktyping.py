
class Vscode:

    def compile(self):
        print("compiling using vscode")

    def execute(self):
        print("execute using vscode")


    def debug(self):
        print("debug using vscode")


class Pycharm:

    def compile(self):
        print("compiling using Pycharm")

    def execute(self):
        print("execute using Pycharm")

    def debug(self):
        print("debug using Pycharm")


class Programmer:
    def coding(self,ide): #pyc
        ide.compile()#
        ide.execute()
        ide.debug()
devop=Programmer()
pyc=Pycharm()
devop.coding(pyc)

#functional programming map,filter reduce,lambada,listcompre
#variable length argument methods *args,**kwargs
#duck typing
#decorators
#customized Exception





