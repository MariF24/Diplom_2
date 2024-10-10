import faker

def get_registration_user():
    fake = faker.Faker()
    email = fake.email()
    name = fake.name()
    password = fake.password()

    return email, name, password

def get_registration_user_no_password():
    fake = faker.Faker()
    email_double = fake.email()
    name_double = fake.name()

    return email_double, name_double