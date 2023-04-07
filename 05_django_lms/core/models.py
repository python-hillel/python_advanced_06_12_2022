import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from faker import Faker

from core.validators import ValidateEmailDomain


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonModel(BaseModel):
    domain = ('gmail.com', 'yahoo.com', 'test.com')
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='first_name')
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='last_name')
    birthday = models.DateField(default=datetime.date.today, blank=True)  # default='2003-01-01'
    city = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(validators=[ValidateEmailDomain(*domain)])

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    class Meta:
        abstract = True

    @classmethod
    def _generate(cls):
        f = Faker()

        first_name = f.first_name()
        last_name = f.last_name()
        obj = cls(
            first_name=first_name,
            last_name=last_name,
            birthday=f.date_between(start_date='-65y', end_date='-18y'),
            email=f'{first_name}.{last_name}@{f.random.choice(cls.domain)}',
            city=f.city()
        )
        obj.save()

        return obj

    @classmethod
    def generator(cls, cnt):
        for _ in range(cnt):
            cls._generate()
