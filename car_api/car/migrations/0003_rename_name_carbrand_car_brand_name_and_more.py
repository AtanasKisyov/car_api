# Generated by Django 4.0.3 on 2022-04-09 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_carbrand_deleted_at_carbrand_is_deleted_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carbrand',
            old_name='name',
            new_name='car_brand_name',
        ),
        migrations.RenameField(
            model_name='carmodel',
            old_name='name',
            new_name='car_model_name',
        ),
    ]
