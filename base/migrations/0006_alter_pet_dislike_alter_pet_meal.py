# Generated by Django 4.0.1 on 2022-02-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_pet_add_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='dislike',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='meal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]