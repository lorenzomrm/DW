# Generated by Django 3.1.4 on 2022-12-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telainicial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pets',
            old_name='descricao',
            new_name='descrição',
        ),
        migrations.RenameField(
            model_name='pets',
            old_name='especie',
            new_name='espécie',
        ),
        migrations.RenameField(
            model_name='pets',
            old_name='raca',
            new_name='raça',
        ),
        migrations.AlterField(
            model_name='pets',
            name='castrado',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1),
        ),
    ]
