# Generated by Django 3.2.12 on 2023-06-20 05:02

from django.db import migrations, models
import paas_wl.platform.applications.constants


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_build_image_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='bkapp_revision_id',
            field=models.IntegerField(help_text='与本次构建关联的 BkApp Revision id', null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='artifact_type',
            field=models.CharField(default=paas_wl.platform.applications.constants.ArtifactType['SLUG'], help_text='构件类型', max_length=16),
        ),
    ]