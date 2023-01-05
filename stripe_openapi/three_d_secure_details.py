from sqlalchemy import Column, Integer, String


class Three_D_Secure_Details(Base):
    __tablename__ = "three_d_secure_details"
    authentication_flow = Column(
        String,
        comment="For authenticated transactions: how the customer was authenticated by\nthe issuing bank",
        nullable=True,
    )
    result = Column(
        String,
        comment="Indicates the outcome of 3D Secure authentication",
        nullable=True,
    )
    result_reason = Column(
        String,
        comment="Additional information about why 3D Secure succeeded or failed based\non the `result`",
        nullable=True,
    )
    version = Column(
        String, comment="The version of 3D Secure that was used", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Three_D_Secure_Details(authentication_flow={authentication_flow!r}, result={result!r}, result_reason={result_reason!r}, version={version!r}, id={id!r})".format(
            authentication_flow=self.authentication_flow,
            result=self.result,
            result_reason=self.result_reason,
            version=self.version,
            id=self.id,
        )


__all__ = ["three_d_secure_details"]
