# Generated by Django 3.2.7 on 2021-10-11 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0010_bankbranch_bankinformation_clentaddressinformation_clientinformation_currency_department_designation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeesinfom',
            old_name='Designationas',
            new_name='Designation',
        ),
    ]
