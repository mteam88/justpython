import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(dirname(abspath(__file__))))) # let python find flaskr

from flaskr.db.dbsqlite import dbsqlite
import pytest

class Testdbsqlite:
    def test_this(self):
        testable_db = dbsqlite()
        tostore = [0,1,"hello"]
        self.recordidfromcreate = testable_db.create(tostore)
        assert isinstance(self.recordidfromcreate, int)
        assert testable_db.read(self.recordidfromcreate) == [0,1,"hello"]
        with pytest.raises(ValueError):
            testable_db.read(self.recordidfromcreate + 1)
        record = testable_db.read(self.recordidfromcreate)
        testable_db.update(self.recordidfromcreate, [1,0,"goodbye"])
        assert testable_db.read(self.recordidfromcreate) == [1,0,"goodbye"]
        assert record == [0,1,"hello"]
        testable_db.delete(self.recordidfromcreate)
        with pytest.raises(ValueError):
            testable_db.read(self.recordidfromcreate)