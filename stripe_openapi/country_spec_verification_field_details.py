from sqlalchemy import ARRAY, Column, Identity, Integer, String

from . import Base


class CountrySpecVerificationFieldDetails(Base):
    __tablename__ = "country_spec_verification_field_details"
    additional = Column(
        ARRAY(String),
        comment="Additional fields which are only required for some users",
    )
    minimum = Column(
        ARRAY(String), comment="Fields which every account must eventually provide"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CountrySpecVerificationFieldDetails(additional={additional!r}, minimum={minimum!r}, id={id!r})".format(
            additional=self.additional, minimum=self.minimum, id=self.id
        )


__all__ = ["country_spec_verification_field_details"]
