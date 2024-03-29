# Generated by Django 2.2.5 on 2019-12-04 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DanceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mon_raised', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dance_team', to='teams.Team')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
