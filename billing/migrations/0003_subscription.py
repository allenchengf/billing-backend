# Generated by Django 4.1.6 on 2023-02-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_alter_customer_created_at_alter_customer_customer_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(max_length=10)),
                ('customer_property', models.CharField(choices=[('uCDN', 'uCDN'), ('H7Connect-DC', 'H7Connect-DC'), ('H7Connect-IX', 'H7Connect-IX'), ('H7Connect-CHINA IP', 'H7Connect-CHINA IP'), ('H7Connect-VC', 'H7Connect-VC'), ('uCDN POC', 'uCDN POC'), ('Infrastructure', 'Infrastructure')], default='uCDN', max_length=100, verbose_name='Product name')),
                ('service_id', models.CharField(blank=True, max_length=50, null=True)),
                ('poc', models.CharField(default='Production', max_length=50)),
                ('status', models.CharField(default='In Use', max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]