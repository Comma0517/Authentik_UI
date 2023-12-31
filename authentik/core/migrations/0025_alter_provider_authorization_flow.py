# Generated by Django 4.1.7 on 2023-03-02 21:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_flows", "0025_alter_flowstagebinding_evaluate_on_plan_and_more"),
        ("authentik_core", "0024_source_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provider",
            name="authorization_flow",
            field=models.ForeignKey(
                help_text="Flow used when authorizing this provider.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="provider_authorization",
                to="authentik_flows.flow",
            ),
        ),
    ]
