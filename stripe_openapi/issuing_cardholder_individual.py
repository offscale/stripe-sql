from sqlalchemy import Column, Integer, String


class Issuing_Cardholder_Individual(Base):
    __tablename__ = "issuing_cardholder_individual"
    dob = Column(
        issuing_cardholder_individual_dob,
        comment="[[FK(issuing_cardholder_individual_dob)]] The date of birth of this cardholder",
        nullable=True,
    )
    first_name = Column(String, comment="The first name of this cardholder")
    last_name = Column(String, comment="The last name of this cardholder")
    verification = Column(
        issuing_cardholder_verification,
        comment="[[FK(issuing_cardholder_verification)]] Government-issued ID document for this cardholder",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Cardholder_Individual(dob={dob!r}, first_name={first_name!r}, last_name={last_name!r}, verification={verification!r}, id={id!r})".format(
            dob=self.dob,
            first_name=self.first_name,
            last_name=self.last_name,
            verification=self.verification,
            id=self.id,
        )


__all__ = ["issuing_cardholder_individual"]
