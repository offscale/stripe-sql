from sqlalchemy import Column, String


class Rule(Base):
    __tablename__ = "rule"
    action = Column(String, comment="The action taken on the payment")
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    predicate = Column(String, comment="The predicate to evaluate the payment against")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Rule(action={action!r}, id={id!r}, predicate={predicate!r})".format(
            action=self.action, id=self.id, predicate=self.predicate
        )


__all__ = ["rule"]
