"""
----------------------------------------------------------------------------------------------------
Written by:
  - Yovany Dominico Girón (y.dominico.giron@elprat.cat)

for Ajuntament del Prat de Llobregat
----------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------
"""
import traceback
from abc import ABC

from sqlalchemy.orm import Session

from nomenclators_archetype.domain.exceptions import RequiredElementError
from nomenclators_archetype.domain.repository.commons import RepositoryOperationError


class UnitOfWorkIsolatedSession(ABC):
    """UnitOfWork class for database transactions with isolated session"""

    def __init__(self, session_factory: callable):  # type: ignore
        self._session_factory = session_factory
        self.session = None

    def __enter__(self):
        self.session = self._session_factory()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        Close the session and manager commit or rollback transaction

        :param exc_type: Exception type if occurs an exception
        :param exc_value: Exception value
        :param exc_traceback: Traceback of the exception
        """

        if exc_type is None:
            self.session.commit()  # type: ignore
        else:
            error_message = "".join(traceback.format_exception(
                exc_type, exc_value, exc_traceback))
            self.session.rollback()  # type: ignore
            if isinstance(exc_value, RequiredElementError):
                raise exc_value
            else:
                raise RepositoryOperationError(
                    f"Repository operation error: {exc_value}\nTraceback:\n{error_message}.") from exc_value
        self.session.close()  # type: ignore

    def commit(self):
        """Force the commit over the transaction"""
        if self.session:
            self.session.commit()

    def rollback(self):
        """Force the rollback over the transaction"""
        if self.session:
            self.session.rollback()


class UnitOfWorkSharedSession(ABC):
    """UnitOfWork class for database transactions with shared session"""

    def __init__(self, db_session: Session):  # type: ignore
        self.session = db_session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        Close the session and manager commit or rollback transaction

        :param exc_type: Exception type if occurs an exception
        :param exc_value: Exception value
        :param exc_traceback: Traceback of the exception
        """

        try:
            if exc_type is None:
                self.session.commit()
            else:
                error_message = "".join(traceback.format_exception(
                    exc_type, exc_value, exc_traceback))
                self.session.rollback()  # type: ignore
                raise RepositoryOperationError(
                    f"Repository operation error: {exc_value}\nTraceback:\n{error_message}.") from exc_value
        finally:
            self.session.close()

    def commit(self):
        """Force the commit over the transaction"""
        if self.session:
            self.session.commit()

    def rollback(self):
        """Force the rollback over the transaction"""
        if self.session:
            self.session.rollback()
