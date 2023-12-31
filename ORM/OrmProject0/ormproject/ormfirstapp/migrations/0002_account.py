# Generated by Django 4.2.5 on 2023-10-15 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ormfirstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('month', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('description', models.TextField(default='', max_length=300)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ormfirstapp.emp')),
            ],
            options={
                'db_table': 'account',
            },
        ),
    ]
