from sqlalchemy import Column, String

from . import Base


class PaymentMethodDetailsBoleto(Base):
    __tablename__ = "payment_method_details_boleto"
    tax_id = Column(
        String,
        comment="The tax ID of the customer (CPF for individuals consumers or CNPJ for businesses consumers)",
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodDetailsBoleto(tax_id={tax_id!r})".format(
            tax_id=self.tax_id
        )


__all__ = ["payment_method_details_boleto"]
