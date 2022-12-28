from sqlalchemy import Column, Integer

class Refund_Next_Action_Display_Details(Base):
    __tablename__ = 'refund_next_action_display_details'
    email_sent = Column(EmailSent)
    expires_at = Column(Integer, comment='The expiry timestamp')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Refund_Next_Action_Display_Details(email_sent={email_sent!r}, expires_at={expires_at!r}, id={id!r})'.format(email_sent=self.email_sent, expires_at=self.expires_at, id=self.id)
__all__ = ['refund_next_action_display_details']