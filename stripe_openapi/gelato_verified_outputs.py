from sqlalchemy import Column, Integer, String


class Gelato_Verified_Outputs(Base):
    __tablename__ = "gelato_verified_outputs"
    address = Column(
        address, comment="[[FK(address)]] The user's verified address", nullable=True
    )
    dob = Column(
        gelato_data_verified_outputs_date,
        comment="[[FK(gelato_data_verified_outputs_date)]] The user’s verified date of birth",
        nullable=True,
    )
    first_name = Column(String, comment="The user's verified first name", nullable=True)
    id_number = Column(String, comment="The user's verified id number", nullable=True)
    id_number_type = Column(
        String, comment="The user's verified id number type", nullable=True
    )
    last_name = Column(String, comment="The user's verified last name", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Gelato_Verified_Outputs(address={address!r}, dob={dob!r}, first_name={first_name!r}, id_number={id_number!r}, id_number_type={id_number_type!r}, last_name={last_name!r}, id={id!r})".format(
            address=self.address,
            dob=self.dob,
            first_name=self.first_name,
            id_number=self.id_number,
            id_number_type=self.id_number_type,
            last_name=self.last_name,
            id=self.id,
        )


__all__ = ["gelato_verified_outputs"]
