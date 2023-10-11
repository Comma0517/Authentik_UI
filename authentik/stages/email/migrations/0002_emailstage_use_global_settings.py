# Generated by Django 3.1.4 on 2021-01-04 13:15

from django.apps.registry import Apps
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def update_template_path(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    EmailStage = apps.get_model("authentik_stages_email", "EmailStage")
    db_alias = schema_editor.connection.alias

    for stage in EmailStage.objects.using(db_alias).all():
        stage.template = stage.template.replace("stages/email/for_email/", "email/")
        stage.save()


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_email", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="emailstage",
            name="use_global_settings",
            field=models.BooleanField(
                default=False,
                help_text=(
                    "When enabled, global Email connection settings will be used and connection"
                    " settings below will be ignored."
                ),
            ),
        ),
        migrations.RunPython(update_template_path),
    ]
