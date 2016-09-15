# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dacParser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dacParser.Offering')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type', models.CharField(choices=[('T', 'Text'), ('O', 'Option'), ('N', 'Numeric')], max_length=2)),
                ('choices', models.ManyToManyField(blank=True, to='gda.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('questions', models.ManyToManyField(blank=True, to='gda.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.CharField(editable=False, max_length=37, primary_key=True, serialize=False)),
                ('used', models.BooleanField(default=False)),
                ('offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dacParser.Offering')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dacParser.Student')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gda.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='token',
            unique_together=set([('student', 'offering', 'token')]),
        ),
    ]
