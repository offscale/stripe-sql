from sqlalchemy import Boolean, Column, Integer, String


class Scheduled_Query_Run(Base):
    """
    If you have [scheduled a Sigma query](https://stripe.com/docs/sigma/scheduled-queries), you'll

    receive a `sigma.scheduled_query_run.created` webhook each time the query
    runs. The webhook contains a `ScheduledQueryRun` object, which you can use to
    retrieve the query results.

    """

    __tablename__ = "scheduled_query_run"
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    data_load_time = Column(
        Integer,
        comment="When the query was run, Sigma contained a snapshot of your Stripe data at this time",
    )
    error = Column(
        sigma_scheduled_query_run_error,
        ForeignKey("sigma_scheduled_query_run_error"),
        nullable=True,
    )
    file = Column(
        file,
        comment="[[FK(file)]] The file object representing the results of the query",
        nullable=True,
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
    result_available_until = Column(
        Integer,
        comment="Time at which the result expires and is no longer available for download",
    )
    sql = Column(String, comment="SQL for the query")
    status = Column(
        String,
        comment="The query's execution status, which will be `completed` for successful runs, and `canceled`, `failed`, or `timed_out` otherwise",
    )
    title = Column(String, comment="Title of the query")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Scheduled_Query_Run(created={created!r}, data_load_time={data_load_time!r}, error={error!r}, file={file!r}, id={id!r}, livemode={livemode!r}, object={object!r}, result_available_until={result_available_until!r}, sql={sql!r}, status={status!r}, title={title!r})".format(
            created=self.created,
            data_load_time=self.data_load_time,
            error=self.error,
            file=self.file,
            id=self.id,
            livemode=self.livemode,
            object=self.object,
            result_available_until=self.result_available_until,
            sql=self.sql,
            status=self.status,
            title=self.title,
        )


__all__ = ["scheduled_query_run"]
