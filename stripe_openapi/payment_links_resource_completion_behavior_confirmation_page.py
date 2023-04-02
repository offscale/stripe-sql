from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentLinksResourceCompletionBehaviorConfirmationPageJson = Table(
    "payment_links_resource_completion_behavior_confirmation_pagejson",
    metadata,
    Column(
        "custom_message",
        String,
        comment="The custom message that is displayed to the customer after the purchase is complete",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_completion_behavior_confirmation_page.json"]
