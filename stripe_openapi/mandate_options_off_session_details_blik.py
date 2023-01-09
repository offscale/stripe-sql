from sqlalchemy import Column, Identity, Integer, String

from . import Base


class MandateOptionsOffSessionDetailsBlik(Base):
    __tablename__ = "mandate_options_off_session_details_blik"
    amount = Column(Integer, comment="Amount of each recurring payment", nullable=True)
    currency = Column(
        String, comment="Currency of each recurring payment", nullable=True
    )
    interval = Column(
        String, comment="Frequency interval of each recurring payment", nullable=True
    )
    interval_count = Column(
        Integer, comment="Frequency indicator of each recurring payment", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "MandateOptionsOffSessionDetailsBlik(amount={amount!r}, currency={currency!r}, interval={interval!r}, interval_count={interval_count!r}, id={id!r})".format(
            amount=self.amount,
            currency=self.currency,
            interval=self.interval,
            interval_count=self.interval_count,
            id=self.id,
        )


__all__ = ["mandate_options_off_session_details_blik"]
