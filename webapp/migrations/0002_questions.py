# Generated by Django 3.0.4 on 2020-03-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('choice_A', models.CharField(max_length=50)),
                ('choice_B', models.CharField(max_length=50)),
                ('choice_C', models.CharField(max_length=50)),
                ('correct', models.CharField(max_length=50)),
            ],
        ),
    ]
