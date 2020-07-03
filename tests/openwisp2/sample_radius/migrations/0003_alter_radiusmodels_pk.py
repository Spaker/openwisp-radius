# Generated by Django 3.0.7 on 2020-06-15 22:28

from django.db import migrations, models
import uuid
from openwisp_radius.migrations import UUIDMigrator


class Migration(migrations.Migration):

    dependencies = [
        ('sample_radius', '0002_default_groups_and_permissions'),
    ]

    operations = [
        migrations.RunPython(
            UUIDMigrator.backup_data, reverse_code=migrations.RunPython.noop
        ),
        migrations.RemoveField(model_name='radiusaccounting', name='id',),
        migrations.AlterField(
            model_name='nas',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name='radiusaccounting',
            name='unique_id',
            field=models.CharField(
                db_column='acctuniqueid',
                max_length=32,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name='accounting unique ID',
            ),
        ),
        migrations.AlterField(
            model_name='radiuscheck',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name='radiusgroupcheck',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name='radiusgroupreply',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name='radiuspostauth',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name='radiusreply',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name='radiususergroup',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
