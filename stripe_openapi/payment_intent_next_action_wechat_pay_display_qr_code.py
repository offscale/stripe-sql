from sqlalchemy import Column, Integer, String


class Payment_Intent_Next_Action_Wechat_Pay_Display_Qr_Code(Base):
    __tablename__ = "payment_intent_next_action_wechat_pay_display_qr_code"
    data = Column(String, comment="The data being used to generate QR code")
    hosted_instructions_url = Column(
        String,
        comment="The URL to the hosted WeChat Pay instructions page, which allows customers to view the WeChat Pay QR code",
    )
    image_data_url = Column(
        String, comment="The base64 image data for a pre-generated QR code"
    )
    image_url_png = Column(
        String, comment="The image_url_png string used to render QR code"
    )
    image_url_svg = Column(
        String, comment="The image_url_svg string used to render QR code"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Intent_Next_Action_Wechat_Pay_Display_Qr_Code(data={data!r}, hosted_instructions_url={hosted_instructions_url!r}, image_data_url={image_data_url!r}, image_url_png={image_url_png!r}, image_url_svg={image_url_svg!r}, id={id!r})".format(
            data=self.data,
            hosted_instructions_url=self.hosted_instructions_url,
            image_data_url=self.image_data_url,
            image_url_png=self.image_url_png,
            image_url_svg=self.image_url_svg,
            id=self.id,
        )


__all__ = ["payment_intent_next_action_wechat_pay_display_qr_code"]
