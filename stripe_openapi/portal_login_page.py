from sqlalchemy import Boolean, Column, Integer, String

class Portal_Login_Page(Base):
    __tablename__ = 'portal_login_page'
    enabled = Column(Boolean, comment='If `true`, a shareable `url` will be generated that will take your customers to a hosted login page for the customer portal.\n\nIf `false`, the previously generated `url`, if any, will be deactivated')
    url = Column(String, comment='A shareable URL to the hosted portal login page. Your customers will be able to log in with their [email](https://stripe.com/docs/api/customers/object#customer_object-email) and receive a link to their customer portal', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Portal_Login_Page(enabled={enabled!r}, url={url!r}, id={id!r})'.format(enabled=self.enabled, url=self.url, id=self.id)
__all__ = ['portal_login_page']