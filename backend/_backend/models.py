from tortoise import fields
from tortoise.models import Model

from _backend.utils.birthday_calculator import calculate_time_until_birthday

class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    username = fields.CharField(max_length=50, unique=True)
    birth_date = fields.DateField()

    class Meta:
        table = "users"

    def time_until_birthday(self):
        return calculate_time_until_birthday(self.birth_date)
