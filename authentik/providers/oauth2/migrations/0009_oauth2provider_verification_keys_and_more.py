# Generated by Django 4.0.3 on 2022-03-29 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_crypto", "0003_certificatekeypair_managed"),
        ("authentik_providers_oauth2", "0008_rename_rsa_key_oauth2provider_signing_key_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="oauth2provider",
            name="verification_keys",
            field=models.ManyToManyField(
                help_text=(
                    "JWTs created with the configured certificates can authenticate with this"
                    " provider."
                ),
                related_name="+",
                to="authentik_crypto.certificatekeypair",
                verbose_name="Allowed certificates for JWT-based client_credentials",
            ),
        ),
        migrations.AlterField(
            model_name="oauth2provider",
            name="signing_key",
            field=models.ForeignKey(
                help_text=(
                    "Key used to sign the tokens. Only required when JWT Algorithm is set to RS256."
                ),
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="authentik_crypto.certificatekeypair",
                verbose_name="Signing Key",
            ),
        ),
    ]
