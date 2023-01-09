from sqlalchemy import Column, Identity, Integer, String

from . import Base


class SourceRedirectFlow(Base):
    __tablename__ = "source_redirect_flow"
    failure_reason = Column(
        String,
        comment="The failure reason for the redirect, either `user_abort` (the customer aborted or dropped out of the redirect flow), `declined` (the authentication failed or the transaction was declined), or `processing_error` (the redirect failed due to a technical error). Present only if the redirect status is `failed`",
        nullable=True,
    )
    return_url = Column(
        String,
        comment="The URL you provide to redirect the customer to after they authenticated their payment",
    )
    status = Column(
        String,
        comment="The status of the redirect, either `pending` (ready to be used by your customer to authenticate the transaction), `succeeded` (succesful authentication, cannot be reused) or `not_required` (redirect should not be used) or `failed` (failed authentication, cannot be reused)",
    )
    url = Column(
        String,
        comment="The URL provided to you to redirect a customer to as part of a `redirect` authentication flow",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SourceRedirectFlow(failure_reason={failure_reason!r}, return_url={return_url!r}, status={status!r}, url={url!r}, id={id!r})".format(
            failure_reason=self.failure_reason,
            return_url=self.return_url,
            status=self.status,
            url=self.url,
            id=self.id,
        )


__all__ = ["source_redirect_flow"]
