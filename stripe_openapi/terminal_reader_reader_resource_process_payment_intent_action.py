from sqlalchemy import Column, Integer


class Terminal_Reader_Reader_Resource_Process_Payment_Intent_Action(Base):
    """
    Represents a reader action to process a payment intent
    """

    __tablename__ = "terminal_reader_reader_resource_process_payment_intent_action"
    payment_intent = Column(
        PaymentIntent, comment="Most recent PaymentIntent processed by the reader"
    )
    process_config = Column(TerminalReaderReaderResourceProcessConfig, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Terminal_Reader_Reader_Resource_Process_Payment_Intent_Action(payment_intent={payment_intent!r}, process_config={process_config!r}, id={id!r})".format(
            payment_intent=self.payment_intent,
            process_config=self.process_config,
            id=self.id,
        )


__all__ = ["terminal_reader_reader_resource_process_payment_intent_action"]
