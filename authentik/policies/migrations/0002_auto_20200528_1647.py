# Generated by Django 3.0.6 on 2020-05-28 16:47

import django.db.models.deletion
from django.db import migrations, models

import authentik.lib.models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_policies", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="policy",
            options={
                "base_manager_name": "objects",
                "verbose_name": "Policy",
                "verbose_name_plural": "Policies",
            },
        ),
        migrations.RemoveField(
            model_name="policy",
            name="negate",
        ),
        migrations.RemoveField(
            model_name="policy",
            name="order",
        ),
        migrations.RemoveField(
            model_name="policy",
            name="timeout",
        ),
        migrations.AddField(
            model_name="policybinding",
            name="negate",
            field=models.BooleanField(
                default=False,
                help_text="Negates the outcome of the policy. Messages are unaffected.",
            ),
        ),
        migrations.AddField(
            model_name="policybinding",
            name="timeout",
            field=models.IntegerField(
                default=30,
                help_text="Timeout after which Policy execution is terminated.",
            ),
        ),
        migrations.AlterField(
            model_name="policybinding",
            name="order",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="policybinding",
            name="policy",
            field=authentik.lib.models.InheritanceForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="authentik_policies.Policy",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="policybinding",
            unique_together={("policy", "target", "order")},
        ),
    ]
