from sqlalchemy import Column, Integer, String

class Issuing_Transaction_Fuel_Data(Base):
    __tablename__ = 'issuing_transaction_fuel_data'
    type = Column(String, comment='The type of fuel that was purchased. One of `diesel`, `unleaded_plus`, `unleaded_regular`, `unleaded_super`, or `other`')
    unit = Column(String, comment='The units for `volume_decimal`. One of `us_gallon` or `liter`')
    unit_cost_decimal = Column(String, comment='The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places')
    volume_decimal = Column(String, comment='The volume of the fuel that was pumped, represented as a decimal string with at most 12 decimal places', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Issuing_Transaction_Fuel_Data(type={type!r}, unit={unit!r}, unit_cost_decimal={unit_cost_decimal!r}, volume_decimal={volume_decimal!r}, id={id!r})'.format(type=self.type, unit=self.unit, unit_cost_decimal=self.unit_cost_decimal, volume_decimal=self.volume_decimal, id=self.id)
__all__ = ['issuing_transaction_fuel_data']