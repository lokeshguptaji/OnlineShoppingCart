# Generated by Django 3.0 on 2020-04-30 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
