# Generated by Django 3.1.6 on 2021-02-16 08:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_flows", "0016_auto_20201202_1307"),
        ("authentik_stages_authenticator_validate", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="OTPValidateStage",
            new_name="AuthenticatorValidateStage",
        ),
        migrations.AlterModelOptions(
            name="authenticatorvalidatestage",
            options={
                "verbose_name": "Authenticator Validation Stage",
                "verbose_name_plural": "Authenticator Validation Stages",
            },
        ),
    ]
