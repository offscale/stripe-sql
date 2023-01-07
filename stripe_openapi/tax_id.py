from sqlalchemy import Boolean, Column, Integer, String


class Tax_Id(Base):
    """
    You can add one or multiple tax IDs to a [customer](https://stripe.com/docs/api/customers).

    A customer's tax IDs are displayed on invoices and credit notes issued for the customer.

    Related guide: [Customer Tax Identification Numbers](https://stripe.com/docs/billing/taxes/tax-ids).

    """

    __tablename__ = "tax_id"
    country = Column(
        String,
        comment="Two-letter ISO code representing the country of the tax ID",
        nullable=True,
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    customer = Column(
        customer, comment="[[FK(customer)]] ID of the customer", nullable=True
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    type = Column(
        String,
        comment="Type of the tax ID, one of `ae_trn`, `au_abn`, `au_arn`, `bg_uic`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `nz_gst`, `ph_tin`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, or `za_vat`. Note that some legacy tax IDs have type `unknown`",
    )
    value = Column(String, comment="Value of the tax ID")
    verification = Column(
        tax_id_verification,
        comment="[[FK(tax_id_verification)]] Tax ID verification information",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Tax_Id(country={country!r}, created={created!r}, customer={customer!r}, id={id!r}, livemode={livemode!r}, object={object!r}, type={type!r}, value={value!r}, verification={verification!r})".format(
            country=self.country,
            created=self.created,
            customer=self.customer,
            id=self.id,
            livemode=self.livemode,
            object=self.object,
            type=self.type,
            value=self.value,
            verification=self.verification,
        )


__all__ = ["tax_id"]
