# Generated by Django 5.0.1 on 2024-06-01 11:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='burger', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('ingredients', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('FastFood', 'FastFood'), ('PakistaniCuisine', 'PakistaniCuisine'), ('Continental', 'Continental'), ('Desserts', 'Desserts')], default='FF', max_length=100)),
                ('product_description', models.TextField(default='none', max_length=300)),
                ('product_quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MenuItems.customer')),
            ],
        ),
        migrations.CreateModel(
            name='dineIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='nihal', max_length=200)),
                ('email', models.CharField(default='none', max_length=200, null=True)),
                ('number', models.CharField(default='111', max_length=100, null=True)),
                ('table_no', models.CharField(default='none', max_length=200)),
                ('people', models.CharField(default='none', max_length=100)),
                ('requests', models.CharField(default='none', max_length=500)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MenuItems.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MenuItems.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MenuItems.product')),
            ],
        ),
        migrations.CreateModel(
            name='shipping_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='nihal', max_length=200)),
                ('email', models.CharField(default='none', max_length=200, null=True)),
                ('number', models.CharField(default='111', max_length=100, null=True)),
                ('address', models.CharField(default='none', max_length=400)),
                ('city', models.CharField(default='lahore', max_length=200)),
                ('province', models.CharField(default='none', max_length=200)),
                ('zipcode', models.CharField(default='none', max_length=100)),
                ('instruction', models.CharField(default='none', max_length=500)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MenuItems.order')),
            ],
        ),
    ]
