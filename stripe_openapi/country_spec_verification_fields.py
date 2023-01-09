from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class CountrySpecVerificationFields(Base):
    __tablename__ = "country_spec_verification_fields"
    company = Column(Integer, ForeignKey("country_spec_verification_field_details.id"))
    individual = Column(
        Integer, ForeignKey("country_spec_verification_field_details.id")
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CountrySpecVerificationFields(company={company!r}, individual={individual!r}, id={id!r})".format(
            company=self.company, individual=self.individual, id=self.id
        )


__all__ = ["country_spec_verification_fields"]
