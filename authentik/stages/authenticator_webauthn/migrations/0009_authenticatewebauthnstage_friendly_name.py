# Generated by Django 4.1.7 on 2023-04-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_authenticator_webauthn", "0008_alter_webauthndevice_credential_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="authenticatewebauthnstage",
            name="friendly_name",
            field=models.TextField(null=True),
        ),
    ]
