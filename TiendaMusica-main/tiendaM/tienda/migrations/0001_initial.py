# Generated by Django 4.2.2 on 2023-06-14 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('idAutor', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('rfc', models.CharField(default='', max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGen', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('portada', models.ImageField(upload_to='imagenes/', verbose_name='Portada')),
                ('album', models.CharField(max_length=50)),
                ('preview', models.FileField(default='', upload_to='audios/', verbose_name='Preview')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tienda.autor')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.genero')),
            ],
        ),
    ]
