# Generated by Django 3.2.8 on 2021-10-12 15:39

import django.db.models.deletion
from django.apps.registry import Apps
from django.core.exceptions import FieldError
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor

import authentik.lib.models
import authentik.providers.proxy.models


def migrate_defaults(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    from authentik.providers.oauth2.models import JWTAlgorithms
    from authentik.providers.proxy.models import ProxyProvider

    db_alias = schema_editor.connection.alias
    try:
        for provider in ProxyProvider.objects.using(db_alias).filter(jwt_alg=JWTAlgorithms.RS256):
            provider.set_oauth_defaults()
            provider.save()
    except FieldError:
        # If the jwt_alg field doesn't exist, just ignore this migration
        pass


def migrate_mode(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    from authentik.providers.proxy.models import ProxyMode

    db_alias = schema_editor.connection.alias
    ProxyProvider = apps.get_model("authentik_providers_proxy", "proxyprovider")
    for provider in ProxyProvider.objects.using(db_alias).all():
        if provider.forward_auth_mode:
            provider.mode = ProxyMode.FORWARD_SINGLE
            provider.save()


class Migration(migrations.Migration):
    replaces = [
        ("authentik_providers_proxy", "0001_initial"),
        ("authentik_providers_proxy", "0002_proxyprovider_cookie_secret"),
        ("authentik_providers_proxy", "0003_proxyprovider_certificate"),
        ("authentik_providers_proxy", "0004_auto_20200913_1947"),
        ("authentik_providers_proxy", "0005_auto_20200914_1536"),
        ("authentik_providers_proxy", "0006_proxyprovider_skip_path_regex"),
        ("authentik_providers_proxy", "0007_auto_20200923_1017"),
        ("authentik_providers_proxy", "0008_auto_20200930_0810"),
        ("authentik_providers_proxy", "0009_auto_20201007_1721"),
        ("authentik_providers_proxy", "0010_auto_20201214_0942"),
        ("authentik_providers_proxy", "0011_proxyprovider_forward_auth_mode"),
        ("authentik_providers_proxy", "0012_proxyprovider_cookie_domain"),
        ("authentik_providers_proxy", "0013_mode"),
        ("authentik_providers_proxy", "0014_proxy_v2"),
    ]

    initial = True

    dependencies = [
        ("authentik_crypto", "0002_create_self_signed_kp"),
        ("authentik_providers_oauth2", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProxyProvider",
            fields=[
                (
                    "oauth2provider_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_providers_oauth2.oauth2provider",
                    ),
                ),
                (
                    "internal_host",
                    models.TextField(
                        blank=True,
                        validators=[
                            authentik.lib.models.DomainlessURLValidator(schemes=("http", "https"))
                        ],
                    ),
                ),
                (
                    "external_host",
                    models.TextField(
                        validators=[
                            authentik.lib.models.DomainlessURLValidator(schemes=("http", "https"))
                        ]
                    ),
                ),
                (
                    "cookie_secret",
                    models.TextField(default=authentik.providers.proxy.models.get_cookie_secret),
                ),
                (
                    "certificate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="authentik_crypto.certificatekeypair",
                    ),
                ),
                (
                    "skip_path_regex",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text=(
                            "Regular expressions for which authentication is not required. Each new"
                            " line is interpreted as a new Regular Expression."
                        ),
                    ),
                ),
                (
                    "internal_host_ssl_validation",
                    models.BooleanField(
                        default=True,
                        help_text="Validate SSL Certificates of upstream servers",
                        verbose_name="Internal host SSL Validation",
                    ),
                ),
                (
                    "basic_auth_enabled",
                    models.BooleanField(
                        default=False,
                        help_text=(
                            "Set a custom HTTP-Basic Authentication header based on values from"
                            " authentik."
                        ),
                        verbose_name="Set HTTP-Basic Authentication",
                    ),
                ),
                (
                    "basic_auth_password_attribute",
                    models.TextField(
                        blank=True,
                        help_text=(
                            "User/Group Attribute used for the password part of the HTTP-Basic"
                            " Header."
                        ),
                        verbose_name="HTTP-Basic Password Key",
                    ),
                ),
                (
                    "basic_auth_user_attribute",
                    models.TextField(
                        blank=True,
                        help_text=(
                            "User/Group Attribute used for the user part of the HTTP-Basic Header."
                            " If not set, the user's Email address is used."
                        ),
                        verbose_name="HTTP-Basic Username Key",
                    ),
                ),
                (
                    "forward_auth_mode",
                    models.BooleanField(
                        default=False,
                        help_text=(
                            "Enable support for forwardAuth in traefik and nginx auth_request."
                            " Exclusive with internal_host."
                        ),
                    ),
                ),
                ("cookie_domain", models.TextField(blank=True, default="")),
                (
                    "mode",
                    models.TextField(
                        choices=[
                            ("proxy", "Proxy"),
                            ("forward_single", "Forward Single"),
                            ("forward_domain", "Forward Domain"),
                        ],
                        default="proxy",
                        help_text=(
                            "Enable support for forwardAuth in traefik and nginx auth_request."
                            " Exclusive with internal_host."
                        ),
                    ),
                ),
            ],
            options={
                "verbose_name": "Proxy Provider",
                "verbose_name_plural": "Proxy Providers",
            },
            bases=("authentik_providers_oauth2.oauth2provider",),
        ),
        migrations.RunPython(
            code=migrate_mode,
        ),
        migrations.RemoveField(
            model_name="proxyprovider",
            name="forward_auth_mode",
        ),
        migrations.RunPython(
            code=migrate_defaults,
        ),
    ]
