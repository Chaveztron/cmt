# Generated by Django 3.0.7 on 2020-07-21 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.TextField()),
                ('contry', models.TextField()),
                ('city', models.TextField()),
            ],
        ),
    ]