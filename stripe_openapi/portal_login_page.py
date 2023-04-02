from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

PortalLoginPageJson = Table(
    "portal_login_pagejson",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="If `true`, a shareable `url` will be generated that will take your customers to a hosted login page for the customer portal.\n\nIf `false`, the previously generated `url`, if any, will be deactivated",
    ),
    Column(
        "url",
        String,
        comment="A shareable URL to the hosted portal login page. Your customers will be able to log in with their [email](https://stripe.com/docs/api/customers/object#customer_object-email) and receive a link to their customer portal",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_login_page.json"]
