# Generated by Django 4.1 on 2022-08-06 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField(verbose_name='fecha de publicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.IntegerField(default=0)),
                ('reservado', models.BooleanField(default=False)),
                ('descontable', models.BooleanField(default=False)),
                ('fecha_publicacion', models.DateTimeField(verbose_name='fecha de publicacion')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ferreteriaOnlineApp.categoria')),
            ],
        ),
    ]
