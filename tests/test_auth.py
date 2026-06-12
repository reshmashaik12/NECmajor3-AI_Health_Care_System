from utils.auth import (
    register_doctor,
    register_patient,
    login_doctor,
    login_patient
)


def test_patient_auth():

    email = "test@gmail.com"

    try:
        register_patient(
            "Test User",
            email,
            "1234",
            25,
            "Male",
            "9999999999",
            "Test Address",
            "O+"
        )
    except:
        pass

    user = login_patient(email, "1234")

    assert user is not None
    print("Auth Test Passed")


def test_doctor_auth():

    email = "doctor_test@gmail.com"

    try:
        register_doctor(
            "Test Doctor",
            email,
            "1234",
            "General Medicine",
            3,
            "8888888888"
        )
    except:
        pass

    user = login_doctor(email, "1234")

    assert user is not None
    print("Doctor Auth Test Passed")


if __name__ == "__main__":
    test_patient_auth()
    test_doctor_auth()
