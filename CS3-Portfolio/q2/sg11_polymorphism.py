class Patient:
    def __init__(self, name, bill_amount):
        self._name: str = name
        self._bill_amount: float = bill_amount

    @property
    def get_name(self):
        return self._name

    @name.setter
    def set_name(self, name):
        self._name = name
        return self._name

    @property
    def get_bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount
        return self._bill_amount

    def calculate_bill():
        return self._bill_amount

    def display_patient_info(self):
        print(f"Patient Name: {self._name}")
        print(f"Bill Amount: ${self._bill_amount:.2f}")