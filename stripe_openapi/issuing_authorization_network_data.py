from sqlalchemy import Column, String

from . import Base


class IssuingAuthorizationNetworkData(Base):
    __tablename__ = "issuing_authorization_network_data"
    acquiring_institution_id = Column(
        String,
        comment="Identifier assigned to the acquirer by the card network. Sometimes this value is not provided by the network; in this case, the value will be `null`",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingAuthorizationNetworkData(acquiring_institution_id={acquiring_institution_id!r})".format(
            acquiring_institution_id=self.acquiring_institution_id
        )


__all__ = ["issuing_authorization_network_data"]
