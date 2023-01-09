from sqlalchemy import Column, Identity, Integer, String

from stripe_openapi.gelato_selfie_report_error import GelatoSelfieReportError

from . import Base


class GelatoSelfieReport(Base):
    """
    Result from a selfie check
    """

    __tablename__ = "gelato_selfie_report"
    document = Column(
        String,
        comment="ID of the [File](https://stripe.com/docs/api/files) holding the image of the identity document used in this check",
        nullable=True,
    )
    error = Column(
        GelatoSelfieReportError,
        comment="[[FK(GelatoSelfieReportError)]] Details on the verification error. Present when status is `unverified`",
        nullable=True,
    )
    selfie = Column(
        String,
        comment="ID of the [File](https://stripe.com/docs/api/files) holding the image of the selfie used in this check",
        nullable=True,
    )
    status = Column(String, comment="Status of this `selfie` check")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "GelatoSelfieReport(document={document!r}, error={error!r}, selfie={selfie!r}, status={status!r}, id={id!r})".format(
            document=self.document,
            error=self.error,
            selfie=self.selfie,
            status=self.status,
            id=self.id,
        )


__all__ = ["gelato_selfie_report"]
