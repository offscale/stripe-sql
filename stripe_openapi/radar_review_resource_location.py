from sqlalchemy import Column, Float, Integer, String

class Radar_Review_Resource_Location(Base):
    __tablename__ = 'radar_review_resource_location'
    city = Column(String, comment='The city where the payment originated', nullable=True)
    country = Column(String, comment='Two-letter ISO code representing the country where the payment originated', nullable=True)
    latitude = Column(Float, comment='The geographic latitude where the payment originated', nullable=True)
    longitude = Column(Float, comment='The geographic longitude where the payment originated', nullable=True)
    region = Column(String, comment='The state/county/province/region where the payment originated', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Radar_Review_Resource_Location(city={city!r}, country={country!r}, latitude={latitude!r}, longitude={longitude!r}, region={region!r}, id={id!r})'.format(city=self.city, country=self.country, latitude=self.latitude, longitude=self.longitude, region=self.region, id=self.id)
__all__ = ['radar_review_resource_location']