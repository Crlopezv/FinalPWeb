# Generated by Django 4.0.4 on 2022-07-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_remove_usuario_apellidos_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=130),
        ),
    ]
