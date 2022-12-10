# Generated by Django 3.1.4 on 2022-12-10 14:41

from django.db import migrations, models
import stdimage.models
import telainicial.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField(null=True)),
                ('sexo', models.CharField(choices=[('M', 'Macho'), ('F', 'Fêmea')], max_length=1)),
                ('especie', models.CharField(choices=[('C', 'Cão'), ('G', 'Gato')], max_length=4)),
                ('raca', models.CharField(max_length=30)),
                ('porte', models.CharField(choices=[('XP', 'Mini'), ('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande'), ('XG', 'Extra Grande')], max_length=2)),
                ('descricao', models.TextField()),
                ('castrado', models.CharField(max_length=3)),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to=telainicial.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
            ],
        ),
    ]
