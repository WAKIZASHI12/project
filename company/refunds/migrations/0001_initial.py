# Generated by Django 5.0.4 on 2024-04-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RefundRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processed_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
