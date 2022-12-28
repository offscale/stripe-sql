from sqlalchemy import Column, Integer, String

class Payment_Method_Details_Klarna(Base):
    __tablename__ = 'payment_method_details_klarna'
    payment_method_category = Column(String, comment='The Klarna payment method used for this transaction.\nCan be one of `pay_later`, `pay_now`, `pay_with_financing`, or `pay_in_installments`', nullable=True)
    preferred_locale = Column(String, comment='Preferred language of the Klarna authorization page that the customer is redirected to.\nCan be one of `de-AT`, `en-AT`, `nl-BE`, `fr-BE`, `en-BE`, `de-DE`, `en-DE`, `da-DK`, `en-DK`, `es-ES`, `en-ES`, `fi-FI`, `sv-FI`, `en-FI`, `en-GB`, `en-IE`, `it-IT`, `en-IT`, `nl-NL`, `en-NL`, `nb-NO`, `en-NO`, `sv-SE`, `en-SE`, `en-US`, `es-US`, `fr-FR`, `en-FR`, `en-AU`, `en-NZ`, `en-CA`, `fr-CA`, `pl-PL`, `en-PL`, `pt-PT`, `en-PT`, `de-CH`, `fr-CH`, `it-CH`, or `en-CH`', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Klarna(payment_method_category={payment_method_category!r}, preferred_locale={preferred_locale!r}, id={id!r})'.format(payment_method_category=self.payment_method_category, preferred_locale=self.preferred_locale, id=self.id)
__all__ = ['payment_method_details_klarna']