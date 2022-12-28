from sqlalchemy import Column, Integer

class Notification_Event_Data(Base):
    __tablename__ = 'notification_event_data'
    object = Column(JSON, comment='Object containing the API resource relevant to the event. For example, an `invoice.created` event will have a full [invoice object](https://stripe.com/docs/api#invoice_object) as the value of the object key')
    previous_attributes = Column(JSON, comment='Object containing the names of the attributes that have changed, and their previous values (sent along only with *.updated events)', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Notification_Event_Data(object={object!r}, previous_attributes={previous_attributes!r}, id={id!r})'.format(object=self.object, previous_attributes=self.previous_attributes, id=self.id)
__all__ = ['notification_event_data']