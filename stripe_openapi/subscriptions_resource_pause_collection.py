from sqlalchemy import Column, Integer, String


class Subscriptions_Resource_Pause_Collection(Base):
    """
    The Pause Collection settings determine how we will pause collection for this subscription and for how long the subscription

    should be paused.

    """

    __tablename__ = "subscriptions_resource_pause_collection"
    behavior = Column(
        String,
        comment="The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`",
    )
    resumes_at = Column(
        Integer,
        comment="The time after which the subscription will resume collecting payments",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Subscriptions_Resource_Pause_Collection(behavior={behavior!r}, resumes_at={resumes_at!r}, id={id!r})".format(
            behavior=self.behavior, resumes_at=self.resumes_at, id=self.id
        )


__all__ = ["subscriptions_resource_pause_collection"]
