from sqlalchemy import Column, Integer, String


class Source_Type_Klarna(Base):
    __tablename__ = "source_type_klarna"
    background_image_url = Column(String, nullable=True)
    client_token = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    locale = Column(String, nullable=True)
    logo_url = Column(String, nullable=True)
    page_title = Column(String, nullable=True)
    pay_later_asset_urls_descriptive = Column(String, nullable=True)
    pay_later_asset_urls_standard = Column(String, nullable=True)
    pay_later_name = Column(String, nullable=True)
    pay_later_redirect_url = Column(String, nullable=True)
    pay_now_asset_urls_descriptive = Column(String, nullable=True)
    pay_now_asset_urls_standard = Column(String, nullable=True)
    pay_now_name = Column(String, nullable=True)
    pay_now_redirect_url = Column(String, nullable=True)
    pay_over_time_asset_urls_descriptive = Column(String, nullable=True)
    pay_over_time_asset_urls_standard = Column(String, nullable=True)
    pay_over_time_name = Column(String, nullable=True)
    pay_over_time_redirect_url = Column(String, nullable=True)
    payment_method_categories = Column(String, nullable=True)
    purchase_country = Column(String, nullable=True)
    purchase_type = Column(String, nullable=True)
    redirect_url = Column(String, nullable=True)
    shipping_delay = Column(Integer, nullable=True)
    shipping_first_name = Column(String, nullable=True)
    shipping_last_name = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source_Type_Klarna(background_image_url={background_image_url!r}, client_token={client_token!r}, first_name={first_name!r}, last_name={last_name!r}, locale={locale!r}, logo_url={logo_url!r}, page_title={page_title!r}, pay_later_asset_urls_descriptive={pay_later_asset_urls_descriptive!r}, pay_later_asset_urls_standard={pay_later_asset_urls_standard!r}, pay_later_name={pay_later_name!r}, pay_later_redirect_url={pay_later_redirect_url!r}, pay_now_asset_urls_descriptive={pay_now_asset_urls_descriptive!r}, pay_now_asset_urls_standard={pay_now_asset_urls_standard!r}, pay_now_name={pay_now_name!r}, pay_now_redirect_url={pay_now_redirect_url!r}, pay_over_time_asset_urls_descriptive={pay_over_time_asset_urls_descriptive!r}, pay_over_time_asset_urls_standard={pay_over_time_asset_urls_standard!r}, pay_over_time_name={pay_over_time_name!r}, pay_over_time_redirect_url={pay_over_time_redirect_url!r}, payment_method_categories={payment_method_categories!r}, purchase_country={purchase_country!r}, purchase_type={purchase_type!r}, redirect_url={redirect_url!r}, shipping_delay={shipping_delay!r}, shipping_first_name={shipping_first_name!r}, shipping_last_name={shipping_last_name!r}, id={id!r})".format(
            background_image_url=self.background_image_url,
            client_token=self.client_token,
            first_name=self.first_name,
            last_name=self.last_name,
            locale=self.locale,
            logo_url=self.logo_url,
            page_title=self.page_title,
            pay_later_asset_urls_descriptive=self.pay_later_asset_urls_descriptive,
            pay_later_asset_urls_standard=self.pay_later_asset_urls_standard,
            pay_later_name=self.pay_later_name,
            pay_later_redirect_url=self.pay_later_redirect_url,
            pay_now_asset_urls_descriptive=self.pay_now_asset_urls_descriptive,
            pay_now_asset_urls_standard=self.pay_now_asset_urls_standard,
            pay_now_name=self.pay_now_name,
            pay_now_redirect_url=self.pay_now_redirect_url,
            pay_over_time_asset_urls_descriptive=self.pay_over_time_asset_urls_descriptive,
            pay_over_time_asset_urls_standard=self.pay_over_time_asset_urls_standard,
            pay_over_time_name=self.pay_over_time_name,
            pay_over_time_redirect_url=self.pay_over_time_redirect_url,
            payment_method_categories=self.payment_method_categories,
            purchase_country=self.purchase_country,
            purchase_type=self.purchase_type,
            redirect_url=self.redirect_url,
            shipping_delay=self.shipping_delay,
            shipping_first_name=self.shipping_first_name,
            shipping_last_name=self.shipping_last_name,
            id=self.id,
        )


__all__ = ["source_type_klarna"]
