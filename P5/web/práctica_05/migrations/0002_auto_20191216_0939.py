# Generated by Django 2.2.8 on 2019-12-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('práctica_05', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='miembros',
            field=models.ManyToManyField(blank=True, to='práctica_05.Musico'),
        ),
    ]
