from abc import ABC, abstractmethod

class CRUDdbInterface(ABC):
    """
    CRUD database interface
    """
    @abstractmethod
    def create(self, to_save):
        """
        Store/save "to_save." Returns id.
        """
        pass
    @abstractmethod
    def read(self, id):
        """
        Read from database by id. Returns object that was stored with create(<object here>)
        """
        pass
    @abstractmethod
    def update(self, id, field, value):
        """
        Update id:field to value. Should be used sparingly. Returns None.
        """
        pass
    @abstractmethod
    def delete(self, id):
        """
        Delete record by id. Returns None.
        """
        pass