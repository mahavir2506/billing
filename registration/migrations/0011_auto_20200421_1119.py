# Generated by Django 3.0.2 on 2020-04-21 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20200420_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Store'),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField(unique=True)),
                ('cust_name', models.CharField(max_length=100)),
                ('name', models.FileField(upload_to='bill/')),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Store')),
            ],
        ),
    ]
