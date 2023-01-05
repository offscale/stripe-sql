from sqlalchemy import Column, Integer


class Account_Requirements_Alternative(Base):
    __tablename__ = "account_requirements_alternative"
    alternative_fields_due = Column(
        ARRAY(String),
        comment="Fields that can be provided to satisfy all fields in `original_fields_due`",
    )
    original_fields_due = Column(
        ARRAY(String),
        comment="Fields that are due and can be satisfied by providing all fields in `alternative_fields_due`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Account_Requirements_Alternative(alternative_fields_due={alternative_fields_due!r}, original_fields_due={original_fields_due!r}, id={id!r})".format(
            alternative_fields_due=self.alternative_fields_due,
            original_fields_due=self.original_fields_due,
            id=self.id,
        )


__all__ = ["account_requirements_alternative"]
