from sqlalchemy import Column, Integer, String


class Invoice_Payment_Method_Options_Card(Base):
    __tablename__ = "invoice_payment_method_options_card"
    installments = Column(InvoiceInstallmentsCard, nullable=True)
    request_three_d_secure = Column(
        String,
        comment="We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoice_Payment_Method_Options_Card(installments={installments!r}, request_three_d_secure={request_three_d_secure!r}, id={id!r})".format(
            installments=self.installments,
            request_three_d_secure=self.request_three_d_secure,
            id=self.id,
        )


__all__ = ["invoice_payment_method_options_card"]
