from abc import ABC, abstractmethod

class CRUDdbInterface(ABC):
    """
    CRUD database interface
    """
    @abstractmethod
    def create(self, to_save, recordid=None):
        """
        Store/save "to_save." Returns recordid.
        """
        pass
    @abstractmethod
    def read(self, recordid):
        """
        Read from database by recordid. Returns object that was stored with create(<object here>)
        """
        pass
    @abstractmethod
    def update(self, recordid, value):
        """
        Update recordid to value. Should be used sparingly. Returns None.
        """
        pass
    @abstractmethod
    def delete(self, recordid):
        """
        Delete record by recordid. Returns None.
        """
        pass