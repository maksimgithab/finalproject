# Generated by Django 5.0.2 on 2024-03-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=10)),
            ],
        ),
    ]
