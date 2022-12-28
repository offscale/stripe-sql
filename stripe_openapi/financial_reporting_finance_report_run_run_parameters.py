from sqlalchemy import Column, Integer, String

class Financial_Reporting_Finance_Report_Run_Run_Parameters(Base):
    __tablename__ = 'financial_reporting_finance_report_run_run_parameters'
    columns = Column(ARRAY(String), comment='The set of output columns requested for inclusion in the report run', nullable=True)
    connected_account = Column(String, comment='Connected account ID by which to filter the report run', nullable=True)
    currency = Column(String, comment='Currency of objects to be included in the report run', nullable=True)
    interval_end = Column(Integer, comment='Ending timestamp of data to be included in the report run (exclusive)', nullable=True)
    interval_start = Column(Integer, comment='Starting timestamp of data to be included in the report run', nullable=True)
    payout = Column(String, comment='Payout ID by which to filter the report run', nullable=True)
    reporting_category = Column(String, comment='Category of balance transactions to be included in the report run', nullable=True)
    timezone = Column(String, comment='Defaults to `Etc/UTC`. The output timezone for all timestamps in the report. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones). Has no effect on `interval_start` or `interval_end`', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Financial_Reporting_Finance_Report_Run_Run_Parameters(columns={columns!r}, connected_account={connected_account!r}, currency={currency!r}, interval_end={interval_end!r}, interval_start={interval_start!r}, payout={payout!r}, reporting_category={reporting_category!r}, timezone={timezone!r}, id={id!r})'.format(columns=self.columns, connected_account=self.connected_account, currency=self.currency, interval_end=self.interval_end, interval_start=self.interval_start, payout=self.payout, reporting_category=self.reporting_category, timezone=self.timezone, id=self.id)
__all__ = ['financial_reporting_finance_report_run_run_parameters']