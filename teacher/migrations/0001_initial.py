# Generated by Django 2.2 on 2021-08-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('salary', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('feedback', models.TextField()),
            ],
        ),
    ]