from sqlalchemy import Column, Identity, Integer, String

from . import Base


class AlternateStatementDescriptors(Base):
    __tablename__ = "alternate_statement_descriptors"
    kana = Column(String, comment="The Kana variation of the descriptor", nullable=True)
    kanji = Column(
        String, comment="The Kanji variation of the descriptor", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AlternateStatementDescriptors(kana={kana!r}, kanji={kanji!r}, id={id!r})".format(
            kana=self.kana, kanji=self.kanji, id=self.id
        )


__all__ = ["alternate_statement_descriptors"]
