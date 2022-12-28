from sqlalchemy import Column, Integer

class Gelato_Report_Id_Number_Options(Base):
    __tablename__ = 'gelato_report_id_number_options'
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Gelato_Report_Id_Number_Options(id={id!r})'.format(id=self.id)
__all__ = ['gelato_report_id_number_options']