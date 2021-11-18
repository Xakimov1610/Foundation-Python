class Odam:
    def __init__(self, name):
        self.name = name

    def hello_name(self):
        return "Salom " + self.name


o = Odam("Laziz")
print(o.hello_name())

