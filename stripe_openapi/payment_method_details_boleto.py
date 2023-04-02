from sqlalchemy import Column, String, Table

from . import metadata

PaymentMethodDetailsBoletoJson = Table(
    "payment_method_details_boletojson",
    metadata,
    Column(
        "tax_id",
        String,
        comment="The tax ID of the customer (CPF for individuals consumers or CNPJ for businesses consumers)",
        primary_key=True,
    ),
)
__all__ = ["payment_method_details_boleto.json"]
