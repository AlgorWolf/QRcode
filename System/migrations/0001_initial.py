# Generated by Django 5.0.1 on 2024-01-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('faculty', models.CharField(choices=[('ENGINEERING', 'ENGINEERING'), ('SCIENCE', 'SCIENCE')], max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('mat_no', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500'), ('600', '600'), ('700', '700')], default=1, max_length=200)),
                ('session', models.CharField(default='2020/2023', max_length=200)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='qrcodes/')),
                ('preview', models.URLField(blank=True, default='', null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
