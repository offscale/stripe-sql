from sqlalchemy import Boolean, Column, Integer, String

class Issuing_Transaction_Flight_Data(Base):
    __tablename__ = 'issuing_transaction_flight_data'
    departure_at = Column(Integer, comment='The time that the flight departed', nullable=True)
    passenger_name = Column(String, comment='The name of the passenger', nullable=True, primary_key=True)
    refundable = Column(Boolean, comment='Whether the ticket is refundable', nullable=True)
    segments = Column(list, comment='The legs of the trip', nullable=True)
    travel_agency = Column(String, comment='The travel agency that issued the ticket', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Issuing_Transaction_Flight_Data(departure_at={departure_at!r}, passenger_name={passenger_name!r}, refundable={refundable!r}, segments={segments!r}, travel_agency={travel_agency!r})'.format(departure_at=self.departure_at, passenger_name=self.passenger_name, refundable=self.refundable, segments=self.segments, travel_agency=self.travel_agency)
__all__ = ['issuing_transaction_flight_data']