# Generated by Django 3.2.7 on 2022-07-11 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('name', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('memory', models.IntegerField()),
                ('vendor', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Fast', 'FastEthernet'), ('Giga', 'GigabitEthernet')], default='Fast', max_length=20)),
                ('slot', models.IntegerField(choices=[(0, 'Slot 0'), (1, 'Slot 1')], default=0)),
                ('port', models.IntegerField(choices=[(0, 'Port 0'), (1, 'Port 1')], default=0)),
                ('ip4_address', models.CharField(default=None, max_length=16, null=True)),
                ('status', models.CharField(choices=[('u', 'Up'), ('d', 'Down')], default='u', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('token', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddConstraint(
            model_name='usuarios',
            constraint=models.UniqueConstraint(fields=('usuario',), name='unique user'),
        ),
        migrations.AddConstraint(
            model_name='tokens',
            constraint=models.UniqueConstraint(fields=('token', 'name'), name='unique token'),
        ),
        migrations.AddField(
            model_name='interfaces',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiApp.devices'),
        ),
        migrations.AddConstraint(
            model_name='interfaces',
            constraint=models.UniqueConstraint(fields=('device', 'type', 'slot', 'port'), name='unique slot-port'),
        ),
    ]