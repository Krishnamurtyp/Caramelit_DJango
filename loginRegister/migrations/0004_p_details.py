# Generated by Django 3.0.6 on 2020-06-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegister', '0003_auto_20200611_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='p_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_details', models.CharField(max_length=200)),
            ],
        ),
    ]
