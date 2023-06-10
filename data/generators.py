import random
from faker import Faker


# Класс для генерации рандомных тестовых данных
class GeneratedData:

    def generate_random_first_name():
        fake = Faker('ru_RU')
        first_name = fake.first_name_female()
        return first_name

    def generate_random_last_name():
        fake = Faker('ru_RU')
        last_name = fake.last_name_female()
        return last_name

    def generate_random_street_address():
        fake = Faker('ru_RU')
        street_address = f"{fake.street_name()} {str(random.randint(111, 999))}"
        return street_address

    def generate_random_phone_number():
        phone_number = f"+7{str(random.randint(900, 999))}{str(random.randint(1111111, 9999999))}"
        return phone_number
