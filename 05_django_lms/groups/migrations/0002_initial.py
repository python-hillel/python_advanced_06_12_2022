# Generated by Django 4.1.6 on 2023-02-10 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='headman',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headman_group', to='students.student'),
        ),
    ]