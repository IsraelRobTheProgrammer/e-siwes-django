# Generated by Django 5.0 on 2024-10-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_student_mat_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mat_no',
            field=models.CharField(max_length=9),
        ),
    ]