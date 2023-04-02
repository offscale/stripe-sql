from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

FinancialReportingFinanceReportRunRunParametersJson = Table(
    "financial_reporting_finance_report_run_run_parametersjson",
    metadata,
    Column(
        "columns",
        ARRAY(String),
        comment="The set of output columns requested for inclusion in the report run",
        nullable=True,
    ),
    Column(
        "connected_account",
        String,
        comment="Connected account ID by which to filter the report run",
        nullable=True,
    ),
    Column(
        "currency",
        String,
        comment="Currency of objects to be included in the report run",
        nullable=True,
    ),
    Column(
        "interval_end",
        Integer,
        comment="Ending timestamp of data to be included in the report run. Can be any UTC timestamp between 1 second after the user specified `interval_start` and 1 second before this report's last `data_available_end` value",
        nullable=True,
    ),
    Column(
        "interval_start",
        Integer,
        comment="Starting timestamp of data to be included in the report run. Can be any UTC timestamp between 1 second after this report's `data_available_start` and 1 second before the user specified `interval_end` value",
        nullable=True,
    ),
    Column(
        "payout",
        String,
        comment="Payout ID by which to filter the report run",
        nullable=True,
    ),
    Column(
        "reporting_category",
        String,
        comment="Category of balance transactions to be included in the report run",
        nullable=True,
    ),
    Column(
        "timezone",
        String,
        comment="Defaults to `Etc/UTC`. The output timezone for all timestamps in the report. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones). Has no effect on `interval_start` or `interval_end`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["financial_reporting_finance_report_run_run_parameters.json"]
