from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

TerminalReaderReaderResourceProcessSetupIntentAction.Json = Table(
    "terminal_reader_reader_resource_process_setup_intent_action.json",
    metadata,
    Column(
        "generated_card",
        String,
        comment="ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod",
        nullable=True,
    ),
    Column(
        "setup_intent",
        SetupIntent,
        ForeignKey("SetupIntent"),
        comment="Most recent SetupIntent processed by the reader",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["terminal_reader_reader_resource_process_setup_intent_action.json"]
