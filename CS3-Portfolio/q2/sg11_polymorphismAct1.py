## Create a base class called Patient with attributes for name and bill amount. Implement methods to calculate the bill amount and display the patient type. Then, create two subclasses: SeniorPatient and PhilHealthPatient, which inherit from the Patient class. Override the calculate_bill method in each subclass to apply different discount rates based on the patient type. Finally, demonstrate polymorphism by creating instances of each patient type and calling their respective methods.

class Patient:

    def __init__(self, name, bill_amount): # Initializes the Patient class with name and bill amount

        self._name: str = name
        self._bill_amount: float = bill_amount

    @property
    def get_name(self): # Returns the name of the patient

        return self._name

    @get_name.setter
    def set_name(self, name): # Sets the name of the patient

        self._name = name
        return self._name

    @property
    def get_bill_amount(self): # Returns the bill amount of the patient

        return self._bill_amount

    @get_bill_amount.setter
    def set_bill_amount(self, bill_amount): # Sets the bill amount of the patient

        self._bill_amount = bill_amount
        return self._bill_amount

    def calculate_bill(self): # Calculates the bill amount for regular patients (no discount applied)

        discount = 1.0  # No discount for regular patients
        self._bill_amount *= discount
        return self._bill_amount

    def display_patient_type(self): # Displays the patient type for regular patients

        patientType = "Regular Patient"
        print(f"Patient Type: {patientType}")

class SeniorPatient(Patient):

    def __init__(self, name, bill_amount): # Initializes the SeniorPatient class with name and bill amount, inheriting from Patient

        super().__init__(name, bill_amount)

    def calculate_bill(self): # Calculates the bill amount for senior patients with a 20% discount applied

        discount = 0.8  # 20% discount for senior patients
        self._bill_amount *= discount
        return self._bill_amount

    def display_patient_type(self): # Displays the patient type for senior patients

        patientType = "Senior Citizen"
        print(f"Patient Type: {patientType}")

class PhilHealthPatient(Patient):

    def __init__(self, name, bill_amount): # Initializes the PhilHealthPatient class with name and bill amount, inheriting from Patient

        super().__init__(name, bill_amount)

    def calculate_bill(self): # Calculates the bill amount for PhilHealth patients with a 15% discount applied

        discount = 0.85  # 15% discount for PhilHealth patients
        self._bill_amount *= discount
        return self._bill_amount

    def display_patient_type(self): # Displays the patient type for PhilHealth patients

        patientType = "PhilHealth Member"
        print(f"Patient Type: {patientType}")

## Demonstration of polymorphism

def main():

    # Create instances of each patient type

    bill = float(15000.00)  # Example bill amount for test patients
    regular_patient = Patient("Juan Dela Cruz", bill)
    senior_patient = SeniorPatient("Maria Santos", bill)
    philhealth_patient = PhilHealthPatient("Pedro Reyes", bill)

    # List of patients

    patients = [
        regular_patient, 
        senior_patient, 
        philhealth_patient
        ]

    # Calculate and display bill amounts and patient types

    print("Hospital Billing System")
    print("-" * 23)
    for patient in patients:
        print(f"Patient Name: {patient.get_name}")
        patient.display_patient_type()
        print(f"Original Bill: ₱{patient.get_bill_amount:,.2f}")
        final_bill = patient.calculate_bill()
        print(f"Final Bill: ₱{final_bill:,.2f}")
        print("")

main()