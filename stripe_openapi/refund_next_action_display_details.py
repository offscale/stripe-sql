from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class RefundNextActionDisplayDetails(Base):
    __tablename__ = "refund_next_action_display_details"
    email_sent = Column(Integer, ForeignKey("email_sent.id"))
    expires_at = Column(Integer, comment="The expiry timestamp")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "RefundNextActionDisplayDetails(email_sent={email_sent!r}, expires_at={expires_at!r}, id={id!r})".format(
            email_sent=self.email_sent, expires_at=self.expires_at, id=self.id
        )


__all__ = ["refund_next_action_display_details"]
