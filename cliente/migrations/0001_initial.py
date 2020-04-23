# Generated by Django 3.0.5 on 2020-04-22 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_cidade', models.CharField(max_length=20)),
                ('nm_estado', models.CharField(max_length=15)),
                ('sg_estado', models.CharField(max_length=2)),
                ('nm_pais', models.CharField(max_length=10)),
                ('sg_pais', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tp_logradouro', models.CharField(max_length=15)),
                ('nm_logradouro', models.CharField(max_length=40)),
                ('nm_bairro', models.CharField(max_length=20)),
                ('cd_cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_cliente', models.CharField(max_length=45, verbose_name='Nome do Cliente')),
                ('nr_cpf', models.CharField(max_length=14, verbose_name='Número do CPF')),
                ('dt_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('nr_endereco', models.IntegerField()),
                ('dsc_complemento', models.TextField()),
                ('cd_endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Endereco')),
            ],
        ),
    ]
