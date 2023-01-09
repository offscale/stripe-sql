from sqlalchemy import Column, Identity, Integer, String

from stripe_openapi.gelato_data_id_number_report_date import (
    GelatoDataIdNumberReportDate,
)
from stripe_openapi.gelato_id_number_report_error import GelatoIdNumberReportError

from . import Base


class GelatoIdNumberReport(Base):
    """
    Result from an id_number check
    """

    __tablename__ = "gelato_id_number_report"
    dob = Column(
        GelatoDataIdNumberReportDate,
        comment="[[FK(GelatoDataIdNumberReportDate)]] Date of birth",
        nullable=True,
    )
    error = Column(
        GelatoIdNumberReportError,
        comment="[[FK(GelatoIdNumberReportError)]] Details on the verification error. Present when status is `unverified`",
        nullable=True,
    )
    first_name = Column(String, comment="First name", nullable=True)
    id_number = Column(String, comment="ID number", nullable=True)
    id_number_type = Column(String, comment="Type of ID number", nullable=True)
    last_name = Column(String, comment="Last name", nullable=True)
    status = Column(String, comment="Status of this `id_number` check")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "GelatoIdNumberReport(dob={dob!r}, error={error!r}, first_name={first_name!r}, id_number={id_number!r}, id_number_type={id_number_type!r}, last_name={last_name!r}, status={status!r}, id={id!r})".format(
            dob=self.dob,
            error=self.error,
            first_name=self.first_name,
            id_number=self.id_number,
            id_number_type=self.id_number_type,
            last_name=self.last_name,
            status=self.status,
            id=self.id,
        )


__all__ = ["gelato_id_number_report"]
