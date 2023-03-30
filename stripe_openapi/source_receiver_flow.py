from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceReceiverFlow.Json = Table(
    "source_receiver_flow.json",
    metadata,
    Column(
        "address",
        String,
        comment="The address of the receiver source. This is the value that should be communicated to the customer to send their funds to",
        nullable=True,
    ),
    Column(
        "amount_charged",
        Integer,
        comment="The total amount that was moved to your balance. This is almost always equal to the amount charged. In rare cases when customers deposit excess funds and we are unable to refund those, those funds get moved to your balance and show up in amount_charged as well. The amount charged is expressed in the source's currency",
    ),
    Column(
        "amount_received",
        Integer,
        comment="The total amount received by the receiver source. `amount_received = amount_returned + amount_charged` should be true for consumed sources unless customers deposit excess funds. The amount received is expressed in the source's currency",
    ),
    Column(
        "amount_returned",
        Integer,
        comment="The total amount that was returned to the customer. The amount returned is expressed in the source's currency",
    ),
    Column(
        "refund_attributes_method",
        String,
        comment="Type of refund attribute method, one of `email`, `manual`, or `none`",
    ),
    Column(
        "refund_attributes_status",
        String,
        comment="Type of refund attribute status, one of `missing`, `requested`, or `available`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_receiver_flow.json"]
