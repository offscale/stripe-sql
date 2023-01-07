from sqlalchemy import Column, Integer, String


class Api_Errors(Base):
    __tablename__ = "api_errors"
    charge = Column(
        String, comment="For card errors, the ID of the failed charge", nullable=True
    )
    code = Column(
        String,
        comment="For some errors that could be handled programmatically, a short string indicating the [error code](https://stripe.com/docs/error-codes) reported",
        nullable=True,
    )
    decline_code = Column(
        String,
        comment="For card errors resulting from a card issuer decline, a short string indicating the [card issuer's reason for the decline](https://stripe.com/docs/declines#issuer-declines) if they provide one",
        nullable=True,
    )
    doc_url = Column(
        String,
        comment="A URL to more information about the [error code](https://stripe.com/docs/error-codes) reported",
        nullable=True,
    )
    message = Column(
        String,
        comment="A human-readable message providing more details about the error. For card errors, these messages can be shown to your users",
        nullable=True,
    )
    param = Column(
        String,
        comment="If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field",
        nullable=True,
    )
    payment_intent = Column(payment_intent, ForeignKey("payment_intent"), nullable=True)
    payment_method = Column(payment_method, ForeignKey("payment_method"), nullable=True)
    payment_method_type = Column(
        String,
        comment="If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors",
        nullable=True,
    )
    request_log_url = Column(
        String,
        comment="A URL to the request log entry in your dashboard",
        nullable=True,
    )
    setup_intent = Column(setup_intent, ForeignKey("setup_intent"), nullable=True)
    source = Column(payment_source, ForeignKey("payment_source"), nullable=True)
    type = Column(
        String,
        comment="The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Api_Errors(charge={charge!r}, code={code!r}, decline_code={decline_code!r}, doc_url={doc_url!r}, message={message!r}, param={param!r}, payment_intent={payment_intent!r}, payment_method={payment_method!r}, payment_method_type={payment_method_type!r}, request_log_url={request_log_url!r}, setup_intent={setup_intent!r}, source={source!r}, type={type!r}, id={id!r})".format(
            charge=self.charge,
            code=self.code,
            decline_code=self.decline_code,
            doc_url=self.doc_url,
            message=self.message,
            param=self.param,
            payment_intent=self.payment_intent,
            payment_method=self.payment_method,
            payment_method_type=self.payment_method_type,
            request_log_url=self.request_log_url,
            setup_intent=self.setup_intent,
            source=self.source,
            type=self.type,
            id=self.id,
        )


__all__ = ["api_errors"]
