# Generated by Django 2.2.14 on 2020-07-11 20:23

import appBookflix.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appBookflix', '0003_auto_20200711_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 853698, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 853737, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 853664, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 853716, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 854282, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 854324, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 854253, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 854302, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 854890, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 854866, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updownnovedad',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 855371, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownnovedad',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 855345, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 855848, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 20, 23, 5, 855825, tzinfo=utc), validators=[appBookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
    ]
