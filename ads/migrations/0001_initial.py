# Generated by Django 2.2.1 on 2019-05-21 18:41

import ads.enums
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_text', models.TextField(max_length=200)),
                ('status', models.CharField(choices=[('E', 'Expired'), ('P', 'Pending'), ('R', 'Rejected'), ('A', 'Active')], default=ads.enums.AdStatusEnum('Pending'), max_length=10)),
                ('creation_date', models.DateField()),
                ('ad_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Seller')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
            ],
        ),
    ]
