# Generated by Django 5.0 on 2024-10-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mat_no',
            field=models.CharField(),
        ),
    ]
