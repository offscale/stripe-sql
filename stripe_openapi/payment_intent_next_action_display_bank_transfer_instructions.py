from sqlalchemy import Column, Identity, Integer, String, Table, list

from . import metadata

PaymentIntentNextActionDisplayBankTransferInstructions.Json = Table(
    "payment_intent_next_action_display_bank_transfer_instructions.json",
    metadata,
    Column(
        "amount_remaining",
        Integer,
        comment="The remaining amount that needs to be transferred to complete the payment",
        nullable=True,
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
        nullable=True,
    ),
    Column(
        "financial_addresses",
        list,
        comment="A list of financial addresses that can be used to fund the customer balance",
        nullable=True,
    ),
    Column(
        "hosted_instructions_url",
        String,
        comment="A link to a hosted page that guides your customer through completing the transfer",
        nullable=True,
    ),
    Column(
        "reference",
        String,
        comment="A string identifying this payment. Instruct your customer to include this code in the reference or memo field of their bank transfer",
        nullable=True,
    ),
    Column("type", String, comment="Type of bank transfer"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_display_bank_transfer_instructions.json"]
