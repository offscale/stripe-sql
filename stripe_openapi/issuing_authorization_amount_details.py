from sqlalchemy import Column, Integer


class Issuing_Authorization_Amount_Details(Base):
    __tablename__ = "issuing_authorization_amount_details"
    atm_fee = Column(
        Integer,
        comment="The fee charged by the ATM for the cash withdrawal",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Authorization_Amount_Details(atm_fee={atm_fee!r}, id={id!r})".format(
            atm_fee=self.atm_fee, id=self.id
        )


__all__ = ["issuing_authorization_amount_details"]
