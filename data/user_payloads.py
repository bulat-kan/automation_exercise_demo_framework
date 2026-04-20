from faker import Faker
from uuid import uuid4


def new_user_payload() -> dict:
    fake = Faker()
    f_name = fake.first_name()
    l_name = fake.last_name()
    name = f"{f_name} {l_name}"
    email = f"test_{uuid4().hex[:8]}@mail.com"
    password = "Password@1"
    title = "Mr"
    payload = {
        "name": name,
        "email": email,
        "password": password,
        "title": title,
        "birth_date": 1,
        "birth_month": 1,
        "birth_year": 2001,
        "firstname": f_name,
        "lastname": l_name,
        "company": "",
        "address1": "123 Main st",
        "address2": "",
        "country": "United States",
        "zipcode": 31321,
        "state": "Florida",
        "city": "Miami",
        "mobile_number": "1234567890"
    }
    return payload
