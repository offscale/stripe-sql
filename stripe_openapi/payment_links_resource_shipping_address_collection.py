from sqlalchemy import ARRAY, Column, Identity, Integer, String

from . import Base


class PaymentLinksResourceShippingAddressCollection(Base):
    __tablename__ = "payment_links_resource_shipping_address_collection"
    allowed_countries = Column(
        ARRAY(String),
        comment="An array of two-letter ISO country codes representing which countries Checkout should provide as options for shipping locations. Unsupported country codes: `AS, CX, CC, CU, HM, IR, KP, MH, FM, NF, MP, PW, SD, SY, UM, VI`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentLinksResourceShippingAddressCollection(allowed_countries={allowed_countries!r}, id={id!r})".format(
            allowed_countries=self.allowed_countries, id=self.id
        )


__all__ = ["payment_links_resource_shipping_address_collection"]
