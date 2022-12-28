from sqlalchemy import Column, Integer, String

class File(Base):
    """
        This is an object representing a file hosted on Stripe's servers. The
    
        file may have been uploaded by yourself using the [create file](https://stripe.com/docs/api#create_file)
        request (for example, when uploading dispute evidence) or it may have
        been created by Stripe (for example, the results of a [Sigma scheduled
        query](#scheduled_queries)).
    
        Related guide: [File Upload Guide](https://stripe.com/docs/file-upload).
    
        """
    __tablename__ = 'file'
    created = Column(Integer, comment='Time at which the object was created. Measured in seconds since the Unix epoch')
    expires_at = Column(Integer, comment='The time at which the file expires and is no longer available in epoch seconds', nullable=True)
    filename = Column(String, comment='A filename for the file, suitable for saving to a filesystem', nullable=True)
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    links = Column(JSON, comment='A list of [file links](https://stripe.com/docs/api#file_links) that point at this file', nullable=True)
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")
    purpose = Column(String, comment='The [purpose](https://stripe.com/docs/file-upload#uploading-a-file) of the uploaded file')
    size = Column(Integer, comment='The size in bytes of the file object')
    title = Column(String, comment='A user friendly title for the document', nullable=True)
    type = Column(String, comment='The type of the file returned (e.g., `csv`, `pdf`, `jpg`, or `png`)', nullable=True)
    url = Column(String, comment='The URL from which the file can be downloaded using your live secret API key', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'File(created={created!r}, expires_at={expires_at!r}, filename={filename!r}, id={id!r}, links={links!r}, object={object!r}, purpose={purpose!r}, size={size!r}, title={title!r}, type={type!r}, url={url!r})'.format(created=self.created, expires_at=self.expires_at, filename=self.filename, id=self.id, links=self.links, object=self.object, purpose=self.purpose, size=self.size, title=self.title, type=self.type, url=self.url)
__all__ = ['file']