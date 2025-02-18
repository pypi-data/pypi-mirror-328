# ---------------------------------------------------------------------------------------------------------------
# piwiPre project
# This program and library is licenced under the European Union Public Licence v1.2 (see LICENCE)
# developed by fabien.battini@gmail.com
# ---------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------
# Management of exceptions for piwiPre
# ---------------------------------------------------------------------------------------------------------------

# LOGGER.error(): prints a message and generate an exception


import inspect
import time
import datetime
import sys

import termcolor
import platform
import os


class PwpTrappedException(Exception):
    def __init__(self):
        super().__init__()


class PwpException(Exception):
    def __init__(self,  msg: str, context: str or None = None):
        super().__init__()
        self.type = "ERROR"
        self.msg = msg if msg else ""
        self.context = context


class PwpInternalException(PwpException):
    def __init__(self, filename: str, line_number: str, msg: str, context: str or None = None):
        super().__init__(msg, context)            # pragma: no cover : defensive code
        self.type = "INTERNAL"                    # pragma: no cover : defensive code
        self.filename = filename                  # pragma: no cover : defensive code
        self.line_number = line_number            # pragma: no cover : defensive code


class PwpConfigException(PwpException):
    def __init__(self, msg: str, context: str or None = None):
        super().__init__(msg, context)
        self.type = "CONFIGURATION"


class PwpFatalException(Exception):
    def __init__(self, msg: str, context: str or None = None):
        super().__init__()                  # pragma: no cover : defensive code
        self.msg = msg if msg else ""       # pragma: no cover : defensive code
        self.context = context              # pragma: no cover : defensive code
        self.type = "FATAL"                 # pragma: no cover : defensive code


class PwpLog:
    def __init__(self):
        self.cwd = os.getcwd()  # this is read at the init of the module, so BEFORE any chdir
        self.gui = None         # if there is a GUI, we will print there
        self.quiet = True
        self.logfile = None
        self.start_time = datetime.datetime.now()
        self.stop_on_warning = False
        self.print_debug = False
        self.colors = True
        self.data = {           # normal logs are not stored
            'trace': [],        # logs are stored for tests
            'info': [],         # logs that are stored for tests
            'Warning': [],      # a problem that do not require stopping the program
            'ERROR': [],        # under normal circumstances, stops the program. Can be trapped for test
        }
        self.started = False
        self.files_processed = {}
        self.db_access = 0
        if platform.system() == "Windows":
            os.system('color')

    def start_logging(self):
        logfile_name = time.strftime("piwiPre_%Y_%m_%d.log")
        try:
            self.logfile = open(logfile_name, "a", encoding="utf-8")
            print(f"Opened log file '{os.path.abspath(logfile_name)}'")
        except OSError:
            print(f"Can not open '{logfile_name}', defaulting to HOME")
            logfile_name = os.path.expanduser("~") + '/' + logfile_name
            try:
                self.logfile = open(logfile_name, "a", encoding="utf-8")
            except OSError:
                self.logfile = None
                print(f"Can not open '{logfile_name}' in HOME !, no log file.")

    def start(self, quiet: bool):

        if self.quiet and quiet and self.started:
            return   # print the banner only if it is the 1st time quiet == True, we already did it

        self.quiet = quiet
        self.db_access = 0

        if not self.started:
            self.start_logging()
            self.started = True

        if quiet:
            self.quiet = quiet
            return

        self.quiet = False
        self.msg(f"---- piwiPre start {self.start_time}")
        self.msg('')
        self.msg(f"BASE (i.e. cwd)           = '{self.cwd}'")
        self.msg(f"System                    = '{platform.system()}'")
        self.msg(f"HOME                      = '{os.path.expanduser('~')}'")
        if platform.system() == "Windows":
            self.msg(f"Exe Install Directory     = '{os.environ['PROGRAMFILES(X86)']}' /piwiPre /ffmpeg")  # noqa
            self.msg(f"Processor Architecture    = '{os.environ['PROCESSOR_ARCHITECTURE']}'")

        self.msg('')

        self.msg('--------------- Help on logs:')
        self.msg('')

        self.msg('LR[LR]')
        self.msg('     L  : Local file')
        self.msg('     R  : Remote file')
        self.msg('')

        self.msg('A[author]')
        self.msg('')

        self.msg('D[date]')
        self.msg('')

        self.msg('Rot[rf]')
        self.msg('   --  : nothing'),
        self.msg('   |-  : FLIP_LEFT_RIGHT'),  # 2
        self.msg('   ^-  : ROTATE_180'),  # 3
        self.msg('   V-  : FLIP_TOP_BOTTOM'),  # 4
        self.msg('   <|  : ROTATE_270'),  # 5
        self.msg('   <-  : ROTATE_270 + flip'),  # 6
        self.msg('   >|  : ROTATE_90 + flip'),  # 7
        self.msg('   >-  : ROTATE_90')
        self.msg('')

        self.msg('meta[diac]: information changed in the metadata of the file (EXIF or IPTC)')  # noqa
        self.msg('     d  : date')
        self.msg('     i  : instructions')
        self.msg('     a  : author')
        self.msg('     c  : copyright')
        self.msg('')

        self.msg('rep[R]  : Representative picture for video')
        self.msg('')

        self.msg('th[STM2XLWUCI] : thumbnail')               # noqa
        self.msg('     S  : _sq.jpg :  120x120   SQUARE cropped to square')
        self.msg('     T  : _th.jpg :  144x144   THUMB')
        self.msg('     M  : _me.jpg :  792x594   MEDIUM')
        self.msg('     2  : _2s.jpg :  240x240   XXSMALL')     # noqa
        self.msg('     X  : _xs.jpg :  432x324   XSMALL')      # noqa
        self.msg('     L  : _la.jpg : 1008x756   LARGE')       # noqa
        self.msg('     W  : _xl.jpg : 1224x918   XLARGE')      # noqa
        self.msg('     U  : _xx.jpg : 1656x1242  XXLARGE')     # noqa
        self.msg('     C  : _cu_250.jpg : 250x250 cropped to square')
        self.msg('     I  : _index.jpg')
        self.msg('')

        self.msg('rth[stm2xlwuci] : Remote thumbnail')              # noqa
        self.msg('   same formats than thumbnails, but lower case')
        self.msg('')

        self.msg('db[CSWH5GA]: information changed in the piwigo SQL database')  # noqa
        self.msg('     C  : Created in the db')
        self.msg('     S  : Size')
        self.msg('     W  : Width')
        self.msg('     H  : Height')
        self.msg('     5  : md5')
        self.msg('     G  : GPS info')
        self.msg('     A  : Author')
        self.msg('')

        self.msg('Actions:[album filename] ')
        self.msg('  Keep  : file was already in album, keep that value')
        self.msg('  Renam : Rename to a new filename because of conflict, and copy to album')              # noqa
        self.msg('  Copy  : copy file to album, there was no previous file')
        self.msg('  Updat : update the file in album with new value')                                      # noqa
        self.msg('  Clobb : Clobber previous version in album, rename was not allowed')                    # noqa
        self.msg('  DELET : File was deleted from local album because no corresponding remote file')       # noqa
        self.msg('  ABORT : Processing of file is aborted, because no remote file')
        self.msg('')

        self.msg('Back:[backup filename] ')
        self.msg('', flush=True)
        # self.test_msg("This is a message generated by test harness")
        # self.warning("This is a warning")

    def __del__(self):
        if self.logfile:
            self.logfile.close()
        # if self.quiet:
        #     return
        print('---- piwiPre End ')

    def configure(self, config):
        self.print_debug = config['debug']
        self.stop_on_warning = config['stop-on-warning']
        self.colors = config['enable-colors']

    def reset_data(self):
        self.start_time = datetime.datetime.now()
        self.db_access = 0
        self.data = {
            'trace': [],
            'info': [],
            'Warning': [],
            'ERROR': [],
        }
        old = self.files_processed
        self.files_processed = {}
        return old

    def msg_nb(self, level):
        return len(self.data[level])

    def end(self):
        # if self.quiet:
        #     self.msg('', flush=True)
        #     return
        end = datetime.datetime.now()
        self.msg(f"--- start         = {self.start_time} ---")
        self.msg(f"--- end           = {end} ---")
        self.msg(f"--- duration      = {end - self.start_time}")
        files = 0
        for k in self.files_processed:
            self.msg(f"--- {k:14} = {self.files_processed[k]} ")
            files += self.files_processed[k]
        if files:
            self.msg(f"--- duration/file = {(end - self.start_time) / files}")
        self.msg("------------------------------------", flush=True)

    def incr_picture(self, category):
        self.files_processed[category] = 1 if category not in self.files_processed \
            else self.files_processed[category] + 1

    def incr_db_access(self):
        self.db_access += 1

    def add_gui(self, gui):
        self.gui = gui

    def __print_highlight(self, level, color):
        if color and self.colors and level in ['Warning', 'ERROR']:
            print(termcolor.colored(f"{level:7} ***********************************************************",
                                    color=color, force_color=True))

    def __print_colored(self, level, lines, color):
        if color and self.colors:
            for msg in lines:
                print(termcolor.colored(f"{level:7} {msg}", color=color, force_color=True))
        else:
            for msg in lines:
                print(f"{level:7} {msg}", flush=True)

        if self.logfile:
            for msg in lines:
                self.logfile.write(f"{level:7} {msg}\n")

        if self.gui:
            gui_msg = ""
            for msg in lines:
                gui_msg += f"{level:7} {msg}"
            self.gui.gui_msg(gui_msg, level=level)

    def do_msg(self, msg, context=None, level='msg', flush=False, color=None):

        lines = []
        if context is not None:
            if level not in ['debug', 'info'] or self.print_debug:
                lines.append(context)

        if level not in ['debug', 'info'] or self.print_debug:
            lines.append(msg)

        if lines:
            self.__print_highlight(level, color)
            self.__print_colored(level, lines, color)
            self.__print_highlight(level, color)

            if flush:
                if self.logfile:
                    self.logfile.flush()
                sys.stdout.flush()

        if level != 'msg' and level != 'debug':
            self.data[level].append(msg)

        if level == 'Warning' and self.stop_on_warning:
            self.error("Stop on warning")

        if level == 'Warning' and self.msg_nb('Warning') > 20:
            self.error("Too much warnings")

        if level == 'ERROR' and self.msg_nb('ERROR') > 20:
            self.fatal_error("Too much errors, aborting")

    # -------------------------------------------------
    # class of messages, ranked lowest priority first
    # -------------------------------------------------

    def debug(self, msg, context=None):  #
        """
        debug is NOT kept for test, and printed only if --debug
        color is light_grey
        :param msg:
        :param context:
        :return:
        """
        self.do_msg(msg, context=context, level='debug', color="light_grey", flush=True)

    def trace(self, msg: str, context: str or None = None):
        """
        trace is always kept for test, and printed only if --debug
        color is light_grey
        if GUI, does NOT generate a PopUp
        """
        self.do_msg(msg, context=context, level='trace', color="light_grey", flush=True)

    def msg(self, msg, context=None,  flush=False):
        """
        msg is NOT kept for test, and ALWAYS printed,
        """
        # if not self.quiet:
        self.do_msg(msg, context=context, level='msg', flush=flush)

    def test_msg(self, msg, context=None):
        self.do_msg("    Test: " + msg, context=context, level='msg', color='blue')

    def info(self, msg):
        self.do_msg(msg, level='msg', color="yellow", flush=True)

    def warning(self, msg: str, context: str or None = None):
        """
        warning is always kept for test,
        ALWAYS printed,
        color is orange
        if GUI, does generate a PopUp
        """
        self.do_msg(msg, context=context, level='Warning', flush=True, color="light_red")    # previously reg

    def error(self, msg, context=None):                              # pragma: no cover
        self.do_msg(msg, level='ERROR', context=context, flush=True, color="magenta")
        if self.gui:
            raise PwpTrappedException
        else:
            raise PwpException(msg, context)

    def internal_error(self, msg: str):                               # pragma: no cover
        previous_frame = inspect.currentframe().f_back
        (filename, line_number, _function_name, _lines, _index) = inspect.getframeinfo(previous_frame)
        context = f"{filename}:{line_number:3}"
        self.do_msg(msg, context=context, level='ERROR', flush=True, color="magenta")
        raise PwpInternalException(filename, line_number, msg, context)

    def config_error(self, msg, context="Cmd-line or .ini file"):    # pragma: no cover
        self.do_msg(msg, level='ERROR', context=context, flush=True, color="magenta")
        if self.gui:
            raise PwpTrappedException
        else:
            raise PwpConfigException(msg, context)

    def fatal_error(self, msg):                                        # pragma: no cover
        self.do_msg(msg, level='ERROR', flush=True, color="red")
        raise PwpFatalException(msg)


LOGGER = PwpLog()
