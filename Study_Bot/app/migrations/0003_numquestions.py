# Generated by Django 2.0.10 on 2019-12-21 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191220_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_questions', models.IntegerField(max_length=1)),
            ],
        ),
    ]
