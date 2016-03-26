""" run with

python setup.py install; nosetests -v --nocapture tests/cm_basic/test_tables.py:Test_tables.test_001

nosetests -v --nocapture tests/cm_basic/test_tables.py

or

nosetests -v tests/cm_basic/test_tables.py

"""

from cloudmesh_client.util import HEADING

from cloudmesh_client.common.Printer import dict_printer
from pprint import pprint


# noinspection PyPep8Naming
class Test_tables:
    """define tests for dict printer so you test
    yaml
    json
    table
    csv
    dict
    printing
    """

    def setup(self):
        self.d = {
            "a:": {
                "id": "a",
                "x": 1,
                "y": 2,
            },
            "b:": {
                "id": "b",
                "x": 3,
                "y": 4,
            },
        }

    # noinspection PyPep8Naming
    def tearDown(self):
        pass

    def test_001_yaml(self):
        HEADING("dict_printer of a yaml object")
        output = dict_printer(self.d, order=None, header=None, output="yaml", sort_keys=True)
        print(output)
        assert ":" in output

    def test_002_json(self):
        HEADING("dict_printer of a json object")
        output = dict_printer(self.d, order=None, header=None, output="json", sort_keys=True)
        print(output)
        assert "{" in output

    def test_003_table(self):
        HEADING("dict_printer of a table object")
        output = dict_printer(self.d, order=None, header=None, output="table", sort_keys=True)
        print(output)
        assert "id" in str(output)

    def test_004_dict(self):
        HEADING("dict_printer of a dict object")
        output = dict(dict_printer(self.d, order=None, header=None, output="dict", sort_keys=True))
        pprint(output)
        assert "id" in str(output)

    def test_005_csv(self):
        HEADING("dict_printer of a csv object")
        output = dict_printer(self.d, order=None, header=None, output="csv", sort_keys=True)
        print(output)
        assert "id" in str(output)
