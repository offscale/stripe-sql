from sqlalchemy import Boolean, Column, Integer, String


class Setup_Attempt(Base):
    """
    A SetupAttempt describes one attempted confirmation of a SetupIntent,

    whether that confirmation was successful or unsuccessful. You can use
    SetupAttempts to inspect details of a specific attempt at setting up a
    payment method using a SetupIntent.

    """

    __tablename__ = "setup_attempt"
    application = Column(
        Application,
        comment="The value of [application](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-application) on the SetupIntent at the time of this confirmation",
        nullable=True,
    )
    attach_to_self = Column(
        Boolean,
        comment="If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.\n\nIt can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer",
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    customer = Column(
        string | Customer,
        comment="The value of [customer](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-customer) on the SetupIntent at the time of this confirmation",
        nullable=True,
    )
    flow_directions = Column(
        ARRAY(String),
        comment="Indicates the directions of money movement for which this payment method is intended to be used.\n\nInclude `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    on_behalf_of = Column(
        Account,
        comment="The value of [on_behalf_of](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-on_behalf_of) on the SetupIntent at the time of this confirmation",
        nullable=True,
    )
    payment_method = Column(
        PaymentMethod, comment="ID of the payment method used with this SetupAttempt"
    )
    payment_method_details = Column(SetupAttemptPaymentMethodDetails)
    setup_error = Column(
        ApiErrors,
        comment="The error encountered during this attempt to confirm the SetupIntent, if any",
        nullable=True,
    )
    setup_intent = Column(
        SetupIntent, comment="ID of the SetupIntent that this attempt belongs to"
    )
    status = Column(
        String,
        comment="Status of this SetupAttempt, one of `requires_confirmation`, `requires_action`, `processing`, `succeeded`, `failed`, or `abandoned`",
    )
    usage = Column(
        String,
        comment="The value of [usage](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-usage) on the SetupIntent at the time of this confirmation, one of `off_session` or `on_session`",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Setup_Attempt(application={application!r}, attach_to_self={attach_to_self!r}, created={created!r}, customer={customer!r}, flow_directions={flow_directions!r}, id={id!r}, livemode={livemode!r}, object={object!r}, on_behalf_of={on_behalf_of!r}, payment_method={payment_method!r}, payment_method_details={payment_method_details!r}, setup_error={setup_error!r}, setup_intent={setup_intent!r}, status={status!r}, usage={usage!r})".format(
            application=self.application,
            attach_to_self=self.attach_to_self,
            created=self.created,
            customer=self.customer,
            flow_directions=self.flow_directions,
            id=self.id,
            livemode=self.livemode,
            object=self.object,
            on_behalf_of=self.on_behalf_of,
            payment_method=self.payment_method,
            payment_method_details=self.payment_method_details,
            setup_error=self.setup_error,
            setup_intent=self.setup_intent,
            status=self.status,
            usage=self.usage,
        )


__all__ = ["setup_attempt"]
