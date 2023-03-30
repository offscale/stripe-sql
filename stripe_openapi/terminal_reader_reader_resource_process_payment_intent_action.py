from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

TerminalReaderReaderResourceProcessPaymentIntentAction.Json = Table(
    "terminal_reader_reader_resource_process_payment_intent_action.json",
    metadata,
    Column(
        "payment_intent",
        PaymentIntent,
        ForeignKey("PaymentIntent"),
        comment="Most recent PaymentIntent processed by the reader",
    ),
    Column(
        "process_config",
        TerminalReaderReaderResourceProcessConfig,
        ForeignKey("TerminalReaderReaderResourceProcessConfig"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["terminal_reader_reader_resource_process_payment_intent_action.json"]
