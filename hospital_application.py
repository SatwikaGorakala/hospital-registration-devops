
class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease


class Hospital:
    def __init__(self):
        self.patients = []

    def register(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        disease = input("Enter disease: ")

        self.patients.append(Patient(name, age, disease))
        print("Patient registered successfully!")

    def view(self):
        for p in self.patients:
            print(p.name, p.age, p.disease)


if __name__ == "__main__":
    hospital = Hospital()

    while True:
        print("\n1. Register Patient")
        print("2. View Patients")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            hospital.register()
        elif choice == "2":
            hospital.view()
        elif choice == "3":
            break
        else:
            print("Invalid choice")