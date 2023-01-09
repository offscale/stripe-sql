from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, String, list

from . import Base


class Balance(Base):
    """
    This is an object representing your Stripe balance. You can retrieve it to see

    the balance currently on your Stripe account.

    You can also retrieve the balance history, which contains a list of
    [transactions](https://stripe.com/docs/reporting/balance-transaction-types) that contributed to the balance
    (charges, payouts, and so forth).

    The available and pending amounts for each currency are broken down further by
    payment source types.

    Related guide: [Understanding Connect Account Balances](https://stripe.com/docs/connect/account-balances).

    """

    __tablename__ = "balance"
    available = Column(
        list,
        comment="Funds that are available to be transferred or paid out, whether automatically by Stripe or explicitly via the [Transfers API](https://stripe.com/docs/api#transfers) or [Payouts API](https://stripe.com/docs/api#payouts). The available balance for each currency and payment type can be found in the `source_types` property",
    )
    connect_reserved = Column(
        list,
        comment="Funds held due to negative balances on connected Custom accounts. The connect reserve balance for each currency and payment type can be found in the `source_types` property",
        nullable=True,
    )
    instant_available = Column(
        list, comment="Funds that can be paid out using Instant Payouts", nullable=True
    )
    issuing = Column(Integer, ForeignKey("balance_detail.id"), nullable=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    pending = Column(
        list,
        comment="Funds that are not yet available in the balance, due to the 7-day rolling pay cycle. The pending balance for each currency, and for each payment type, can be found in the `source_types` property",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Balance(available={available!r}, connect_reserved={connect_reserved!r}, instant_available={instant_available!r}, issuing={issuing!r}, livemode={livemode!r}, object={object!r}, pending={pending!r}, id={id!r})".format(
            available=self.available,
            connect_reserved=self.connect_reserved,
            instant_available=self.instant_available,
            issuing=self.issuing,
            livemode=self.livemode,
            object=self.object,
            pending=self.pending,
            id=self.id,
        )


__all__ = ["balance"]
