from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

TerminalReaderReaderResourceReaderActionJson = Table(
    "terminal_reader_reader_resource_reader_actionjson",
    metadata,
    Column(
        "failure_code",
        String,
        comment="Failure code, only set if status is `failed`",
        nullable=True,
    ),
    Column(
        "failure_message",
        String,
        comment="Detailed failure message, only set if status is `failed`",
        nullable=True,
    ),
    Column(
        "process_payment_intent",
        TerminalReaderReaderResourceProcessPaymentIntentAction,
        ForeignKey("TerminalReaderReaderResourceProcessPaymentIntentAction"),
        nullable=True,
    ),
    Column(
        "process_setup_intent",
        TerminalReaderReaderResourceProcessSetupIntentAction,
        ForeignKey("TerminalReaderReaderResourceProcessSetupIntentAction"),
        nullable=True,
    ),
    Column(
        "refund_payment",
        TerminalReaderReaderResourceRefundPaymentAction,
        ForeignKey("TerminalReaderReaderResourceRefundPaymentAction"),
        nullable=True,
    ),
    Column(
        "set_reader_display",
        TerminalReaderReaderResourceSetReaderDisplayAction,
        ForeignKey("TerminalReaderReaderResourceSetReaderDisplayAction"),
        nullable=True,
    ),
    Column("status", String, comment="Status of the action performed by the reader"),
    Column("type", String, comment="Type of action performed by the reader"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["terminal_reader_reader_resource_reader_action.json"]
