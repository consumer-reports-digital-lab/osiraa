# Generated by Django 3.2.12 on 2022-09-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_identity', '0005_alter_identityuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='identityuser',
            name='address_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='identityuser',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='identityuser',
            name='phone_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='identityuser',
            name='power_of_attorney',
            field=models.BooleanField(default=False),
        ),
    ]
