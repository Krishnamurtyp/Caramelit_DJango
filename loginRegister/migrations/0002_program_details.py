# Generated by Django 3.0.6 on 2020-06-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegister', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='program_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=100)),
            ],
        ),
    ]
