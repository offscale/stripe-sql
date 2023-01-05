from sqlalchemy import Column, String


class Source_Type_Acss_Debit(Base):
    __tablename__ = "source_type_acss_debit"
    bank_address_city = Column(String, nullable=True)
    bank_address_line_1 = Column(String, nullable=True)
    bank_address_line_2 = Column(String, nullable=True)
    bank_address_postal_code = Column(String, nullable=True)
    bank_name = Column(String, nullable=True, primary_key=True)
    category = Column(String, nullable=True)
    country = Column(String, nullable=True)
    fingerprint = Column(String, nullable=True)
    last4 = Column(String, nullable=True)
    routing_number = Column(String, nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source_Type_Acss_Debit(bank_address_city={bank_address_city!r}, bank_address_line_1={bank_address_line_1!r}, bank_address_line_2={bank_address_line_2!r}, bank_address_postal_code={bank_address_postal_code!r}, bank_name={bank_name!r}, category={category!r}, country={country!r}, fingerprint={fingerprint!r}, last4={last4!r}, routing_number={routing_number!r})".format(
            bank_address_city=self.bank_address_city,
            bank_address_line_1=self.bank_address_line_1,
            bank_address_line_2=self.bank_address_line_2,
            bank_address_postal_code=self.bank_address_postal_code,
            bank_name=self.bank_name,
            category=self.category,
            country=self.country,
            fingerprint=self.fingerprint,
            last4=self.last4,
            routing_number=self.routing_number,
        )


__all__ = ["source_type_acss_debit"]
