from sqlalchemy import Boolean, Column, Integer, String

class Issuing_Transaction_Flight_Data_Leg(Base):
    __tablename__ = 'issuing_transaction_flight_data_leg'
    arrival_airport_code = Column(String, comment="The three-letter IATA airport code of the flight's destination", nullable=True)
    carrier = Column(String, comment='The airline carrier code', nullable=True)
    departure_airport_code = Column(String, comment='The three-letter IATA airport code that the flight departed from', nullable=True)
    flight_number = Column(String, comment='The flight number', nullable=True)
    service_class = Column(String, comment="The flight's service class", nullable=True)
    stopover_allowed = Column(Boolean, comment='Whether a stopover is allowed on this flight', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Issuing_Transaction_Flight_Data_Leg(arrival_airport_code={arrival_airport_code!r}, carrier={carrier!r}, departure_airport_code={departure_airport_code!r}, flight_number={flight_number!r}, service_class={service_class!r}, stopover_allowed={stopover_allowed!r}, id={id!r})'.format(arrival_airport_code=self.arrival_airport_code, carrier=self.carrier, departure_airport_code=self.departure_airport_code, flight_number=self.flight_number, service_class=self.service_class, stopover_allowed=self.stopover_allowed, id=self.id)
__all__ = ['issuing_transaction_flight_data_leg']