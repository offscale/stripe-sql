from sqlalchemy import Column, Integer, String

class Terminal_Reader_Reader_Resource_Reader_Action(Base):
    """
    Represents an action performed by the reader
        """
    __tablename__ = 'terminal_reader_reader_resource_reader_action'
    failure_code = Column(String, comment='Failure code, only set if status is `failed`', nullable=True)
    failure_message = Column(String, comment='Detailed failure message, only set if status is `failed`', nullable=True)
    process_payment_intent = Column(TerminalReaderReaderResourceProcessPaymentIntentAction, nullable=True)
    process_setup_intent = Column(TerminalReaderReaderResourceProcessSetupIntentAction, nullable=True)
    set_reader_display = Column(TerminalReaderReaderResourceSetReaderDisplayAction, nullable=True)
    status = Column(String, comment='Status of the action performed by the reader')
    type = Column(String, comment='Type of action performed by the reader')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Terminal_Reader_Reader_Resource_Reader_Action(failure_code={failure_code!r}, failure_message={failure_message!r}, process_payment_intent={process_payment_intent!r}, process_setup_intent={process_setup_intent!r}, set_reader_display={set_reader_display!r}, status={status!r}, type={type!r}, id={id!r})'.format(failure_code=self.failure_code, failure_message=self.failure_message, process_payment_intent=self.process_payment_intent, process_setup_intent=self.process_setup_intent, set_reader_display=self.set_reader_display, status=self.status, type=self.type, id=self.id)
__all__ = ['terminal_reader_reader_resource_reader_action']