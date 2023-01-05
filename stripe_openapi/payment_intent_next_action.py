from sqlalchemy import Column, String


class Payment_Intent_Next_Action(Base):
    __tablename__ = "payment_intent_next_action"
    alipay_handle_redirect = Column(
        PaymentIntentNextActionAlipayHandleRedirect, nullable=True
    )
    boleto_display_details = Column(PaymentIntentNextActionBoleto, nullable=True)
    card_await_notification = Column(
        PaymentIntentNextActionCardAwaitNotification, nullable=True
    )
    display_bank_transfer_instructions = Column(
        PaymentIntentNextActionDisplayBankTransferInstructions, nullable=True
    )
    konbini_display_details = Column(PaymentIntentNextActionKonbini, nullable=True)
    oxxo_display_details = Column(
        PaymentIntentNextActionDisplayOxxoDetails, nullable=True
    )
    paynow_display_qr_code = Column(
        PaymentIntentNextActionPaynowDisplayQrCode, nullable=True
    )
    pix_display_qr_code = Column(PaymentIntentNextActionPixDisplayQrCode, nullable=True)
    promptpay_display_qr_code = Column(
        PaymentIntentNextActionPromptpayDisplayQrCode, nullable=True
    )
    redirect_to_url = Column(PaymentIntentNextActionRedirectToUrl, nullable=True)
    type = Column(
        String,
        comment="Type of the next action to perform, one of `redirect_to_url`, `use_stripe_sdk`, `alipay_handle_redirect`, `oxxo_display_details`, or `verify_with_microdeposits`",
    )
    use_stripe_sdk = Column(
        JSON,
        comment="When confirming a PaymentIntent with Stripe.js, Stripe.js depends on the contents of this dictionary to invoke authentication flows. The shape of the contents is subject to change and is only intended to be used by Stripe.js",
        nullable=True,
    )
    verify_with_microdeposits = Column(
        PaymentIntentNextActionVerifyWithMicrodeposits, nullable=True
    )
    wechat_pay_display_qr_code = Column(
        PaymentIntentNextActionWechatPayDisplayQrCode, nullable=True
    )
    wechat_pay_redirect_to_android_app = Column(
        PaymentIntentNextActionWechatPayRedirectToAndroidApp,
        nullable=True,
        primary_key=True,
    )
    wechat_pay_redirect_to_ios_app = Column(
        PaymentIntentNextActionWechatPayRedirectToIosApp, nullable=True
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Intent_Next_Action(alipay_handle_redirect={alipay_handle_redirect!r}, boleto_display_details={boleto_display_details!r}, card_await_notification={card_await_notification!r}, display_bank_transfer_instructions={display_bank_transfer_instructions!r}, konbini_display_details={konbini_display_details!r}, oxxo_display_details={oxxo_display_details!r}, paynow_display_qr_code={paynow_display_qr_code!r}, pix_display_qr_code={pix_display_qr_code!r}, promptpay_display_qr_code={promptpay_display_qr_code!r}, redirect_to_url={redirect_to_url!r}, type={type!r}, use_stripe_sdk={use_stripe_sdk!r}, verify_with_microdeposits={verify_with_microdeposits!r}, wechat_pay_display_qr_code={wechat_pay_display_qr_code!r}, wechat_pay_redirect_to_android_app={wechat_pay_redirect_to_android_app!r}, wechat_pay_redirect_to_ios_app={wechat_pay_redirect_to_ios_app!r})".format(
            alipay_handle_redirect=self.alipay_handle_redirect,
            boleto_display_details=self.boleto_display_details,
            card_await_notification=self.card_await_notification,
            display_bank_transfer_instructions=self.display_bank_transfer_instructions,
            konbini_display_details=self.konbini_display_details,
            oxxo_display_details=self.oxxo_display_details,
            paynow_display_qr_code=self.paynow_display_qr_code,
            pix_display_qr_code=self.pix_display_qr_code,
            promptpay_display_qr_code=self.promptpay_display_qr_code,
            redirect_to_url=self.redirect_to_url,
            type=self.type,
            use_stripe_sdk=self.use_stripe_sdk,
            verify_with_microdeposits=self.verify_with_microdeposits,
            wechat_pay_display_qr_code=self.wechat_pay_display_qr_code,
            wechat_pay_redirect_to_android_app=self.wechat_pay_redirect_to_android_app,
            wechat_pay_redirect_to_ios_app=self.wechat_pay_redirect_to_ios_app,
        )


__all__ = ["payment_intent_next_action"]
