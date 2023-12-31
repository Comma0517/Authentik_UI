# Generated by Django 3.0.7 on 2020-06-30 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentik_flows", "0006_auto_20200629_0857"),
    ]

    operations = [
        migrations.CreateModel(
            name="OTPStaticStage",
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
                ("token_count", models.IntegerField(default=6)),
            ],
            options={
                "verbose_name": "Static Authenticator Setup Stage",
                "verbose_name_plural": "Static Authenticator Setup Stages",
            },
            bases=("authentik_flows.stage",),
        ),
    ]
