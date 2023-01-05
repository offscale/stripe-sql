from sqlalchemy import Column, String


class Source_Type_Multibanco(Base):
    __tablename__ = "source_type_multibanco"
    entity = Column(String, nullable=True)
    reference = Column(String, nullable=True)
    refund_account_holder_address_city = Column(String, nullable=True)
    refund_account_holder_address_country = Column(String, nullable=True)
    refund_account_holder_address_line1 = Column(String, nullable=True)
    refund_account_holder_address_line2 = Column(String, nullable=True)
    refund_account_holder_address_postal_code = Column(String, nullable=True)
    refund_account_holder_address_state = Column(String, nullable=True)
    refund_account_holder_name = Column(String, nullable=True, primary_key=True)
    refund_iban = Column(String, nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source_Type_Multibanco(entity={entity!r}, reference={reference!r}, refund_account_holder_address_city={refund_account_holder_address_city!r}, refund_account_holder_address_country={refund_account_holder_address_country!r}, refund_account_holder_address_line1={refund_account_holder_address_line1!r}, refund_account_holder_address_line2={refund_account_holder_address_line2!r}, refund_account_holder_address_postal_code={refund_account_holder_address_postal_code!r}, refund_account_holder_address_state={refund_account_holder_address_state!r}, refund_account_holder_name={refund_account_holder_name!r}, refund_iban={refund_iban!r})".format(
            entity=self.entity,
            reference=self.reference,
            refund_account_holder_address_city=self.refund_account_holder_address_city,
            refund_account_holder_address_country=self.refund_account_holder_address_country,
            refund_account_holder_address_line1=self.refund_account_holder_address_line1,
            refund_account_holder_address_line2=self.refund_account_holder_address_line2,
            refund_account_holder_address_postal_code=self.refund_account_holder_address_postal_code,
            refund_account_holder_address_state=self.refund_account_holder_address_state,
            refund_account_holder_name=self.refund_account_holder_name,
            refund_iban=self.refund_iban,
        )


__all__ = ["source_type_multibanco"]
