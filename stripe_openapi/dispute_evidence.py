from sqlalchemy import Column, Integer, String


class Dispute_Evidence(Base):
    __tablename__ = "dispute_evidence"
    access_activity_log = Column(
        String,
        comment="Any server or activity logs showing proof that the customer accessed or downloaded the purchased digital product. This information should include IP addresses, corresponding timestamps, and any detailed recorded activity",
        nullable=True,
    )
    billing_address = Column(
        String, comment="The billing address provided by the customer", nullable=True
    )
    cancellation_policy = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your subscription cancellation policy, as shown to the customer",
        nullable=True,
    )
    cancellation_policy_disclosure = Column(
        String,
        comment="An explanation of how and when the customer was shown your refund policy prior to purchase",
        nullable=True,
    )
    cancellation_rebuttal = Column(
        String,
        comment="A justification for why the customer's subscription was not canceled",
        nullable=True,
    )
    customer_communication = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any communication with the customer that you feel is relevant to your case. Examples include emails proving that the customer received the product or service, or demonstrating their use of or satisfaction with the product or service",
        nullable=True,
    )
    customer_email_address = Column(
        String, comment="The email address of the customer", nullable=True
    )
    customer_name = Column(String, comment="The name of the customer", nullable=True)
    customer_purchase_ip = Column(
        String,
        comment="The IP address that the customer used when making the purchase",
        nullable=True,
    )
    customer_signature = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A relevant document or contract showing the customer's signature",
        nullable=True,
    )
    duplicate_charge_documentation = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation for the prior charge that can uniquely identify the charge, such as a receipt, shipping label, work order, etc. This document should be paired with a similar document from the disputed payment that proves the two payments are separate",
        nullable=True,
    )
    duplicate_charge_explanation = Column(
        String,
        comment="An explanation of the difference between the disputed charge versus the prior charge that appears to be a duplicate",
        nullable=True,
    )
    duplicate_charge_id = Column(
        String,
        comment="The Stripe ID for the prior charge which appears to be a duplicate of the disputed charge",
        nullable=True,
    )
    product_description = Column(
        String,
        comment="A description of the product or service that was sold",
        nullable=True,
    )
    receipt = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any receipt or message sent to the customer notifying them of the charge",
        nullable=True,
    )
    refund_policy = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your refund policy, as shown to the customer",
        nullable=True,
    )
    refund_policy_disclosure = Column(
        String,
        comment="Documentation demonstrating that the customer was shown your refund policy prior to purchase",
        nullable=True,
    )
    refund_refusal_explanation = Column(
        String,
        comment="A justification for why the customer is not entitled to a refund",
        nullable=True,
    )
    service_date = Column(
        String,
        comment="The date on which the customer received or began receiving the purchased service, in a clear human-readable format",
        nullable=True,
    )
    service_documentation = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a service was provided to the customer. This could include a copy of a signed contract, work order, or other form of written agreement",
        nullable=True,
    )
    shipping_address = Column(
        String,
        comment="The address to which a physical product was shipped. You should try to include as complete address information as possible",
        nullable=True,
    )
    shipping_carrier = Column(
        String,
        comment="The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, please separate them with commas",
        nullable=True,
    )
    shipping_date = Column(
        String,
        comment="The date on which a physical product began its route to the shipping address, in a clear human-readable format",
        nullable=True,
    )
    shipping_documentation = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a product was shipped to the customer at the same address the customer provided to you. This could include a copy of the shipment receipt, shipping label, etc. It should show the customer's full shipping address, if possible",
        nullable=True,
    )
    shipping_tracking_number = Column(
        String,
        comment="The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas",
        nullable=True,
    )
    uncategorized_file = Column(
        file,
        comment="[[FK(file)]] (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any additional evidence or statements",
        nullable=True,
    )
    uncategorized_text = Column(
        String, comment="Any additional evidence or statements", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Dispute_Evidence(access_activity_log={access_activity_log!r}, billing_address={billing_address!r}, cancellation_policy={cancellation_policy!r}, cancellation_policy_disclosure={cancellation_policy_disclosure!r}, cancellation_rebuttal={cancellation_rebuttal!r}, customer_communication={customer_communication!r}, customer_email_address={customer_email_address!r}, customer_name={customer_name!r}, customer_purchase_ip={customer_purchase_ip!r}, customer_signature={customer_signature!r}, duplicate_charge_documentation={duplicate_charge_documentation!r}, duplicate_charge_explanation={duplicate_charge_explanation!r}, duplicate_charge_id={duplicate_charge_id!r}, product_description={product_description!r}, receipt={receipt!r}, refund_policy={refund_policy!r}, refund_policy_disclosure={refund_policy_disclosure!r}, refund_refusal_explanation={refund_refusal_explanation!r}, service_date={service_date!r}, service_documentation={service_documentation!r}, shipping_address={shipping_address!r}, shipping_carrier={shipping_carrier!r}, shipping_date={shipping_date!r}, shipping_documentation={shipping_documentation!r}, shipping_tracking_number={shipping_tracking_number!r}, uncategorized_file={uncategorized_file!r}, uncategorized_text={uncategorized_text!r}, id={id!r})".format(
            access_activity_log=self.access_activity_log,
            billing_address=self.billing_address,
            cancellation_policy=self.cancellation_policy,
            cancellation_policy_disclosure=self.cancellation_policy_disclosure,
            cancellation_rebuttal=self.cancellation_rebuttal,
            customer_communication=self.customer_communication,
            customer_email_address=self.customer_email_address,
            customer_name=self.customer_name,
            customer_purchase_ip=self.customer_purchase_ip,
            customer_signature=self.customer_signature,
            duplicate_charge_documentation=self.duplicate_charge_documentation,
            duplicate_charge_explanation=self.duplicate_charge_explanation,
            duplicate_charge_id=self.duplicate_charge_id,
            product_description=self.product_description,
            receipt=self.receipt,
            refund_policy=self.refund_policy,
            refund_policy_disclosure=self.refund_policy_disclosure,
            refund_refusal_explanation=self.refund_refusal_explanation,
            service_date=self.service_date,
            service_documentation=self.service_documentation,
            shipping_address=self.shipping_address,
            shipping_carrier=self.shipping_carrier,
            shipping_date=self.shipping_date,
            shipping_documentation=self.shipping_documentation,
            shipping_tracking_number=self.shipping_tracking_number,
            uncategorized_file=self.uncategorized_file,
            uncategorized_text=self.uncategorized_text,
            id=self.id,
        )


__all__ = ["dispute_evidence"]
