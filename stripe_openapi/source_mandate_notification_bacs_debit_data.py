from sqlalchemy import Column, Identity, Integer, String

from . import Base


class SourceMandateNotificationBacsDebitData(Base):
    __tablename__ = "source_mandate_notification_bacs_debit_data"
    last4 = Column(
        String,
        comment="Last 4 digits of the account number associated with the debit",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return (
            "SourceMandateNotificationBacsDebitData(last4={last4!r}, id={id!r})".format(
                last4=self.last4, id=self.id
            )
        )


__all__ = ["source_mandate_notification_bacs_debit_data"]
