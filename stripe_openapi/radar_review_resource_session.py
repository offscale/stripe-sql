from sqlalchemy import Column, Integer, String

class Radar_Review_Resource_Session(Base):
    __tablename__ = 'radar_review_resource_session'
    browser = Column(String, comment='The browser used in this browser session (e.g., `Chrome`)', nullable=True)
    device = Column(String, comment='Information about the device used for the browser session (e.g., `Samsung SM-G930T`)', nullable=True)
    platform = Column(String, comment='The platform for the browser session (e.g., `Macintosh`)', nullable=True)
    version = Column(String, comment='The version for the browser session (e.g., `61.0.3163.100`)', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Radar_Review_Resource_Session(browser={browser!r}, device={device!r}, platform={platform!r}, version={version!r}, id={id!r})'.format(browser=self.browser, device=self.device, platform=self.platform, version=self.version, id=self.id)
__all__ = ['radar_review_resource_session']