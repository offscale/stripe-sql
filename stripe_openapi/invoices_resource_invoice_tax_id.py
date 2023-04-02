from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

InvoicesResourceInvoiceTaxIdJson = Table(
    "invoices_resource_invoice_tax_idjson",
    metadata,
    Column(
        "type",
        String,
        comment="The type of the tax ID, one of `eu_vat`, `br_cnpj`, `br_cpf`, `eu_oss_vat`, `gb_vat`, `nz_gst`, `au_abn`, `au_arn`, `in_gst`, `no_vat`, `za_vat`, `ch_vat`, `mx_rfc`, `sg_uen`, `ru_inn`, `ru_kpp`, `ca_bn`, `hk_br`, `es_cif`, `tw_vat`, `th_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `li_uid`, `my_itn`, `us_ein`, `kr_brn`, `ca_qst`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `my_sst`, `sg_gst`, `ae_trn`, `cl_tin`, `sa_vat`, `id_npwp`, `my_frp`, `il_vat`, `ge_vat`, `ua_vat`, `is_vat`, `bg_uic`, `hu_tin`, `si_tin`, `ke_pin`, `tr_tin`, `eg_tin`, `ph_tin`, or `unknown`",
    ),
    Column("value", String, comment="The value of the tax ID", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoices_resource_invoice_tax_id.json"]
