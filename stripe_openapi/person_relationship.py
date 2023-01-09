from sqlalchemy import Boolean, Column, Float, Identity, Integer, String

from . import Base


class PersonRelationship(Base):
    __tablename__ = "person_relationship"
    director = Column(
        Boolean,
        comment="Whether the person is a director of the account's legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations",
        nullable=True,
    )
    executive = Column(
        Boolean,
        comment="Whether the person has significant responsibility to control, manage, or direct the organization",
        nullable=True,
    )
    owner = Column(
        Boolean,
        comment="Whether the person is an owner of the account’s legal entity",
        nullable=True,
    )
    percent_ownership = Column(
        Float,
        comment="The percent owned by the person of the account's legal entity",
        nullable=True,
    )
    representative = Column(
        Boolean,
        comment="Whether the person is authorized as the primary representative of the account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account",
        nullable=True,
    )
    title = Column(
        String,
        comment="The person's title (e.g., CEO, Support Engineer)",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PersonRelationship(director={director!r}, executive={executive!r}, owner={owner!r}, percent_ownership={percent_ownership!r}, representative={representative!r}, title={title!r}, id={id!r})".format(
            director=self.director,
            executive=self.executive,
            owner=self.owner,
            percent_ownership=self.percent_ownership,
            representative=self.representative,
            title=self.title,
            id=self.id,
        )


__all__ = ["person_relationship"]
