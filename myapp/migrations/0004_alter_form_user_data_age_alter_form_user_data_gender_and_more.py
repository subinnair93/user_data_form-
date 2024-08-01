# Generated by Django 5.0.7 on 2024-07-26 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_form_user_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_user_data',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='form_user_data',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='form_user_data',
            name='marital_status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], max_length=50),
        ),
    ]