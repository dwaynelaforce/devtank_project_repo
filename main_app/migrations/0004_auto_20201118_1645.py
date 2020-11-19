# Generated by Django 2.2.4 on 2020-11-19 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0004_auto_20201118_1849'),
        ('main_app', '0003_auto_20201118_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('messager', models.ManyToManyField(related_name='messaged_by', to='login_reg_app.Dev')),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='started_by', to='login_reg_app.Client')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='times_viewed',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('convo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.Chat')),
                ('replier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='login_reg_app.Dev')),
            ],
        ),
    ]