# Generated by Django 2.2.4 on 2020-11-20 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0004_auto_20201118_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dev',
            name='profile_pic',
            field=models.ImageField(default='/media/default.png', upload_to='media'),
        ),
    ]