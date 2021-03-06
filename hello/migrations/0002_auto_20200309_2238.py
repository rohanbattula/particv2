# Generated by Django 3.1 on 2020-03-09 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='dateTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='distance',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='entryFee',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='guysAllowed',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
