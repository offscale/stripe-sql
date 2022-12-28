from sqlalchemy import Column, String

class Account_Dashboard_Settings(Base):
    __tablename__ = 'account_dashboard_settings'
    display_name = Column(String, comment='The display name for this account. This is used on the Stripe Dashboard to differentiate between accounts', nullable=True, primary_key=True)
    timezone = Column(String, comment='The timezone used in the Stripe Dashboard for this account. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones)', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Account_Dashboard_Settings(display_name={display_name!r}, timezone={timezone!r})'.format(display_name=self.display_name, timezone=self.timezone)
__all__ = ['account_dashboard_settings']