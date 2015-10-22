from __future__ import print_function

import cmd
import sys
import traceback
import string
import textwrap

from docopt import docopt
from cloudmesh_client.shell.plugins.RegisterCommand import RegisterCommand
from cloudmesh_client.shell.plugins.NovaCommand import NovaCommand
from cloudmesh_client.shell.plugins.KeyCommand import KeyCommand
from cloudmesh_client.shell.plugins.GroupCommand import GroupCommand
from cloudmesh_client.shell.plugins.SelectCommand import SelectCommand
from cloudmesh_client.shell.plugins.ManCommand import ManCommand
from cloudmesh_client.shell.plugins.TerminalCommands import TerminalCommands
from cloudmesh_client.shell.plugins.OpenCommand import OpenCommand
from cloudmesh_client.shell.plugins.ReservationCommand import ReservationCommand
from cloudmesh_client.shell.plugins.ServerCommand import ServerCommand
from cloudmesh_client.shell.plugins.CloudCommand import CloudCommand
from cloudmesh_client.shell.plugins.SecureShellCommand import SecureShellCommand
from cloudmesh_client.shell.plugins.SecgroupCommand import SecgroupCommand
from cloudmesh_client.shell.plugins.DefaultCommand import DefaultCommand
from cloudmesh_client.shell.plugins.InventoryCommand import InventoryCommand
from cloudmesh_client.shell.plugins.ListCommand import ListCommand
from cloudmesh_client.shell.plugins.QuotaCommand import QuotaCommand
from cloudmesh_client.shell.plugins.VmCommand import VmCommand
from cloudmesh_client.shell.plugins.LimitsCommand import LimitsCommand
from cloudmesh_client.shell.plugins.CometCommand import CometCommand
from cloudmesh_client.shell.plugins.ImageCommand import ImageCommand
from cloudmesh_client.shell.plugins.HpcCommand import HpcCommand
from cloudmesh_client.shell.plugins.ColorCommand import ColorCommand
from cloudmesh_client.shell.plugins.UsageCommand import UsageCommand

import cloudmesh_client
import cloudmesh_base
from cloudmesh_base.util import get_python
from cloudmesh_base.util import check_python
import cloudmesh_base
from cloudmesh_client.common.tables import dict_printer
from cloudmesh_client.shell.command import command


class CloudmeshContext(object):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


# noinspection PyPep8Naming
class CloudmeshConsole(cmd.Cmd,
                       ServerCommand,
                       TerminalCommands,
                       ManCommand,
                       SelectCommand,
                       GroupCommand,
                       KeyCommand,
                       SecureShellCommand,
                       ReservationCommand,
                       RegisterCommand,
                       SecgroupCommand,
                       CloudCommand,
                       OpenCommand,
                       NovaCommand,
                       InventoryCommand,
                       DefaultCommand,
                       ListCommand,
                       QuotaCommand,
                       VmCommand,
                       CometCommand,
                       ImageCommand,
                       HpcCommand,
                       ColorCommand,
                       UsageCommand):
    """
    Cloudmesh Console
    """
    def register_topics(self):
        topics = {}
        for command in [TerminalCommands,
                        ManCommand,
                        ServerCommand,
                        SelectCommand,
                        GroupCommand,
                        KeyCommand,
                        SecureShellCommand,
                        RegisterCommand,
                        ReservationCommand,
                        OpenCommand,
                        CloudCommand,
                        SecgroupCommand,
                        NovaCommand,
                        InventoryCommand,
                        DefaultCommand,
                        ListCommand,
                        QuotaCommand,
                        VmCommand,
                        CometCommand,
                        LimitsCommand,
                        ImageCommand,
                        HpcCommand,
                        ColorCommand,
                        UsageCommand]:
            tmp = command.topics.copy()
            topics.update(tmp)
        for name in topics:
            self.register_command_topic(topics[name], name)
        for name in ["q", "EOF", "man"]:
            self.register_command_topic("shell", name)

    def __init__(self, context):
        cmd.Cmd.__init__(self)
        self.command_topics = {}
        self.register_topics()
        self.context = context
        if self.context.debug:
            print("init CloudmeshConsole")

        self.prompt = 'cm> '

        self.banner = textwrap.dedent("""
            +=======================================================+
            .   ____ _                 _                     _      .
            .  / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__   .
            . | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \  .
            . | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | | .
            .  \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_| .
            +=======================================================+
                                 Cloudmesh Shell
            """)
        # KeyCommands.__init__(self, context)
        for c in CloudmeshConsole.__bases__[1:]:
            c.__init__(self, context)

    def preloop(self):
        """adds the banner to the preloop"""

        if self.context.splash:
            lines = textwrap.dedent(self.banner).split("\n")
            for line in lines:
                # Console._print("BLUE", "", line)
                print(line)

    def do_EOF(self, args):
        """
        ::

            Usage:
                EOF

            Description:
                Command to the shell to terminate reading a script.
        """
        return True

    def do_quit(self, args):
        """
        ::

            Usage:
                quit

            Description:
                Action to be performed whne quit is typed
        """
        return True

    do_q = do_quit

    def emptyline(self):
        return

    def do_context(self, args):
        """
        ::

            Usage:
                context

            Description:
                Lists the context variables and their values
        """
        """
        :param args:
        :return:
        """
        print(self.context.__dict__)

    @command
    def do_version(self, args, arguments):
        """
        Usage:
           version [--format=FORMAT] [--check=CHECK]

        Options:
            --format=FORMAT  the format to print the versions in [default: table]
            --check=CHECK    boolean tp conduct an additional check [default: True]

        Description:
            Prints out the version number
        """

        python_version, pip_version = get_python()

        versions = {
            "cloudmesh_client": {
                "name": "cloudmesh_client",
                "version": str(cloudmesh_client.__version__)
            },
            "cloudmesh_base": {
                "name": "cloudmesh_base",
                "version": str(cloudmesh_base.__version__)
            },
            "python": {
                "name": "python",
                "version": str(python_version)
            },
            "pip": {
                "name": "pip",
                "version": str(pip_version)
            }
        }

        print (dict_printer(versions, output=arguments["--format"], order=["name", "version"]))
        if arguments["--check"] in ["True"]:
            check_python()

    def register_command_topic(self, topic, command_name):
        try:
            a = self.command_topics[topic]
        except:
            self.command_topics[topic] = []
        self.command_topics[topic].append(command_name)

    def do_help(self, arg):
        """
        ::

            Usage:
                help
                help COMMAND

            Description:
                List available commands with "help" or detailed help with
                "help COMMAND"."""

        if arg:
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write("%s\n" % str(doc))
                        return
                except AttributeError:
                    pass
                self.stdout.write("%s\n" % str(self.nohelp % (arg,)))
                return
            func()
        else:
            names = self.get_names()
            cmds_doc = []
            cmds_undoc = []
            help_page = {}
            for name in names:
                if name[:5] == 'help_':
                    help_page[name[5:]] = 1
            names.sort()
            # There can be duplicates if routines overridden
            prevname = ''
            for name in names:
                if name[:3] == 'do_':
                    if name == prevname:
                        continue
                    prevname = name
                    cmd = name[3:]
                    if cmd in help_page:
                        cmds_doc.append(cmd)
                        del help_page[cmd]
                    elif getattr(self, name).__doc__:
                        cmds_doc.append(cmd)
                    else:
                        cmds_undoc.append(cmd)

            self.stdout.write("%s\n" % str(self.doc_leader))
            self.print_topics(self.doc_header, cmds_doc, 15, 80)
            self.print_topics(self.misc_header, list(help_page.keys()), 15, 80)
            self.print_topics(self.undoc_header, cmds_undoc, 15, 80)

            for topic in self.command_topics:
                topic_cmds = sorted(self.command_topics[topic], key=str.lower)
                self.print_topics(string.capwords(topic + " commands"), topic_cmds, 15, 80)

    def help_help(self):
        """
        ::

            Usage:
               help NAME

            Prints out the help message for a given function
        """
        print (textwrap.dedent(self.help_help.__doc__))
    '''
    @command
    def do_bar(self, arg, arguments):
        """Usage:
                bar -f FILE
                bar FILE
                bar list

        This command does some useful things.

        Arguments:
              FILE   a file name

        Options:
              -f      specify the file

        """
        print(arguments)
    '''


def simple():
    context = CloudmeshContext(debug=False,
                               splash=True)
    con = CloudmeshConsole(context)
    con.cmdloop()


def main():
    """cm.

    Usage:
      cm --help
      cm [--debug] [--nosplash] [--file=SCRIPT] [-i] [COMMAND ...]

    Arguments:
      COMMAND                  A command to be executed

    Options:
      --file=SCRIPT  -f  SCRIPT  Executes the script
      -i                 After start keep the shell interactive,
                         otherwise quit [default: False]
      --nosplash    do not show the banner [default: False]
    """

    try:
        arg = docopt(main.__doc__, help=True)
        if arg['--help']:
            print(main.__doc__)
            sys.exit()

        # fixing the help parameter parsing

        #   arguments['COMMAND'] = ['help']
        #   arguments['help'] = 'False'

        script_file = arg['--file']

    except:
        script_file = None
        interactive = False

        arguments = sys.argv[1:]
        arg = {
            '--debug': '--debug' in arguments,
            '--nosplash': '--nosplash' in arguments,
            '-i': '-i' in arguments}

        for a in arg:
            if arg[a]:
                arguments.remove(a)

        arg['COMMAND'] = [' '.join(arguments)]

    splash = not arg['--nosplash']
    debug = arg['--debug']
    interactive = arg['-i']

    context = CloudmeshContext(debug=debug,
                               splash=splash)
    cmd = CloudmeshConsole(context)

    # TODO: check if cludmesh_yaml exists and if not create it
    # also creat .cloudmesh dir if it not exists
    """
    from cloudmesh_client.common import cloudmesh_yaml

    create_cmd3_yaml_file(force=False, verbose=False)

    filename = cloudmesh_yaml
    try:
        module_config = ConfigDict(filename=filename)
        modules = module_config["cmd3"]["modules"]
        properties = module_config["cmd3"]["properties"]
    except:
        modules = ['cloudmesh_cmd3.plugins']
    for module_name in modules:
        #print ("INSTALL", module_name)
        try:
            plugins.append(dict(get_plugins_from_module(module_name)))
        except:
            # print "WARNING: could not find", module_name
            pass

    """

    # if script_file is not None:
    #     cmd.do_exec(script_file)

    if len(arg['COMMAND']) > 0:
        try:
            user_cmd = " ".join(arg['COMMAND'])
            if debug:
                print(">", user_cmd)
            cmd.onecmd(user_cmd)
        except Exception, e:
            print("ERROR: executing command '{0}'".format(user_cmd))
            print(70 * "=")
            print(e)
            print(70 * "=")
            print(traceback.format_exc())

        if interactive:
            cmd.cmdloop()

    elif not script_file or interactive:
        cmd.cmdloop()


if __name__ == "__main__":
    main()
    # simple()
