from sqlalchemy import Column, Identity, Integer, String

from stripe_openapi.setup_intent import SetupIntent

from . import Base


class TerminalReaderReaderResourceProcessSetupIntentAction(Base):
    """
    Represents a reader action to process a setup intent
    """

    __tablename__ = "terminal_reader_reader_resource_process_setup_intent_action"
    generated_card = Column(
        String,
        comment="ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod",
        nullable=True,
    )
    setup_intent = Column(
        SetupIntent,
        comment="[[FK(SetupIntent)]] Most recent SetupIntent processed by the reader",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TerminalReaderReaderResourceProcessSetupIntentAction(generated_card={generated_card!r}, setup_intent={setup_intent!r}, id={id!r})".format(
            generated_card=self.generated_card,
            setup_intent=self.setup_intent,
            id=self.id,
        )


__all__ = ["terminal_reader_reader_resource_process_setup_intent_action"]
