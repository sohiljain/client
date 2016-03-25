""" run with

python setup.py install; nosetests -v --nocapture  tests/cm_cloud/test_list.py:Test_list.test_001

nosetests -v --nocapture tests/test_list.py

or

nosetests -v tests/test_list.py

"""

from cloudmesh_client.util import banner
from cloudmesh_client.util import HEADING

from cloudmesh_client.common.Shell import Shell
from cloudmesh_client.common.dotdict import dotdict
from cloudmesh_client.default import Default

class Test_list:

    data = dotdict({
        "cloud": Default.get_cloud(),
        "format": "json",
        "fake": "fake",
        "wrong_cloud": "no_cloud",
        "default_key": "my_default_key",
        "default_value": "my_default_value"
    })

    def run(self, command):
        command = command.format(**self.data)
        banner(command, c ="-")
        print (command)
        parameter = command.split(" ")
        shell_command = parameter[0]
        args = parameter[1:]
        result = Shell.execute(shell_command, args)
        print(result)
        return str(result)

    def setup(self):
        pass

    def tearDown(self):
        pass

    def D(self, line):
        return (line.format(**self.data))

    def test_001(self):
        """testing cm list --cloud cloud default"""
        HEADING()

        result = self.run('cm default {default_key}="{default_value}')
        # set default
        result = self.run("cm default list --cloud={cloud}")
        assert self.D("{default}") in result

        result = self.run("cm list --cloud={cloud} {default_key}")
        assert self.D("{default_value}") in result

        # delete the default name
        result = self.run("cm default delete {default_key} --cloud={cloud}")

        assert "ok." in result

        return

    def test_002(self):
        """testing cm list --cloud cloud --format json default"""
        HEADING()

        result = self.run("cm default --cloud={cloud} {default_key}={default_value}")
        assert "ok." in result

        result = self.run("cm list --cloud={cloud} --format={format} default")
        assert "hallo" in result

        # delete the default name
        result = self.run("cm default delete {default_key} --cloud={cloud}")
        assert "ok." in result

        return

    def test_003(self):
        """testing cm list --cloud trial --user fake default"""
        HEADING()
        banner("cm list --cloud={wrong_cloud} --user={fake} default")

        result = self.run("cm list --cloud={wrong_cloud} --user={fake} default")
        assert "No" in result

        return