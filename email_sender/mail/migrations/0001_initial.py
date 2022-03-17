# Generated by Django 4.0.3 on 2022-03-09 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=81)),
                ('message', models.TextField()),
                ('from_mail', models.EmailField(max_length=254)),
                ('to_mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.tomail')),
            ],
        ),
    ]
