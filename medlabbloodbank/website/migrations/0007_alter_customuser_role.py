# Generated by Django 4.2.4 on 2023-09-08 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_donor_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'DONOR'), (2, 'HOSPITAL'), (3, 'STAFF'), (4, 'REGISTEREDDONOR')], default='1', null=True),
        ),
    ]
