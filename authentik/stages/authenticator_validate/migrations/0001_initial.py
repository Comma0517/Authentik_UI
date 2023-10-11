# Generated by Django 3.0.7 on 2020-06-13 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentik_flows", "0007_auto_20200703_2059"),
    ]

    operations = [
        migrations.CreateModel(
            name="OTPValidateStage",
            fields=[
                (
                    "stage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_flows.Stage",
                    ),
                ),
                (
                    "not_configured_action",
                    models.TextField(choices=[("skip", "Skip")], default="skip"),
                ),
            ],
            options={
                "verbose_name": "OTP Validation Stage",
                "verbose_name_plural": "OTP Validation Stages",
            },
            bases=("authentik_flows.stage",),
        ),
    ]
