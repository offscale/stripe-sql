from sqlalchemy import ARRAY, JSON, Boolean, Column, ForeignKey, Integer, String

from . import Base


class SetupIntent(Base):
    """
    A SetupIntent guides you through the process of setting up and saving a customer's payment credentials for future payments.

    For example, you could use a SetupIntent to set up and save your customer's card without immediately collecting a payment.
    Later, you can use [PaymentIntents](https://stripe.com/docs/api#payment_intents) to drive the payment flow.

    Create a SetupIntent as soon as you're ready to collect your customer's payment credentials.
    Do not maintain long-lived, unconfirmed SetupIntents as they may no longer be valid.
    The SetupIntent then transitions through multiple [statuses](https://stripe.com/docs/payments/intents#intent-statuses) as it guides
    you through the setup process.

    Successful SetupIntents result in payment credentials that are optimized for future payments.
    For example, cardholders in [certain regions](/guides/strong-customer-authentication) may need to be run through
    [Strong Customer Authentication](https://stripe.com/docs/strong-customer-authentication) at the time of payment method collection
    in order to streamline later [off-session payments](https://stripe.com/docs/payments/setup-intents).
    If the SetupIntent is used with a [Customer](https://stripe.com/docs/api#setup_intent_object-customer), upon success,
    it will automatically attach the resulting payment method to that Customer.
    We recommend using SetupIntents or [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) on
    PaymentIntents to save payment methods in order to prevent saving invalid or unoptimized payment methods.

    By using SetupIntents, you ensure that your customers experience the minimum set of required friction,
    even as regulations change over time.

    Related guide: [Setup Intents API](https://stripe.com/docs/payments/setup-intents).

    """

    __tablename__ = "setup_intent"
    application = Column(
        Application,
        ForeignKey("Application"),
        comment="ID of the Connect application that created the SetupIntent",
        nullable=True,
    )
    attach_to_self = Column(
        Boolean,
        comment="If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.\n\nIt can only be used for this Stripe Account???s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer",
        nullable=True,
    )
    cancellation_reason = Column(
        String,
        comment="Reason for cancellation of this SetupIntent, one of `abandoned`, `requested_by_customer`, or `duplicate`",
        nullable=True,
    )
    client_secret = Column(
        String,
        comment="The client secret of this SetupIntent. Used for client-side retrieval using a publishable key.\n\nThe client secret can be used to complete payment setup from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret",
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    customer = Column(
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="ID of the Customer this SetupIntent belongs to, if one exists.\n\nIf present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent",
        nullable=True,
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    )
    flow_directions = Column(
        ARRAY(String),
        comment="Indicates the directions of money movement for which this payment method is intended to be used.\n\nInclude `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    last_setup_error = Column(
        Integer,
        ForeignKey("api_errors.id"),
        comment="The error encountered in the previous SetupIntent confirmation",
        nullable=True,
    )
    latest_attempt = Column(
        String,
        ForeignKey("setup_attempt.id"),
        comment="The most recent SetupAttempt for this SetupIntent",
        nullable=True,
    )
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    mandate = Column(
        Mandate,
        ForeignKey("Mandate"),
        comment="ID of the multi use Mandate generated by the SetupIntent",
        nullable=True,
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    next_action = Column(
        Integer,
        ForeignKey("setup_intent_next_action.id"),
        comment="If present, this property tells you what actions you need to take in order for your customer to continue payment setup",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    on_behalf_of = Column(
        Account,
        ForeignKey("Account"),
        comment="The account (if any) for which the setup is intended",
        nullable=True,
    )
    payment_method = Column(
        String,
        ForeignKey("payment_method.id"),
        comment="ID of the payment method used with this SetupIntent",
        nullable=True,
    )
    payment_method_options = Column(
        Integer,
        ForeignKey("setup_intent_payment_method_options.id"),
        comment="Payment-method-specific configuration for this SetupIntent",
        nullable=True,
    )
    payment_method_types = Column(
        ARRAY(String),
        comment="The list of payment method types (e.g. card) that this SetupIntent is allowed to set up",
    )
    single_use_mandate = Column(
        Mandate,
        ForeignKey("Mandate"),
        comment="ID of the single_use Mandate generated by the SetupIntent",
        nullable=True,
    )
    status = Column(
        String,
        comment="[Status](https://stripe.com/docs/payments/intents#intent-statuses) of this SetupIntent, one of `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `canceled`, or `succeeded`",
    )
    usage = Column(
        String,
        comment="Indicates how the payment method is intended to be used in the future.\n\nUse `on_session` if you intend to only reuse the payment method when the customer is in your checkout flow. Use `off_session` if your customer may or may not be in your checkout flow. If not provided, this value defaults to `off_session`",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SetupIntent(application={application!r}, attach_to_self={attach_to_self!r}, cancellation_reason={cancellation_reason!r}, client_secret={client_secret!r}, created={created!r}, customer={customer!r}, description={description!r}, flow_directions={flow_directions!r}, id={id!r}, last_setup_error={last_setup_error!r}, latest_attempt={latest_attempt!r}, livemode={livemode!r}, mandate={mandate!r}, metadata={metadata!r}, next_action={next_action!r}, object={object!r}, on_behalf_of={on_behalf_of!r}, payment_method={payment_method!r}, payment_method_options={payment_method_options!r}, payment_method_types={payment_method_types!r}, single_use_mandate={single_use_mandate!r}, status={status!r}, usage={usage!r})".format(
            application=self.application,
            attach_to_self=self.attach_to_self,
            cancellation_reason=self.cancellation_reason,
            client_secret=self.client_secret,
            created=self.created,
            customer=self.customer,
            description=self.description,
            flow_directions=self.flow_directions,
            id=self.id,
            last_setup_error=self.last_setup_error,
            latest_attempt=self.latest_attempt,
            livemode=self.livemode,
            mandate=self.mandate,
            metadata=self.metadata,
            next_action=self.next_action,
            object=self.object,
            on_behalf_of=self.on_behalf_of,
            payment_method=self.payment_method,
            payment_method_options=self.payment_method_options,
            payment_method_types=self.payment_method_types,
            single_use_mandate=self.single_use_mandate,
            status=self.status,
            usage=self.usage,
        )


__all__ = ["setup_intent"]
