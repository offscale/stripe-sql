from sqlalchemy import Column, String

from . import Base


class PaymentMethodBoleto(Base):
    __tablename__ = "payment_method_boleto"
    tax_id = Column(
        String,
        comment="Uniquely identifies the customer tax id (CNPJ or CPF)",
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodBoleto(tax_id={tax_id!r})".format(tax_id=self.tax_id)


__all__ = ["payment_method_boleto"]
