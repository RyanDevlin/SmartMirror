# Generated by Django 2.1.5 on 2019-03-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20190321_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Ticker',
            field=models.CharField(choices=[('0', 'APPL\n'), ('1', 'MSFT\n'), ('2', 'FB\n'), ('3', 'SPY\n'), ('4', 'TVIX\n'), ('5', 'GOOGL\n')], max_length=5),
        ),
    ]
