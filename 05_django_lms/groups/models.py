import datetime

from django.db import models

from core.models import BaseModel
from teachers.models import Teacher


class Group(BaseModel):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    headman = models.OneToOneField(
        'students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group'
    )
    teachers = models.ManyToManyField(to=Teacher, blank=True, related_name='groups')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'Group name: {self.name}'

    @classmethod
    def generate_fake_data(cls):
        for name in 'Python', 'Java', 'HTML+CSS', 'C#', 'C/C++', 'DevOPS', 'PM', 'QA':
            cls.objects.create(name=name)
