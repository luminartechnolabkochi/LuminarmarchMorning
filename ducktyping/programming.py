class Pycharm:
    def compile(self):
        print("compile using pycharm")
    def execute(self):
        print("execute")

class Vscode:
    def compile(self):
        print("compile using vscode")

    def execute(self):
        print("vscode execute")


class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()

p=Programmer()
pyc=Vscode()
p.coding(pyc)