# Generated by Django 4.0.2 on 2022-03-20 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_alter_contract_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='customer',
            new_name='is_customer',
        ),
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.company'),
        ),
    ]