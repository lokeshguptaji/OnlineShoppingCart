# Generated by Django 3.0 on 2020-05-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200430_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
