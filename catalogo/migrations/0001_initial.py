# Generated by Django 2.1.7 on 2019-02-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('genero', models.CharField(choices=[('ac', 'Ação'), ('fc', 'Ficção'), ('tr', 'Terror'), ('av', 'Aventura'), ('cm', 'Comédia'), ('dr', 'Drama'), ('ro', 'Romance')], default='ac', max_length=2)),
                ('sinopse', models.TextField()),
                ('lancamento', models.DateField()),
                ('duracao', models.PositiveIntegerField()),
                ('classificacao_indicativa', models.PositiveIntegerField()),
                ('cartaz', models.ImageField(upload_to='media')),
            ],
        ),
    ]