from sqlalchemy import Column, Integer, String


class Invoice_Setting_Custom_Field(Base):
    __tablename__ = "invoice_setting_custom_field"
    name = Column(String, comment="The name of the custom field")
    value = Column(String, comment="The value of the custom field")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoice_Setting_Custom_Field(name={name!r}, value={value!r}, id={id!r})".format(
            name=self.name, value=self.value, id=self.id
        )


__all__ = ["invoice_setting_custom_field"]
