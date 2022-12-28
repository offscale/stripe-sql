from sqlalchemy import Column, Integer, String

class Setup_Intent_Payment_Method_Options_Link(Base):
    __tablename__ = 'setup_intent_payment_method_options_link'
    persistent_token = Column(String, comment='Token used for persistent Link logins', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Setup_Intent_Payment_Method_Options_Link(persistent_token={persistent_token!r}, id={id!r})'.format(persistent_token=self.persistent_token, id=self.id)
__all__ = ['setup_intent_payment_method_options_link']