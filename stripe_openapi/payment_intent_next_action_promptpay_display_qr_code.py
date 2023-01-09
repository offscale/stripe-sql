from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentIntentNextActionPromptpayDisplayQrCode(Base):
    __tablename__ = "payment_intent_next_action_promptpay_display_qr_code"
    data = Column(
        String,
        comment="The raw data string used to generate QR code, it should be used together with QR code library",
    )
    hosted_instructions_url = Column(
        String,
        comment="The URL to the hosted PromptPay instructions page, which allows customers to view the PromptPay QR code",
    )
    image_url_png = Column(
        String,
        comment="The PNG path used to render the QR code, can be used as the source in an HTML img tag",
    )
    image_url_svg = Column(
        String,
        comment="The SVG path used to render the QR code, can be used as the source in an HTML img tag",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentIntentNextActionPromptpayDisplayQrCode(data={data!r}, hosted_instructions_url={hosted_instructions_url!r}, image_url_png={image_url_png!r}, image_url_svg={image_url_svg!r}, id={id!r})".format(
            data=self.data,
            hosted_instructions_url=self.hosted_instructions_url,
            image_url_png=self.image_url_png,
            image_url_svg=self.image_url_svg,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_promptpay_display_qr_code"]
