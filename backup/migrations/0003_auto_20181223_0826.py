# Generated by Django 2.1.4 on 2018-12-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0002_auto_20181223_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_backup',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания записи'),
        ),
        migrations.AlterField(
            model_name='client_backup',
            name='dir',
            field=models.CharField(max_length=1500, verbose_name='Путь к катологу'),
        ),
        migrations.AlterField(
            model_name='client_backup',
            name='ip',
            field=models.GenericIPAddressField(protocol='IPv4', verbose_name='ip адрес'),
        ),
        migrations.AlterField(
            model_name='client_backup',
            name='mount',
            field=models.CharField(max_length=1500, verbose_name='монтирование каталога'),
        ),
        migrations.AlterField(
            model_name='client_backup',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client_backup',
            name='umount',
            field=models.CharField(max_length=1500, verbose_name='размонтирование каталога'),
        ),
        migrations.AlterField(
            model_name='storge_backup',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания записи'),
        ),
        migrations.AlterField(
            model_name='storge_backup',
            name='dir',
            field=models.CharField(max_length=1500, verbose_name='Путь к катологу'),
        ),
        migrations.AlterField(
            model_name='storge_backup',
            name='ip',
            field=models.GenericIPAddressField(protocol='IPv4', verbose_name='ip адрес'),
        ),
        migrations.AlterField(
            model_name='storge_backup',
            name='mount',
            field=models.CharField(max_length=1500, verbose_name='монтирование каталога'),
        ),
        migrations.AlterField(
            model_name='storge_backup',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='storge_backup',
            name='umount',
            field=models.CharField(max_length=1500, verbose_name='размонтирование каталога'),
        ),
    ]
