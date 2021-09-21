# Generated by Django 3.2.5 on 2021-09-18 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0016_clientinformation_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankinformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Client_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.branchinformationm')),
            ],
        ),
        migrations.CreateModel(
            name='BankBranch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Branch_Name', models.CharField(blank=True, max_length=700, null=True)),
                ('Address', models.CharField(blank=True, max_length=700, null=True)),
                ('Phone', models.CharField(blank=True, max_length=55, null=True)),
                ('Email', models.EmailField(blank=True, max_length=55, null=True)),
                ('Client_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance.clientinformation')),
            ],
        ),
    ]