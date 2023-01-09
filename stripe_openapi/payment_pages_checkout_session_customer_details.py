from sqlalchemy import Column, String, list

from . import Base


class PaymentPagesCheckoutSessionCustomerDetails(Base):
    __tablename__ = "payment_pages_checkout_session_customer_details"
    address = Column(
        Address,
        comment="[[FK(Address)]] The customer's address after a completed Checkout Session. Note: This property is populated only for sessions on or after March 30, 2022",
        nullable=True,
    )
    email = Column(
        String,
        comment="The email associated with the Customer, if one exists, on the Checkout Session after a completed Checkout Session or at time of session expiry.\nOtherwise, if the customer has consented to promotional content, this value is the most recent valid email provided by the customer on the Checkout form",
        nullable=True,
    )
    name = Column(
        String,
        comment="The customer's name after a completed Checkout Session. Note: This property is populated only for sessions on or after March 30, 2022",
        nullable=True,
    )
    phone = Column(
        String,
        comment="The customer's phone number after a completed Checkout Session",
        nullable=True,
    )
    tax_exempt = Column(
        String,
        comment="The customer’s tax exempt status after a completed Checkout Session",
        nullable=True,
    )
    tax_ids = Column(
        list,
        comment="The customer’s tax IDs after a completed Checkout Session",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentPagesCheckoutSessionCustomerDetails(address={address!r}, email={email!r}, name={name!r}, phone={phone!r}, tax_exempt={tax_exempt!r}, tax_ids={tax_ids!r})".format(
            address=self.address,
            email=self.email,
            name=self.name,
            phone=self.phone,
            tax_exempt=self.tax_exempt,
            tax_ids=self.tax_ids,
        )


__all__ = ["payment_pages_checkout_session_customer_details"]
