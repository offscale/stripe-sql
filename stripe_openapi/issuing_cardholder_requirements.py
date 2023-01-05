from sqlalchemy import Column, Integer, String


class Issuing_Cardholder_Requirements(Base):
    __tablename__ = "issuing_cardholder_requirements"
    disabled_reason = Column(
        String,
        comment="If `disabled_reason` is present, all cards will decline authorizations with `cardholder_verification_required` reason",
        nullable=True,
    )
    past_due = Column(
        ARRAY(String),
        comment="Array of fields that need to be collected in order to verify and re-enable the cardholder",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Cardholder_Requirements(disabled_reason={disabled_reason!r}, past_due={past_due!r}, id={id!r})".format(
            disabled_reason=self.disabled_reason, past_due=self.past_due, id=self.id
        )


__all__ = ["issuing_cardholder_requirements"]
