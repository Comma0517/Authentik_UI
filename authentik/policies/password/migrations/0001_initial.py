# Generated by Django 3.0.6 on 2020-05-19 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentik_policies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PasswordPolicy",
            fields=[
                (
                    "policy_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_policies.Policy",
                    ),
                ),
                ("amount_uppercase", models.IntegerField(default=0)),
                ("amount_lowercase", models.IntegerField(default=0)),
                ("amount_symbols", models.IntegerField(default=0)),
                ("length_min", models.IntegerField(default=0)),
                (
                    "symbol_charset",
                    models.TextField(default="!\\\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "),
                ),
                ("error_message", models.TextField()),
            ],
            options={
                "verbose_name": "Password Policy",
                "verbose_name_plural": "Password Policies",
            },
            bases=("authentik_policies.policy",),
        ),
    ]
