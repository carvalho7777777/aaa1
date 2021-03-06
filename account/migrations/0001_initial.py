# Generated by Django 2.2 on 2020-06-10 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='дата рождения')),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/', verbose_name='фотография')),
                ('phone', models.CharField(blank=True, max_length=140, null=True, verbose_name='телефон')),
                ('position', models.CharField(blank=True, max_length=200, null=True, verbose_name='должность')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
