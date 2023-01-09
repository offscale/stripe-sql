from sqlalchemy import Boolean, Column, ForeignKey, String

from stripe_openapi.payment_method import PaymentMethod

from . import Base


class Mandate(Base):
    """
    A Mandate is a record of the permission a customer has given you to debit their payment method.
    """

    __tablename__ = "mandate"
    customer_acceptance = Column(Integer, ForeignKey("customer_acceptance.id"))
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    multi_use = Column(Integer, ForeignKey("mandate_multi_use.id"), nullable=True)
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    payment_method = Column(
        PaymentMethod,
        comment="[[FK(PaymentMethod)]] ID of the payment method associated with this mandate",
    )
    payment_method_details = Column(
        Integer, ForeignKey("mandate_payment_method_details.id")
    )
    single_use = Column(Integer, ForeignKey("mandate_single_use.id"), nullable=True)
    status = Column(
        String,
        comment="The status of the mandate, which indicates whether it can be used to initiate a payment",
    )
    type = Column(String, comment="The type of the mandate")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Mandate(customer_acceptance={customer_acceptance!r}, id={id!r}, livemode={livemode!r}, multi_use={multi_use!r}, object={object!r}, payment_method={payment_method!r}, payment_method_details={payment_method_details!r}, single_use={single_use!r}, status={status!r}, type={type!r})".format(
            customer_acceptance=self.customer_acceptance,
            id=self.id,
            livemode=self.livemode,
            multi_use=self.multi_use,
            object=self.object,
            payment_method=self.payment_method,
            payment_method_details=self.payment_method_details,
            single_use=self.single_use,
            status=self.status,
            type=self.type,
        )


__all__ = ["mandate"]
