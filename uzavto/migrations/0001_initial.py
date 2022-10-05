# Generated by Django 4.1.1 on 2022-10-05 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('logo', models.ImageField(upload_to='model')),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('year', models.DateField()),
                ('image', models.ImageField(upload_to='cars')),
                ('expenses', models.FloatField()),
                ('color', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uzavto.model')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]