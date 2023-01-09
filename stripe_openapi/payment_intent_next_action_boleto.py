from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentIntentNextActionBoleto(Base):
    __tablename__ = "payment_intent_next_action_boleto"
    expires_at = Column(
        Integer, comment="The timestamp after which the boleto expires", nullable=True
    )
    hosted_voucher_url = Column(
        String,
        comment="The URL to the hosted boleto voucher page, which allows customers to view the boleto voucher",
        nullable=True,
    )
    number = Column(String, comment="The boleto number", nullable=True)
    pdf = Column(
        String, comment="The URL to the downloadable boleto voucher PDF", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentIntentNextActionBoleto(expires_at={expires_at!r}, hosted_voucher_url={hosted_voucher_url!r}, number={number!r}, pdf={pdf!r}, id={id!r})".format(
            expires_at=self.expires_at,
            hosted_voucher_url=self.hosted_voucher_url,
            number=self.number,
            pdf=self.pdf,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_boleto"]
