# Generated by Django 4.2.4 on 2023-09-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_delete_donorresponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('bloodType', models.CharField(max_length=5)),
                ('weight', models.FloatField()),
                ('donorHistory', models.CharField(max_length=3)),
                ('difficulty', models.CharField(max_length=3)),
                ('donated', models.CharField(max_length=3)),
                ('allergies', models.CharField(max_length=3)),
                ('alcohol', models.CharField(max_length=3)),
                ('jail', models.CharField(max_length=3)),
                ('surgery', models.CharField(max_length=3)),
                ('diseased', models.CharField(max_length=3)),
                ('hivaids', models.CharField(max_length=3)),
                ('pregnant', models.CharField(blank=True, max_length=3, null=True)),
                ('child', models.CharField(blank=True, max_length=3, null=True)),
                ('feelgood', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
    ]
