from faker import Faker

from .models import User

fkr = Faker()

FIRST_NAME = 0
SECOND_NAME = 1


def create_users(users_amount=55):
    for _ in range(users_amount):
        name_parts = fkr.name().split(" ")
        user = User.objects.create(
            first_name=name_parts[FIRST_NAME],
            last_name=name_parts[SECOND_NAME]
        )
        user.save()
        print(f"{user} was created")


if __name__ == '__main__':
    print("Start filling DB with data:\n")
    create_users()
