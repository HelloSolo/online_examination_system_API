# Generated by Django 4.0.6 on 2022-07-08 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_response_response_candidate_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_score', models.CharField(max_length=10)),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.candidate')),
            ],
        ),
    ]
