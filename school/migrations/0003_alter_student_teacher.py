# Generated by Django 4.0.1 on 2022-01-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_student_group_alter_student_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.Teacher'),
        ),
    ]
