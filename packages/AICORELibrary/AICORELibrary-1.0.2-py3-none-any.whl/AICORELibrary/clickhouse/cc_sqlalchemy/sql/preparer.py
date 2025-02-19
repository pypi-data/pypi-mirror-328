from sqlalchemy.sql.compiler import IdentifierPreparer

from AICORELibrary.clickhouse.driver.query import quote_identifier


class ChIdentifierPreparer(IdentifierPreparer):

    quote_identifier = staticmethod(quote_identifier)

    def _requires_quotes(self, _value):
        return True
