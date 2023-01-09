from sqlalchemy import Column, Identity, Integer

from . import Base


class GelatoReportIdNumberOptions(Base):
    __tablename__ = "gelato_report_id_number_options"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "GelatoReportIdNumberOptions(id={id!r})".format(id=self.id)


__all__ = ["gelato_report_id_number_options"]
