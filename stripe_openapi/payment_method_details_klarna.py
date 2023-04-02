from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsKlarnaJson = Table(
    "payment_method_details_klarnajson",
    metadata,
    Column(
        "payment_method_category",
        String,
        comment="The Klarna payment method used for this transaction.\nCan be one of `pay_later`, `pay_now`, `pay_with_financing`, or `pay_in_installments`",
        nullable=True,
    ),
    Column(
        "preferred_locale",
        String,
        comment="Preferred language of the Klarna authorization page that the customer is redirected to.\nCan be one of `de-AT`, `en-AT`, `nl-BE`, `fr-BE`, `en-BE`, `de-DE`, `en-DE`, `da-DK`, `en-DK`, `es-ES`, `en-ES`, `fi-FI`, `sv-FI`, `en-FI`, `en-GB`, `en-IE`, `it-IT`, `en-IT`, `nl-NL`, `en-NL`, `nb-NO`, `en-NO`, `sv-SE`, `en-SE`, `en-US`, `es-US`, `fr-FR`, `en-FR`, `cs-CZ`, `en-CZ`, `el-GR`, `en-GR`, `en-AU`, `en-NZ`, `en-CA`, `fr-CA`, `pl-PL`, `en-PL`, `pt-PT`, `en-PT`, `de-CH`, `fr-CH`, `it-CH`, or `en-CH`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_klarna.json"]
