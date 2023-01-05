from sqlalchemy import Boolean, Column, Integer, String


class Source_Type_Three_D_Secure(Base):
    __tablename__ = "source_type_three_d_secure"
    address_line1_check = Column(String, nullable=True)
    address_zip_check = Column(String, nullable=True)
    authenticated = Column(Boolean, nullable=True)
    brand = Column(String, nullable=True)
    card = Column(String, nullable=True)
    country = Column(String, nullable=True)
    customer = Column(String, nullable=True)
    cvc_check = Column(String, nullable=True)
    description = Column(String, nullable=True)
    dynamic_last4 = Column(String, nullable=True)
    exp_month = Column(Integer, nullable=True)
    exp_year = Column(Integer, nullable=True)
    fingerprint = Column(String, nullable=True)
    funding = Column(String, nullable=True)
    iin = Column(String, nullable=True)
    issuer = Column(String, nullable=True)
    last4 = Column(String, nullable=True)
    name = Column(String, nullable=True)
    three_d_secure = Column(String, nullable=True)
    tokenization_method = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source_Type_Three_D_Secure(address_line1_check={address_line1_check!r}, address_zip_check={address_zip_check!r}, authenticated={authenticated!r}, brand={brand!r}, card={card!r}, country={country!r}, customer={customer!r}, cvc_check={cvc_check!r}, description={description!r}, dynamic_last4={dynamic_last4!r}, exp_month={exp_month!r}, exp_year={exp_year!r}, fingerprint={fingerprint!r}, funding={funding!r}, iin={iin!r}, issuer={issuer!r}, last4={last4!r}, name={name!r}, three_d_secure={three_d_secure!r}, tokenization_method={tokenization_method!r}, id={id!r})".format(
            address_line1_check=self.address_line1_check,
            address_zip_check=self.address_zip_check,
            authenticated=self.authenticated,
            brand=self.brand,
            card=self.card,
            country=self.country,
            customer=self.customer,
            cvc_check=self.cvc_check,
            description=self.description,
            dynamic_last4=self.dynamic_last4,
            exp_month=self.exp_month,
            exp_year=self.exp_year,
            fingerprint=self.fingerprint,
            funding=self.funding,
            iin=self.iin,
            issuer=self.issuer,
            last4=self.last4,
            name=self.name,
            three_d_secure=self.three_d_secure,
            tokenization_method=self.tokenization_method,
            id=self.id,
        )


__all__ = ["source_type_three_d_secure"]
