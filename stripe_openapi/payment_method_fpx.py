from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentMethodFpx(Base):
    __tablename__ = "payment_method_fpx"
    account_holder_type = Column(
        String,
        comment="Account holder type, if provided. Can be one of `individual` or `company`",
        nullable=True,
    )
    bank = Column(
        String,
        comment="The customer's bank, if provided. Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`, `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodFpx(account_holder_type={account_holder_type!r}, bank={bank!r}, id={id!r})".format(
            account_holder_type=self.account_holder_type, bank=self.bank, id=self.id
        )


__all__ = ["payment_method_fpx"]
