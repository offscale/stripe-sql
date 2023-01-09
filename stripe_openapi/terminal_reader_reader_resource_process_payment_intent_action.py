from sqlalchemy import Column, ForeignKey, Identity, Integer

from stripe_openapi.payment_intent import PaymentIntent

from . import Base


class TerminalReaderReaderResourceProcessPaymentIntentAction(Base):
    """
    Represents a reader action to process a payment intent
    """

    __tablename__ = "terminal_reader_reader_resource_process_payment_intent_action"
    payment_intent = Column(
        PaymentIntent,
        comment="[[FK(PaymentIntent)]] Most recent PaymentIntent processed by the reader",
    )
    process_config = Column(
        Integer,
        ForeignKey("terminal_reader_reader_resource_process_config.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TerminalReaderReaderResourceProcessPaymentIntentAction(payment_intent={payment_intent!r}, process_config={process_config!r}, id={id!r})".format(
            payment_intent=self.payment_intent,
            process_config=self.process_config,
            id=self.id,
        )


__all__ = ["terminal_reader_reader_resource_process_payment_intent_action"]
