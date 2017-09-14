# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=64, null=True, verbose_name='主机名')),
                ('network_ip', models.GenericIPAddressField(unique=True, verbose_name='外网IP')),
                ('manage_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='管理IP')),
                ('port', models.IntegerField(blank=True, default='22', null=True, verbose_name='ssh端口')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型号')),
                ('system', models.CharField(blank=True, max_length=128, null=True, verbose_name='系统版本')),
                ('cabinet', models.CharField(blank=True, max_length=64, null=True, verbose_name='机柜')),
                ('position', models.CharField(blank=True, max_length=64, null=True, verbose_name='位置')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='序列号')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU')),
                ('memory', models.CharField(blank=True, max_length=64, null=True, verbose_name='内存')),
                ('disk', models.CharField(blank=True, max_length=256, null=True, verbose_name='硬盘')),
                ('uplink_port', models.CharField(blank=True, max_length=256, null=True, verbose_name='上联端口')),
                ('ship_time', models.DateField(default='1970-01-01', verbose_name='出厂时间')),
                ('end_time', models.DateField(default='1970-01-01', verbose_name='到保时间')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否启用')),
                ('ps', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '资产管理',
                'db_table': 'asset',
                'permissions': set([('read_asset', '只读资产管理')]),
            },
        ),
        migrations.CreateModel(
            name='data_centers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_center_list', models.CharField(max_length=128, null=True, verbose_name='数据中心')),
            ],
            options={
                'verbose_name': '数据中心',
                'verbose_name_plural': '数据中心',
                'db_table': 'data_centers',
            },
        ),
        migrations.CreateModel(
            name='performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_use', models.CharField(blank=True, max_length=32, null=True, verbose_name='CPU使用率')),
                ('mem_use', models.CharField(blank=True, max_length=32, null=True, verbose_name='内存使用率')),
                ('in_use', models.CharField(blank=True, max_length=32, null=True, verbose_name='进流量')),
                ('out_use', models.CharField(blank=True, max_length=32, null=True, verbose_name='出流量')),
                ('cdate', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('udate', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.asset')),
            ],
            options={
                'verbose_name': '监控状态',
                'verbose_name_plural': '监控状态',
                'db_table': 'performance',
                'ordering': ['cdate'],
            },
        ),
        migrations.CreateModel(
            name='system_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='名称')),
                ('username', models.CharField(blank=True, max_length=64, null=True, verbose_name='登陆用户')),
                ('password', models.CharField(blank=True, max_length=256, null=True, verbose_name='登陆密码')),
                ('ps', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('product_line', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='产品线')),
            ],
            options={
                'verbose_name': '系统登陆用户',
                'verbose_name_plural': '系统登陆用户',
                'db_table': 'system_users',
                'permissions': set([('read_system_users', '只读系统登陆用户')]),
            },
        ),
        migrations.CreateModel(
            name='web_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, null=True, verbose_name='登录用户')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='用户地址')),
                ('login_user', models.CharField(max_length=32, null=True, verbose_name='所用账号')),
                ('host', models.CharField(max_length=32, null=True, verbose_name='登录主机')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '历史登录',
                'verbose_name_plural': '历史登录',
                'db_table': 'web_history',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='data_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.data_centers', verbose_name='数据中心'),
        ),
        migrations.AddField(
            model_name='asset',
            name='product_line',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='产品线'),
        ),
        migrations.AddField(
            model_name='asset',
            name='system_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.system_users', verbose_name='登陆用户'),
        ),
    ]
