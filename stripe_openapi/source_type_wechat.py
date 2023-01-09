from sqlalchemy import Column, String

from . import Base


class SourceTypeWechat(Base):
    __tablename__ = "source_type_wechat"
    prepay_id = Column(String, nullable=True, primary_key=True)
    qr_code_url = Column(String, nullable=True)
    statement_descriptor = Column(String, nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceTypeWechat(prepay_id={prepay_id!r}, qr_code_url={qr_code_url!r}, statement_descriptor={statement_descriptor!r})".format(
            prepay_id=self.prepay_id,
            qr_code_url=self.qr_code_url,
            statement_descriptor=self.statement_descriptor,
        )


__all__ = ["source_type_wechat"]
