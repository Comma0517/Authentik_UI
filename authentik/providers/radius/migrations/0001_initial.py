# Generated by Django 4.1.7 on 2023-03-20 10:58

import django.db.models.deletion
from django.db import migrations, models

import authentik.lib.generators


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentik_core", "0027_alter_user_uuid"),
    ]

    operations = [
        migrations.CreateModel(
            name="RadiusProvider",
            fields=[
                (
                    "provider_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_core.provider",
                    ),
                ),
                (
                    "shared_secret",
                    models.TextField(
                        default=authentik.lib.generators.generate_id,
                        help_text="Shared secret between clients and server to hash packets.",
                    ),
                ),
                (
                    "client_networks",
                    models.TextField(
                        default="0.0.0.0/0, ::/0",
                        help_text="List of CIDRs (comma-separated) that clients can connect from. A more specific CIDR will match before a looser one. Clients connecting from a non-specified CIDR will be dropped.",
                    ),
                ),
            ],
            options={
                "verbose_name": "Radius Provider",
                "verbose_name_plural": "Radius Providers",
            },
            bases=("authentik_core.provider", models.Model),
        ),
    ]
