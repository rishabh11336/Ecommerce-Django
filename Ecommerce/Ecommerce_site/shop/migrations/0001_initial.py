# Generated by Django 4.1 on 2022-08-21 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=10)),
                ('description', models.CharField(default='', max_length=200)),
                ('fdescription', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('image', models.ImageField(upload_to='static/Shop/')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
