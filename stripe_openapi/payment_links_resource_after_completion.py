from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

PaymentLinksResourceAfterCompletion.Json = Table(
    "payment_links_resource_after_completion.json",
    metadata,
    Column(
        "hosted_confirmation",
        PaymentLinksResourceCompletionBehaviorConfirmationPage,
        ForeignKey("PaymentLinksResourceCompletionBehaviorConfirmationPage"),
        nullable=True,
    ),
    Column(
        "redirect",
        PaymentLinksResourceCompletionBehaviorRedirect,
        ForeignKey("PaymentLinksResourceCompletionBehaviorRedirect"),
        nullable=True,
    ),
    Column(
        "type", String, comment="The specified behavior after the purchase is complete"
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_after_completion.json"]
