from sqlalchemy import Boolean, Column, Integer

class Dispute_Evidence_Details(Base):
    __tablename__ = 'dispute_evidence_details'
    due_by = Column(Integer, comment="Date by which evidence must be submitted in order to successfully challenge dispute. Will be null if the customer's bank or credit card company doesn't allow a response for this particular dispute", nullable=True)
    has_evidence = Column(Boolean, comment='Whether evidence has been staged for this dispute')
    past_due = Column(Boolean, comment='Whether the last evidence submission was submitted past the due date. Defaults to `false` if no evidence submissions have occurred. If `true`, then delivery of the latest evidence is *not* guaranteed')
    submission_count = Column(Integer, comment='The number of times evidence has been submitted. Typically, you may only submit evidence once')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Dispute_Evidence_Details(due_by={due_by!r}, has_evidence={has_evidence!r}, past_due={past_due!r}, submission_count={submission_count!r}, id={id!r})'.format(due_by=self.due_by, has_evidence=self.has_evidence, past_due=self.past_due, submission_count=self.submission_count, id=self.id)
__all__ = ['dispute_evidence_details']