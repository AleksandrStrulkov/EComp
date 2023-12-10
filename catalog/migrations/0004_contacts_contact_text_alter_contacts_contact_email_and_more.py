# Generated by Django 4.2.7 on 2023-12-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='contact_text',
            field=models.TextField(blank=True, null=True, verbose_name='Ваше сообщение'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='contact_email',
            field=models.CharField(max_length=30, verbose_name='Ваш email'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='contact_name',
            field=models.CharField(max_length=30, verbose_name='Ваше имя'),
        ),
    ]
