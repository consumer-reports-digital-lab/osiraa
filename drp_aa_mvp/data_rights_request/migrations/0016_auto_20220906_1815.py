# Generated by Django 3.2.12 on 2022-09-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_rights_request', '0015_auto_20220906_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarightsstatus',
            name='reason',
            field=models.TextField(blank=True, choices=[('need_user_verification', 'need_user_verification'), ('suspected_fraud', 'suspected_fraud'), ('insufficient_verification', 'insufficient_verification'), ('no_match', 'no_match'), ('claim_not_covered', 'claim_not_covered'), ('outside_jurisdiction', 'outside_jurisdiction'), ('other', 'other'), ('', '')], default='', max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='datarightsstatus',
            name='user_verification_url',
            field=models.URLField(blank=True, default='', max_length=127, null=True),
        ),
    ]
