# Generated by Django 4.2.7 on 2023-12-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_versions_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.IntegerField(max_length=150, unique=True, verbose_name='статус товара на складе')),
            ],
            options={
                'verbose_name': 'номер версии',
                'verbose_name_plural': 'номера версии',
            },
        ),
        migrations.AlterField(
            model_name='statusproduct',
            name='status_name',
            field=models.CharField(max_length=150, unique=True, verbose_name='статус товара на складе'),
        ),
    ]
