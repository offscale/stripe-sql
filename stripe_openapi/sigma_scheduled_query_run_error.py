from sqlalchemy import Column, Integer, String


class Sigma_Scheduled_Query_Run_Error(Base):
    __tablename__ = "sigma_scheduled_query_run_error"
    message = Column(String, comment="Information about the run failure")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Sigma_Scheduled_Query_Run_Error(message={message!r}, id={id!r})".format(
            message=self.message, id=self.id
        )


__all__ = ["sigma_scheduled_query_run_error"]
