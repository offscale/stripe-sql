from sqlalchemy import Column, Identity, Integer, String

from . import Base


class SourceMandateNotificationAcssDebitData(Base):
    __tablename__ = "source_mandate_notification_acss_debit_data"
    statement_descriptor = Column(
        String,
        comment="The statement descriptor associate with the debit",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceMandateNotificationAcssDebitData(statement_descriptor={statement_descriptor!r}, id={id!r})".format(
            statement_descriptor=self.statement_descriptor, id=self.id
        )


__all__ = ["source_mandate_notification_acss_debit_data"]
