# Generated by Django 4.1.2 on 2022-10-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_pet_person_pets'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=21),
            preserve_default=False,
        ),
    ]