# Generated by Django 4.0.2 on 2022-02-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_remove_contract_status_contract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]