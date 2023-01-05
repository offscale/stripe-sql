from sqlalchemy import Column, Integer, String


class Source_Code_Verification_Flow(Base):
    __tablename__ = "source_code_verification_flow"
    attempts_remaining = Column(
        Integer,
        comment="The number of attempts remaining to authenticate the source object with a verification code",
    )
    status = Column(
        String,
        comment="The status of the code verification, either `pending` (awaiting verification, `attempts_remaining` should be greater than 0), `succeeded` (successful verification) or `failed` (failed verification, cannot be verified anymore as `attempts_remaining` should be 0)",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source_Code_Verification_Flow(attempts_remaining={attempts_remaining!r}, status={status!r}, id={id!r})".format(
            attempts_remaining=self.attempts_remaining, status=self.status, id=self.id
        )


__all__ = ["source_code_verification_flow"]
