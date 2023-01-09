from sqlalchemy import Column, Identity, Integer

from . import Base


class IssuingTransactionLodgingData(Base):
    __tablename__ = "issuing_transaction_lodging_data"
    check_in_at = Column(
        Integer, comment="The time of checking into the lodging", nullable=True
    )
    nights = Column(
        Integer, comment="The number of nights stayed at the lodging", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingTransactionLodgingData(check_in_at={check_in_at!r}, nights={nights!r}, id={id!r})".format(
            check_in_at=self.check_in_at, nights=self.nights, id=self.id
        )


__all__ = ["issuing_transaction_lodging_data"]
