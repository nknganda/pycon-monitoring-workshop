# Generated by Django 2.1.2 on 2018-10-14 05:30

from django.db import migrations, models
import django_fsm
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(choices=[('received', 'RECEIVED'), ('started', 'STARTED'), ('failed', 'FAILED'), ('submitted', 'SUBMITTED'), ('completed', 'COMPLETED')], db_index=True, default='received', max_length=50, protected=True)),
                ('message_id', models.CharField(db_index=True, max_length=255)),
                ('data', jsonfield.fields.JSONField(default={'attempts': 0})),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]
