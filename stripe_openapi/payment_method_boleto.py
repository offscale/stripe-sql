from sqlalchemy import Column, String, Table

from . import metadata

PaymentMethodBoleto.Json = Table(
    "payment_method_boleto.json",
    metadata,
    Column(
        "tax_id",
        String,
        comment="Uniquely identifies the customer tax id (CNPJ or CPF)",
        primary_key=True,
    ),
)
__all__ = ["payment_method_boleto.json"]
