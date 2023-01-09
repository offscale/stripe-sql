from sqlalchemy import Column, String

from . import Base


class SourceMandateNotificationSepaDebitData(Base):
    __tablename__ = "source_mandate_notification_sepa_debit_data"
    creditor_identifier = Column(
        String, comment="SEPA creditor ID", nullable=True, primary_key=True
    )
    last4 = Column(
        String,
        comment="Last 4 digits of the account number associated with the debit",
        nullable=True,
    )
    mandate_reference = Column(
        String, comment="Mandate reference associated with the debit", nullable=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceMandateNotificationSepaDebitData(creditor_identifier={creditor_identifier!r}, last4={last4!r}, mandate_reference={mandate_reference!r})".format(
            creditor_identifier=self.creditor_identifier,
            last4=self.last4,
            mandate_reference=self.mandate_reference,
        )


__all__ = ["source_mandate_notification_sepa_debit_data"]
