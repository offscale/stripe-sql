from sqlalchemy import Column, Integer


class Treasury_Financial_Accounts_Resource_Status_Details(Base):
    __tablename__ = "treasury_financial_accounts_resource_status_details"
    closed = Column(
        treasury_financial_accounts_resource_closed_status_details,
        comment="[[FK(treasury_financial_accounts_resource_closed_status_details)]] Details related to the closure of this FinancialAccount",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Treasury_Financial_Accounts_Resource_Status_Details(closed={closed!r}, id={id!r})".format(
            closed=self.closed, id=self.id
        )


__all__ = ["treasury_financial_accounts_resource_status_details"]
