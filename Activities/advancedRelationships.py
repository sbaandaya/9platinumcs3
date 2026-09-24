class ElectronicDevice:
    def __init__(self, Hardware, Software):
        self.Hardware = Hardware
        self.Software = Software
    def display_Hardware(self):
        print("Original:", self.Hardware)
    def display_Software(self):
        print("Original:", self.Software)
class Computer(ElectronicDevice):
    def __init__(self, Hardware, Software, Model, Size, motherboard):
        super().__init__(Hardware, Software)
        self.Model = Model
        self.Size = Size
        self.motherboard = motherboard
    def display_Model(self):
        print("Extra:", self.Model)
    def display_Size(self):
        print("Extra:", self.Size)
    def display_Motherboard(self):
        print("A Computer", self.motherboard, "a Motherboard")

Computer1 = Computer("Has", "Has", "old model", "Large", "has")
Computer1.display_Hardware()
Computer1.display_Software()
Computer1.display_Model()
Computer1.display_Size()
Computer1.display_Motherboard()