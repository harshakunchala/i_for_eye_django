# Generated by Django 3.0.6 on 2020-07-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iforeyepro', '0002_auto_20200726_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo_details',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]