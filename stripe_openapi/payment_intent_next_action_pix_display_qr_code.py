from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentIntentNextActionPixDisplayQrCode(Base):
    __tablename__ = "payment_intent_next_action_pix_display_qr_code"
    data = Column(
        String,
        comment="The raw data string used to generate QR code, it should be used together with QR code library",
        nullable=True,
    )
    expires_at = Column(
        Integer, comment="The date (unix timestamp) when the PIX expires", nullable=True
    )
    hosted_instructions_url = Column(
        String,
        comment="The URL to the hosted pix instructions page, which allows customers to view the pix QR code",
        nullable=True,
    )
    image_url_png = Column(
        String,
        comment="The image_url_png string used to render png QR code",
        nullable=True,
    )
    image_url_svg = Column(
        String,
        comment="The image_url_svg string used to render svg QR code",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentIntentNextActionPixDisplayQrCode(data={data!r}, expires_at={expires_at!r}, hosted_instructions_url={hosted_instructions_url!r}, image_url_png={image_url_png!r}, image_url_svg={image_url_svg!r}, id={id!r})".format(
            data=self.data,
            expires_at=self.expires_at,
            hosted_instructions_url=self.hosted_instructions_url,
            image_url_png=self.image_url_png,
            image_url_svg=self.image_url_svg,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_pix_display_qr_code"]
