# Generated by Django 3.2.5 on 2021-09-03 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]