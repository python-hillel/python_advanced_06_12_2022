from random import randint

from django.db import models

from core.models import PersonModel


class Teacher(PersonModel):
    salary = models.PositiveIntegerField(default=10_000)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name} (${self.salary})'

    @classmethod
    def _generate(cls):
        teacher = super()._generate()
        teacher.salary = randint(10_000, 100_000)
        teacher.save()
