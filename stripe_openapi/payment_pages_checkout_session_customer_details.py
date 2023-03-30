from sqlalchemy import Column, ForeignKey, String, Table, list

from stripe_openapi.address import Address

from . import metadata

PaymentPagesCheckoutSessionCustomerDetails.Json = Table(
    "payment_pages_checkout_session_customer_details.json",
    metadata,
    Column(
        "address",
        Address,
        ForeignKey("Address"),
        comment="The customer's address after a completed Checkout Session. Note: This property is populated only for sessions on or after March 30, 2022",
        nullable=True,
    ),
    Column(
        "email",
        String,
        comment="The email associated with the Customer, if one exists, on the Checkout Session after a completed Checkout Session or at time of session expiry.\nOtherwise, if the customer has consented to promotional content, this value is the most recent valid email provided by the customer on the Checkout form",
        nullable=True,
    ),
    Column(
        "name",
        String,
        comment="The customer's name after a completed Checkout Session. Note: This property is populated only for sessions on or after March 30, 2022",
        nullable=True,
    ),
    Column(
        "phone",
        String,
        comment="The customer's phone number after a completed Checkout Session",
        nullable=True,
    ),
    Column(
        "tax_exempt",
        String,
        comment="The customer’s tax exempt status after a completed Checkout Session",
        nullable=True,
    ),
    Column(
        "tax_ids",
        list,
        comment="The customer’s tax IDs after a completed Checkout Session",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["payment_pages_checkout_session_customer_details.json"]
