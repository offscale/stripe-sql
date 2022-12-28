from sqlalchemy import Column, Integer, String

class Payment_Pages_Checkout_Session_Custom_Text_Position(Base):
    __tablename__ = 'payment_pages_checkout_session_custom_text_position'
    message = Column(String, comment='Text may be up to 500 characters in length')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Pages_Checkout_Session_Custom_Text_Position(message={message!r}, id={id!r})'.format(message=self.message, id=self.id)
__all__ = ['payment_pages_checkout_session_custom_text_position']