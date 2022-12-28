from sqlalchemy import Column, Integer, String

class Source_Type_Ach_Credit_Transfer(Base):
    __tablename__ = 'source_type_ach_credit_transfer'
    account_number = Column(String, nullable=True)
    bank_name = Column(String, nullable=True)
    fingerprint = Column(String, nullable=True)
    refund_account_holder_name = Column(String, nullable=True)
    refund_account_holder_type = Column(String, nullable=True)
    refund_routing_number = Column(String, nullable=True)
    routing_number = Column(String, nullable=True)
    swift_code = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Source_Type_Ach_Credit_Transfer(account_number={account_number!r}, bank_name={bank_name!r}, fingerprint={fingerprint!r}, refund_account_holder_name={refund_account_holder_name!r}, refund_account_holder_type={refund_account_holder_type!r}, refund_routing_number={refund_routing_number!r}, routing_number={routing_number!r}, swift_code={swift_code!r}, id={id!r})'.format(account_number=self.account_number, bank_name=self.bank_name, fingerprint=self.fingerprint, refund_account_holder_name=self.refund_account_holder_name, refund_account_holder_type=self.refund_account_holder_type, refund_routing_number=self.refund_routing_number, routing_number=self.routing_number, swift_code=self.swift_code, id=self.id)
__all__ = ['source_type_ach_credit_transfer']