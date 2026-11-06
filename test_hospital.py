from hospital_application import Patient, Hospital


def test_patient_creation():
    patient = Patient("Satwika", 21, "Fever")

    assert patient.name == "Satwika"
    assert patient.age == 21
    assert patient.disease == "Fever"


def test_hospital_initially_empty():
    hospital = Hospital()

    assert len(hospital.patients) == 0
