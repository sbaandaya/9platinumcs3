class Patient:
  def __init__(self, name, bill_amount):
    self.name = name
    self.bill_amount = bill_amount
  def get_name(self):
    return self.name
  def set_name(self):
    pass
  def get_bill_amount(self):
    return self.bill_amount
  def set_bill_amount(self):
    print("Hospital Billing System")
    print("-----------------------")
    print("Patient Name:", self.name)
  def display_patient_type(self):
    print("Patient Type: Regular Patient")
    print("Original Bill:", self.bill_amount)
    print("Final Bill:", self.bill_amount)
    print("")

class SeniorPatient(Patient):
  def __init__(self, name, bill_amount):
    super().__init__(name, bill_amount)
  def calculate_bill(self):
    print("Patient Name:", self.name)
  def display_patient_type(self):
    print("Patient Type: Senior Citizen")
    print("Original Bill:", self.bill_amount)
    discount = self.bill_amount*0.2
    total = self.bill_amount - discount
    print("Final Bill:", total)
    print("")

class PhilHealthPatient(Patient):
  def __init__(self, name, bill_amount):
    super().__init__(name, bill_amount)
  def calculate_bill(self):
    print("Patient Name:", self.name)
  def display_patient_type(self):
    print("Patient Type: PhilHealth Member")
    print("Original Bill:", self.bill_amount)
    discount = self.bill_amount*0.15
    total = self.bill_amount - discount
    print("Final Bill:", total)
    print("")

patient1 = Patient("Me", 15000)
patient2 = SeniorPatient("I", 15000)
patient3 = PhilHealthPatient("You", 15000)
patient1.set_bill_amount()
patient1.display_patient_type()
patient2.calculate_bill()
patient2.display_patient_type()
patient3.calculate_bill()
patient3.display_patient_type()
