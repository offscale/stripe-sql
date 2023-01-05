from sqlalchemy import Column, Integer, String


class Payment_Intent_Next_Action_Konbini(Base):
    __tablename__ = "payment_intent_next_action_konbini"
    expires_at = Column(
        Integer, comment="The timestamp at which the pending Konbini payment expires"
    )
    hosted_voucher_url = Column(
        String,
        comment="The URL for the Konbini payment instructions page, which allows customers to view and print a Konbini voucher",
        nullable=True,
    )
    stores = Column(PaymentIntentNextActionKonbiniStores)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Intent_Next_Action_Konbini(expires_at={expires_at!r}, hosted_voucher_url={hosted_voucher_url!r}, stores={stores!r}, id={id!r})".format(
            expires_at=self.expires_at,
            hosted_voucher_url=self.hosted_voucher_url,
            stores=self.stores,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_konbini"]
