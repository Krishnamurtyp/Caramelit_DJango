# Generated by Django 2.2.12 on 2020-06-18 08:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('date_of_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('course_description', models.TextField(default='')),
                ('course_difficulty', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course_category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('date_of_creation', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Course_subcategory',
            fields=[
                ('subcategory_id', models.AutoField(primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(max_length=100)),
                ('date_of_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course_category')),
            ],
        ),
        migrations.CreateModel(
            name='Course_resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourse_name', models.CharField(max_length=100)),
                ('resourse_link', models.CharField(max_length=100)),
                ('resourse_length', models.CharField(max_length=10)),
                ('date_of_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course_subcategory'),
        ),
    ]
