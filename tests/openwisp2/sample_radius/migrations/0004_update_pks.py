from django.db import migrations
from openwisp_radius.migrations import UUIDMigrator


class Migration(migrations.Migration):

    dependencies = [
        ('sample_radius', '0003_alter_radiusmodels_pk'),
    ]

    operations = [
        migrations.RunPython(
            UUIDMigrator.upgrade_primary_keys, reverse_code=migrations.RunPython.noop
        ),
    ]
