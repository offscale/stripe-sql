from sqlalchemy import Column, Integer, String


class Currency_Option(Base):
    __tablename__ = "currency_option"
    custom_unit_amount = Column(
        custom_unit_amount,
        comment="[[FK(custom_unit_amount)]] When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links",
        nullable=True,
    )
    tax_behavior = Column(
        String,
        comment="Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed",
        nullable=True,
    )
    tiers = Column(
        list,
        comment="Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`",
        nullable=True,
    )
    unit_amount = Column(
        Integer,
        comment="The unit amount in %s to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`",
        nullable=True,
    )
    unit_amount_decimal = Column(
        String,
        comment="The unit amount in %s to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Currency_Option(custom_unit_amount={custom_unit_amount!r}, tax_behavior={tax_behavior!r}, tiers={tiers!r}, unit_amount={unit_amount!r}, unit_amount_decimal={unit_amount_decimal!r}, id={id!r})".format(
            custom_unit_amount=self.custom_unit_amount,
            tax_behavior=self.tax_behavior,
            tiers=self.tiers,
            unit_amount=self.unit_amount,
            unit_amount_decimal=self.unit_amount_decimal,
            id=self.id,
        )


__all__ = ["currency_option"]
