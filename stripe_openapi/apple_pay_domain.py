from sqlalchemy import Boolean, Column, Integer, String


class Apple_Pay_Domain(Base):
    __tablename__ = "apple_pay_domain"
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    domain_name = Column(String)
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Apple_Pay_Domain(created={created!r}, domain_name={domain_name!r}, id={id!r}, livemode={livemode!r}, object={object!r})".format(
            created=self.created,
            domain_name=self.domain_name,
            id=self.id,
            livemode=self.livemode,
            object=self.object,
        )


__all__ = ["apple_pay_domain"]
