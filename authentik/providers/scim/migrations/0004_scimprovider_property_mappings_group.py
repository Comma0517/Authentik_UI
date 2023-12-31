# Generated by Django 4.1.7 on 2023-03-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_core", "0025_alter_provider_authorization_flow"),
        ("authentik_providers_scim", "0003_scimgroup"),
    ]

    operations = [
        migrations.AddField(
            model_name="scimprovider",
            name="property_mappings_group",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="Property mappings used for group creation/updating.",
                to="authentik_core.propertymapping",
            ),
        ),
    ]
