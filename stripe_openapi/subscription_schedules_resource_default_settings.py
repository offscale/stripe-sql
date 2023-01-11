from sqlalchemy import Column, Float, ForeignKey, Identity, Integer, String

from . import Base


class SubscriptionSchedulesResourceDefaultSettings(Base):
    __tablename__ = "subscription_schedules_resource_default_settings"
    application_fee_percent = Column(
        Float,
        comment="A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the application owner's Stripe account during this phase of the schedule",
        nullable=True,
    )
    automatic_tax = Column(
        Integer,
        ForeignKey("subscription_schedules_resource_default_settings_automatic_tax.id"),
        nullable=True,
    )
    billing_cycle_anchor = Column(
        String,
        comment="Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle)",
    )
    billing_thresholds = Column(
        Integer,
        ForeignKey("subscription_billing_thresholds.id"),
        comment="Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period",
        nullable=True,
    )
    collection_method = Column(
        String,
        comment="Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`",
        nullable=True,
    )
    default_payment_method = Column(
        String,
        ForeignKey("payment_method.id"),
        comment="ID of the default payment method for the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings",
        nullable=True,
    )
    description = Column(
        String,
        comment="Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription",
        nullable=True,
    )
    invoice_settings = Column(
        Integer,
        ForeignKey("invoice_setting_subscription_schedule_setting.id"),
        comment="The subscription schedule's default invoice settings",
        nullable=True,
    )
    on_behalf_of = Column(
        Account,
        ForeignKey("Account"),
        comment="The account (if any) the charge was made on behalf of for charges associated with the schedule's subscription. See the Connect documentation for details",
        nullable=True,
    )
    transfer_data = Column(
        Integer,
        ForeignKey("subscription_transfer_data.id"),
        comment="The account (if any) the associated subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SubscriptionSchedulesResourceDefaultSettings(application_fee_percent={application_fee_percent!r}, automatic_tax={automatic_tax!r}, billing_cycle_anchor={billing_cycle_anchor!r}, billing_thresholds={billing_thresholds!r}, collection_method={collection_method!r}, default_payment_method={default_payment_method!r}, description={description!r}, invoice_settings={invoice_settings!r}, on_behalf_of={on_behalf_of!r}, transfer_data={transfer_data!r}, id={id!r})".format(
            application_fee_percent=self.application_fee_percent,
            automatic_tax=self.automatic_tax,
            billing_cycle_anchor=self.billing_cycle_anchor,
            billing_thresholds=self.billing_thresholds,
            collection_method=self.collection_method,
            default_payment_method=self.default_payment_method,
            description=self.description,
            invoice_settings=self.invoice_settings,
            on_behalf_of=self.on_behalf_of,
            transfer_data=self.transfer_data,
            id=self.id,
        )


__all__ = ["subscription_schedules_resource_default_settings"]
