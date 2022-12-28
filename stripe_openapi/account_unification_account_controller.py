from sqlalchemy import Boolean, Column, Integer, String

class Account_Unification_Account_Controller(Base):
    __tablename__ = 'account_unification_account_controller'
    is_controller = Column(Boolean, comment='`true` if the Connect application retrieving the resource controls the account and can therefore exercise [platform controls](https://stripe.com/docs/connect/platform-controls-for-standard-accounts). Otherwise, this field is null', nullable=True)
    type = Column(String, comment='The controller type. Can be `application`, if a Connect application controls the account, or `account`, if the account controls itself')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Account_Unification_Account_Controller(is_controller={is_controller!r}, type={type!r}, id={id!r})'.format(is_controller=self.is_controller, type=self.type, id=self.id)
__all__ = ['account_unification_account_controller']