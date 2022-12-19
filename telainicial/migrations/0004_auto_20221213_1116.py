# Generated by Django 3.1.4 on 2022-12-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telainicial', '0003_auto_20221213_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='castrado',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='porte',
            field=models.CharField(choices=[('Mini', 'Mini'), ('Pequeno', 'Pequeno'), ('Médio', 'Médio'), ('Grande', 'Grande'), ('Extra Grande', 'Extra Grande')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sexo',
            field=models.CharField(choices=[('Macho', 'Macho'), ('Fêmea', 'Fêmea')], max_length=5, null=True),
        ),
    ]