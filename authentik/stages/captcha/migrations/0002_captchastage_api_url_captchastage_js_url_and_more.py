# Generated by Django 4.1.2 on 2022-10-20 19:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_captcha", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="captchastage",
            name="api_url",
            field=models.TextField(default="https://www.recaptcha.net/recaptcha/api/siteverify"),
        ),
        migrations.AddField(
            model_name="captchastage",
            name="js_url",
            field=models.TextField(default="https://www.recaptcha.net/recaptcha/api.js"),
        ),
        migrations.AlterField(
            model_name="captchastage",
            name="private_key",
            field=models.TextField(help_text="Private key, acquired your captcha Provider."),
        ),
        migrations.AlterField(
            model_name="captchastage",
            name="public_key",
            field=models.TextField(help_text="Public key, acquired your captcha Provider."),
        ),
    ]
