class Notebook:
    def __init__(self):
        self.firmasi = "HP"
        self.model = "dw-15"
        self.cpu = "core i3 10100"
        self.ddr = 4
        self.price = 500

    def laptop_info(self):
        print("Firma:\t", self.firmasi)
        print("Model:\t", self.model)
        print("CPU:\t", self.cpu)
        print("DDR:\t", self.ddr)
        print("Price:\t", self.price, "$")


one = Notebook()
one.laptop_info()