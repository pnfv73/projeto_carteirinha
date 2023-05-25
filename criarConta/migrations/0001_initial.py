# Generated by Django 4.2.1 on 2023-05-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('idfunc', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('regfuncional', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('senha', models.CharField(max_length=15)),
            ],
        ),

        migrations.RenameField(
            model_name='Funcionario',
            old_name='regfuncional',
            new_name='registro_funcional',            
                 
        ),

        migrations.RenameField(
            model_name='Funcionario',
            old_name='nome',
            new_name='nome_completo',
        ),        
    ]
