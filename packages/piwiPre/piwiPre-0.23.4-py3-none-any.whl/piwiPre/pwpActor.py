# ---------------------------------------------------------------------------------------------------------------
# piwiPre project
# This program and library is licenced under the European Union Public Licence v1.2 (see LICENCE)
# developed by fabien.battini(at)gmail.com
# ---------------------------------------------------------------------------------------------------------------

import re
import os
import shutil
import time
import datetime
# import tracemalloc    # noqa
# import gc
import pathlib
import sys
import stat

# https://mariadb.com/docs/server/connect/programming-languages/c/install/
# noqa      sudo apt install libmariadb3 libmariadb-dev
# pip install mariadb

try:
    import mariadb
except ImportError as err:
    if '--quiet' not in sys.argv:
        print(f"Error {err} while importing mariadb")
    mariadb = None

import hashlib

# pip install fabric
# doc: https://docs.fabfile.org/en/stable/
# doc: https://www.paramiko.org/
# doc: https://help.ubuntu.com/community/SSH/OpenSSH/Keys
import fabric
import invoke

# pip install requests
# doc: https://requests.readthedocs.io/en/latest/

# import requests.cookies


import urllib3.exceptions

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Remove useless warning on https certificates


# --------------------------------------------------------

from piwiPre.pwpErrors import LOGGER


class PwpSummary:
    def __init__(self, stage, old_file):
        # old_file should be a PwpFileEntry
        self.stage = stage
        self.old_file = old_file
        self.local = old_file.is_local if old_file else None
        self.remote = old_file.is_remote if old_file else None
        self.author = ''
        self.date = ''
        self.rotation = ''

        self.meta_date = False
        self.meta_instructions = False
        self.meta_author = False
        self.meta_copyright = False

        self.action = ""
        self.destination = None

        self.backup = ""

        self.representative = False

        self.db_created = False
        self.db_size = False
        self.db_width = False
        self.db_height = False
        self.db_md5 = False
        self.db_gps = False
        self.db_author = False

        self.thumb_s = False
        self.thumb_t = False
        self.thumb_m = False
        self.thumb_2 = False
        self.thumb_x = False
        self.thumb_l = False
        self.thumb_w = False
        self.thumb_u = False
        self.thumb_c = False
        self.thumb_index = False

        self.rem_thumb_s = False
        self.rem_thumb_t = False
        self.rem_thumb_m = False
        self.rem_thumb_2 = False
        self.rem_thumb_x = False
        self.rem_thumb_l = False
        self.rem_thumb_w = False
        self.rem_thumb_u = False
        self.rem_thumb_c = False
        self.rem_thumb_index = False

        self.auto_conf = False
        self.rem_auto_conf = False

    def get_meta(self):
        meta = ""
        meta += "d" if self.meta_date else '-'
        meta += "i" if self.meta_instructions else '-'
        meta += "a" if self.meta_author else '-'
        meta += "c" if self.meta_copyright else '-'
        return meta

    def __str__(self):
        name = f"{self.old_file.basename[-40:]:40}"
        author = f"{self.author[-15:]:15}"

        action = self.action
        dst = '' if self.destination is None else self.destination.local
        # dst = f"{destination[-50:]:50}"

        backup = f"{self.backup}"

        where = ""
        where += 'L' if self.local else '-'
        where += 'R' if self.remote else '-'

        meta = self.get_meta()

        rep = "R" if self.representative else '-'

        db = ""
        db += "c" if self.db_created else '-'
        db += "s" if self.db_size else '-'
        db += "w" if self.db_width else '-'
        db += "h" if self.db_height else '-'
        db += "5" if self.db_md5 else '-'
        db += "g" if self.db_gps else '-'
        db += "a" if self.db_author else '-'

        thumbs = ""
        thumbs += 'S' if self.thumb_s else '-'
        thumbs += 'T' if self.thumb_t else '-'
        thumbs += 'M' if self.thumb_m else '-'
        thumbs += '2' if self.thumb_2 else '-'
        thumbs += 'X' if self.thumb_x else '-'
        thumbs += 'L' if self.thumb_l else '-'
        thumbs += 'W' if self.thumb_w else '-'
        thumbs += 'U' if self.thumb_u else '-'
        thumbs += 'C' if self.thumb_c else '-'
        thumbs += 'I' if self.thumb_index else '-'

        rem_thumbs = ""
        rem_thumbs += 's' if self.rem_thumb_s else '-'
        rem_thumbs += 't' if self.rem_thumb_t else '-'
        rem_thumbs += 'm' if self.rem_thumb_m else '-'
        rem_thumbs += '2' if self.rem_thumb_2 else '-'
        rem_thumbs += 'x' if self.rem_thumb_x else '-'
        rem_thumbs += 'l' if self.rem_thumb_l else '-'
        rem_thumbs += 'w' if self.rem_thumb_w else '-'
        rem_thumbs += 'u' if self.rem_thumb_u else '-'
        rem_thumbs += 'i' if self.rem_thumb_c else '-'
        rem_thumbs += 'i' if self.rem_thumb_index else '-'

        return (f"{self.stage:6} {name} LR[{where}] A[{author}] D[{self.date:19}] " +
                f"rot[{self.rotation:2}] meta[{meta}] rep[{rep}] db[{db}] " +
                f"th[{thumbs}] rth[{rem_thumbs}] {action:5}:[{dst}] back[{backup}]")


class DirInfo:
    def __init__(self, name, path, dir_id, rank, id_upper_cat, global_rank, upper_cats,
                 representative_picture_id):
        self.name = name
        self.path = path  # full path starting with ./galleries/photo  (not available in the database)
        self.dir_id = dir_id
        self.rank = rank
        self.id_upper_cat = id_upper_cat
        self.global_rank = global_rank
        self.upper_cats = upper_cats
        self.representative_picture_id = representative_picture_id

    def __str__(self):
        return f"dir('{self.path}':{self.dir_id})"

    #    images: piwigo_images                                      updated if file changed     created if file new
    #       id: unique id of the picture                                                                yes
    #       file: filename, without path                                                                yes
    #       date_available: date on insertion in the database                                           yes
    #       date_creation: creation date of the file                                                    yes
    #       name: display name of the picture. defaults to file                                         yes
    #       comment: user comment. defaults to null
    #       author: defaults to null
    #       hit:
    #       filesize: file size                                             yes,                        yes     # noqa
    #       width:  picture width                                           yes,                        yes
    #       height: picture height                                          yes,                        yes
    #       coi:
    #       representative_ext: the 4 char extension of representative
    #       date_metadata_update:                                                                       yes
    #       path:  full path of file, starting with ./galleries/photo                                   yes
    #       storage_category_id: id of storage dir                                                      yes
    #       level:  level of privacy. defaults to 0. sometimes 4, which is probably an error            yes
    #       md5sum:                                                         yes                         yes
    #       added_by: id of inserter,                                                                   yes
    #       rotation: defaults to 0                                         yes,                        yes
    #       latitude:                                                       yes,                        yes
    #       longitude:                                                      yes,                        yes
    #               see 2023-02-19-11h02-55-Plouhinec.jpg                                                       # noqa
    #       lastmodified:                                                   yes (automatic)             yes     # noqa


class FileInfo:
    def __init__(self, file_id, file, date_available, date_creation, name, author, file_size, width, height,
                 date_metadata_update, path, storage_category_id, level, md5sum, added_by, latitude, longitude,
                 representative_ext, last_modified):
        self.file_id = file_id
        self.file = file
        self.date_available = date_available
        self.date_creation = date_creation
        self.name = name
        self.author = author
        self.file_size = file_size
        self.width = width
        self.height = height
        self.date_metadata_update = date_metadata_update
        self.path = path
        self.storage_category_id = storage_category_id
        self.level = level
        self.md5sum = md5sum if md5sum != "null" else None
        self.added_by = added_by
        self.latitude = latitude
        self.longitude = longitude
        self.representative_ext = representative_ext
        self.last_modified = last_modified

    def __str__(self):
        return f"file('{self.path}':{self.file_id})"


class PwpActor:
    allowed_chars = r"a-zA-Z0-9\-_.&@~!,;+°()àâäéèêëïîôöùûüÿçñÀÂÄÉÈÊËÏÎÔÖÙÛÜŸÇÑ "  # noqa
    tmp_dir = '.piwiPre.tmp'

    def __init__(self):
        self.dryrun = False
        # values that are cached from the 1st config used
        self.print_debug = False
        self.trace_malloc = False

        # management of piwigo
        self.piwigo_user = None
        self.piwigo_level = 0

        # management of ssh/sftp
        self.remote_user = None
        self.remote_pwd = None
        self.remote_host = None
        self.remote_port = None
        self.ls_command = None
        self.ls_output = None
        self.ssh_connection: fabric.Connection or None = None

        self.remote_uname = None

        self.sql_host = None
        self.sql_port = None
        self.sql_user = None
        self.sql_pwd = None
        self.sql_database = None
        self.sql_connection = None

        # info about the first album
        self.sql_first_album = None  # name
        self.sql_first_album_id = None  # id of the first album
        self.sql_first_album_path = None
        self.sql_first_album_upper_cat = None
        self.sql_first_album_global_rank = None
        self.sql_first_album_upper_cats = None
        self.sql_first_album_rank = None
        self.sql_first_representative = None

        # end of cache
        self.dir_made = []
        self.dir_numbers = {}

    @staticmethod
    def get_environ(name):
        try:
            res = os.environ[name]
        except OSError as e:
            LOGGER.error(f"get_environ[{name}] : ERROR {e}")
            return None
        res = res.replace('\\', '/')
        return res

    def configure(self, config):
        self.print_debug = config['debug']
        self.dryrun = config['dryrun']
        self.trace_malloc = config['trace-malloc']

        #  self.trace_malloc_start()

        self.connect_ssh(config)
        self.connect_sql(config)

    def reset_data(self):
        self.dryrun = False
        # values that are cached from the 1st config used
        self.print_debug = False
        # end of cache
        self.dir_made = []
        self.dir_numbers = {}

        # self.ssh_connection = None  NO REASON to do this, notably without closing the previous one

    @staticmethod
    def isdir(path):
        # os.path.isdir() is NOT reliable on NFS share drives
        try:
            res = os.stat(path)
            return stat.S_ISDIR(res.st_mode)
        except FileNotFoundError:
            # this is the normal error
            return False
        except NotADirectoryError:
            # this is another normal error
            return False
        except OSError as e:
            if e.errno == 6:
                # non valid descriptor
                return False
            if e.errno == 13:
                # permission denied
                # we see this error when the directory has just been erased
                # probably a transient NFS error ?
                # see BUG 0325 while executing program_699
                return False
            LOGGER.error(f"Error {e}, errno = {e.errno} while isdir({path})")  # noqa  # pragma: no cover: defensive code

    @staticmethod
    def is_a_subdir(path, father):
        n_path = os.path.abspath(path)
        n_base = os.path.abspath(father)

        return n_path.startswith(n_base)

    @staticmethod
    def is_same_dir(p1, p2):
        n1 = PwpActor.linux_path(os.path.abspath(p1))
        n2 = PwpActor.linux_path(os.path.abspath(p2))
        return n1 == n2

    @staticmethod
    def linux_path(path: str):
        return path.replace("\\", '/')

    @staticmethod
    def normalise_path(path, base: str = '.', error_if_not_included=False, caller="", absolute=False):
        # '.'. means os.getcwd()    # noqa
        if path != '' and path[0] == '[' and path[-1] == ']':
            return path
        n_path = os.path.abspath(path)
        n_base = os.path.abspath(base)

        if absolute is False:
            if n_path.startswith(n_base):
                return PwpActor.linux_path(os.path.relpath(n_path, n_base))
            if error_if_not_included:   # pragma: no cover: defense code
                LOGGER.config_error(f"{caller} : {path} should be included in {base}")
                return None

        # path_drive, _ = os.path.splitdrive(n_path)
        # base_drive, _ = os.path.splitdrive(n_base)
        # if path_drive == base_drive:
        #     return os.path.relpath(n_path, n_base)

        return PwpActor.linux_path(n_path)

    @staticmethod
    def isfile(path) -> bool:
        try:
            return os.path.isfile(path)
        except OSError as e:                                       # pragma: no cover: defensive code
            LOGGER.error(f"Error {e}, while isfile({path})")
            return False

    def mkdirs(self, dir_name, forced=False):
        dir_name = dir_name.rstrip('/')
        dir_name = dir_name or '.'

        if self.dryrun and not forced:
            LOGGER.debug(f"Would makedirs '{dir_name}'")
            return True

        # # ACTOR.flush_nfs_dir(os.path.dirname(dir_name))     # noqa
        # the father dir may not exist, so we cannot flush it

        father = os.path.dirname(dir_name)
        if os.path.dirname(father) != father:
            # os.path.dirname('//toto/fifi/lulu") -> '//toto/fifi'  # noqa
            # BUT:
            # os.path.dirname('//toto/fifi") -> '//toto/fifi', because python recognizes the network share syntax/ # noqa
            self.mkdirs(father)
            # this is a home-made recursive implementation of makedirs,
            # in an attempt to trap all nfs flush problems.

        # if father != dir_name:
        # ACTOR.flush_nfs_dir(father)

        if self.isdir(dir_name):
            # LOGGER.msg(f"mkdirs: '{dir_name}' exists")
            # ACTOR.flush_nfs_dir(dir_name)
            return False

        try:
            os.makedirs(dir_name, exist_ok=True)
        except FileExistsError as e:
            # this should NEVER happen, because we have just checked if os.path.isdir(dir_name) ...
            # but, in real-life, it DOES happen, probably some inconsistency in the NFS implementation
            LOGGER.error(f"mkdirs: '{dir_name}' exists ERROR {e}")  # pragma: no cover: defensive code
        except OSError as e:
            LOGGER.error(f"mkdirs: '{dir_name}' ERROR {e}")  # pragma: no cover: defensive code

        # ACTOR.flush_nfs_dir(father)

        if self.isdir(dir_name):
            LOGGER.debug(f"makedirs '{dir_name}'")
        else:
            # This is probably a transient error due to NFS. Better stop and rerun than keep an inconsistent state
            LOGGER.error(f"FAIL: makedirs '{dir_name}'")  # pragma: no cover: defensive code

    def copy(self, src, dst, forced=False):
        """
        copy src to dst, unless dryrun is True
        :param src: file to copy
        :param dst: destination filename
        :param forced: if True, copy is always done, if False, do not copy if dryrun is True
        :return: None
        """
        base = os.path.dirname(dst)
        self.mkdirs(base, forced)

        if not ACTOR.isfile(src):
            LOGGER.error(f"FAILED copy '{src}' ->  '{dst}' : non existing source")  # pragma: no cover: defensive code

        if self.dryrun and not forced:
            LOGGER.debug(f"Would copy '{src}' ->  '{dst}'")
            return

        try:
            shutil.copy2(src, dst)  # preserve metadata
        except OSError as e:
            LOGGER.error(f"copy: '{src}', {dst} ERROR {e}")  # pragma: no cover: defensive code


        # ACTOR.flush_nfs_dir(os.path.dirname(dst))     # noqa

        if ACTOR.isfile(dst):
            LOGGER.debug(f"copy '{src}' ->  '{dst}'")
        else:
            # This is probably a transient error due to NFS. Better stop and rerun than keep an inconsistent state
            LOGGER.error(f"FAIL:copy '{src}' ->  '{dst}'")  # pragma: no cover: defensive code

    def copytree(self, src, dst):
        """
        copytree(self, src, dst): safely copy src to dst : dst will be a copy of src
        :param src: source directory
        :param dst: destination directory
        :return: None
        """
        if self.dryrun:  # pragma: no cover
            LOGGER.debug(f"Would copytree'{src}' ->  '{dst}'")
            return

        try:
            shutil.copytree(src, dst, dirs_exist_ok=True)
        except OSError as e:
            LOGGER.error(f"copytree: '{src}', {dst} ERROR {e}")  # pragma: no cover: defensive code

        # ACTOR.flush_nfs_dir(dst)

        if ACTOR.isdir(dst):
            LOGGER.debug(f"copytree '{src}' ->  '{dst}'")
        else:
            # This is probably a transient error due to NFS. Better stop and rerun than keep an inconsistent state
            LOGGER.error(f"FAIL:copytree '{src}' ->  '{dst}'")  # pragma: no cover: defensive code

    def move(self, src, dst, forced=False):
        if self.dryrun and not forced:  # pragma: no cover
            LOGGER.debug(f"Would move file '{src}' -> '{dst}'")
            return

        base = os.path.dirname(dst)
        try:
            self.mkdirs(base)
            if os.path.exists(dst):
                self.delete(dst)  # pragma: no cover
        except OSError as e:
            LOGGER.error(f"mkdirs: '{base}' ERROR {e}")  # pragma: no cover: defensive code

        try:
            shutil.move(src, dst)
        except FileNotFoundError as e:
            LOGGER.warning(f"move file  '{src}' , {dst} FileNotFoundError ERROR {e}")  # pr
        except OSError as e:
            LOGGER.error(f"move: '{src}', {dst}' ERROR {e}")  # pragma: no cover: defensive code

        # ACTOR.flush_nfs_dir(os.path.dirname(dst)) # noqa

        # let's assume the library does the job and yell in case of problem
        #
        if os.path.exists(dst):
            LOGGER.debug(f"move file '{src}' -> '{dst}'")
        else:
            # from time to time, this exception arises which is completely abnormal,
            # since shutil.move has raised no exception
            # this happens ONLY on NFS network shares, not with physical HDD
            LOGGER.error(f"FAIL:move file '{src}' -> '{dst}'")  # pragma: no cover: defensive code

    def delete(self, src, forced=False, msg=""):
        # if we do not do this, we have file not found exceptions
        # because in some tests, the file has just been created, erased, created again
        # and NFS buffers are outdated
        # ACTOR.flush_nfs_dir(os.path.dirname(src)) # noqa

        if not os.path.exists(src):
            LOGGER.debug(f"CAVEAT: {msg} Delete '{src}' non existing file")
            return False

        if self.dryrun and not forced:
            LOGGER.trace(f"Would delete '{src}' {msg}")
            return False

        try:
            os.remove(src)
        except FileNotFoundError as e:
            # this should NEVER happen, but does from time to time,
            # and always end up with the file being erased
            LOGGER.warning(f"delete file  '{src}' raised FileNotFoundError Exception {e}")  # pragma: no cover: defense
            LOGGER.error(f"FAIL: delete '{src}'")  # pragma: no cover: defensive code
        except OSError as e:
            LOGGER.warning(f"delete file  '{src}' raised OSError {e}")  # pragma: no cover: defensive code
            LOGGER.error(f"FAIL: delete '{src}' error {e}")  # pragma: no cover: defensive code

        # ACTOR.flush_nfs_dir(os.path.dirname(src)) # noqa

        if os.path.exists(src):
            LOGGER.warning(f"delete file  '{src}' file still exists")  # pragma: no cover: defensive code
            LOGGER.error(f"FAIL: delete '{src}'  {msg}")  # pragma: no cover: defensive code

        LOGGER.debug(f"deleted file '{src}'  {msg} OK")
        return True

    def rmtree(self, src, msg: str = ''):
        if not ACTOR.isdir(src):
            LOGGER.debug(f"rmtree '{src}' : non existing directory  {msg}")
            return False

        if self.dryrun:
            LOGGER.debug(f"would remove tree '{src}'  {msg}")
            return False

        try:
            shutil.rmtree(src)  # self.do_rmtree(src)  #
        except OSError as e:
            LOGGER.error(f"FAIL: error {e} while remove tree '{src}'  {msg}")  # pragma: no cover: defensive code

        # ACTOR.flush_nfs_dir(os.path.dirname(src)) # noqa

        if ACTOR.isdir(src):
            # This is probably a transient error due to NFS. Better stop and rerun than keep an inconsistent state
            LOGGER.error(f"FAIL:  remove tree '{src}'  {msg}")  # pragma: no cover: defensive code
        else:
            LOGGER.debug(f"removed tree  '{src}'  {msg}")

        # Python bug here !
        #       We have from time to time, located on the calling context in PwpMain:
        #       UnboundLocalError: local variable 'local_file_path' referenced before assignment
        #       when this is error is clearly wrong.
        #       It seems that adding a return value helps.
        return True

    @staticmethod
    def open(filename: str, mode: str, encoding="utf-8"):
        if mode == 'r' and not ACTOR.isfile(filename):
            LOGGER.error(f"ERROR reading non-existing file {filename}")  # pragma: no cover: defensive code
        try:
            if "b" in mode:  # pragma: no cover
                return open(filename, mode)  # binary mode doesn't take an encoding argument
            return open(filename, mode, encoding=encoding)

        except FileNotFoundError as e:
            LOGGER.warning(f"open '{filename}'  FileNotFoundError ERROR {e}")  # pr

        except OSError as e:
            LOGGER.error(f"open: '{filename}' ERROR {e}")  # pragma: no cover: defensive code

    @staticmethod
    def get_last_numerical_field(template: str):
        items_list = re.findall('{[^}]*}', template)
        non_numerical = ['{a}', '{month_name}', '{occasion}', '{author}', '{suffix}', '{file}']
        while items_list:
            res = items_list.pop()
            if res not in non_numerical:
                return res[1:-1]  # skip {}
        LOGGER.internal_error(f"incoherent get_last_numerical_field {template} returns None")  # pragma: no cover: defe

    def get_info_from_format(self, template: str, src: str, field_name: str):
        """
        Extract information from src according to the descriptor
        :param template: a string that describes the information format
        :param src: the source with information
        :param field_name: for error message
        :return: a dictionary

        Assuming that template is a reasonably simple format,

        Assuming also that the possible items within template are all known,
        which is the case in piwiPre.

        If the same fields occurs several times, then the 1st instance of the field is returned

        If src is the result of formatting template with some values,
        then we can find back the values, provided the string is simple enough.
        This can even been done independently of the order of the fields in the template,
        because we can find the order by analysing template.
        """
        items_list = re.findall('{[^}]*}', template)  # the list of all items to find, e.g. '{Y}'
        # here, we have all items possibly found in piwiPre
        trans = {
            'size': r"(\d+)",  # noqa
            'Y': r"(\d\d\d\d)",
            'm': r"(\d\d)",
            'd': r"(\d\d)",
            'H': r"(\d\d)",
            'M': r"(\d\d)",
            'S': r"(\d\d)",
            'ms': r"(\d+)",
            'count': r"(\d+)",
            'z': r"(\+?\-?\d\d\d\d)",
            'a': r"(am|pm)",
            'month_name': '([' + self.allowed_chars + ']+)',
            'occasion': '([' + self.allowed_chars + ']+)',
            'author': r'(.*)',
            'suffix': r'(\w+)$',
            'file': r"(.*?)",  # noqa
            'flags': r'([-+\w]+)',
            'basename': '([' + self.allowed_chars + ']+)',
        }
        template2 = str.replace(template, '.', '\\.')
        dico = None

        try:
            str_format = template2.format(**trans)
            res = re.match(str_format, src)
            if res:
                dico = {}
                for field in trans.keys():
                    ff = '{' + field + '}'
                    dico[field] = res.group(items_list.index(ff) + 1) if ff in items_list else None
        except IndexError as e:
            LOGGER.error(f"Error {e} while trying to parse file names, "
                         f" the '{field_name}' config item is probably wrong \n"
                         f" '{field_name}' = '{template}'"
                         )   # pragma: no cover: defensive code

        return dico

    def create(self, filename):
        with self.open(filename, 'w') as f:
            f.write(f"Fake file created for test {datetime.datetime.now()}\n")

    # ----------------------------------------------------------------------
    # management of ssh/sftp

    @staticmethod
    def build_timestamp(filename: str):
        try:
            file_time = os.path.getmtime(filename)
            timestamp = time.strftime("%Y/%m/%d-%H:%M:%S", time.localtime(file_time))
            return timestamp
        except FileNotFoundError as e:
            LOGGER.warning(f"getmtime '{filename}'  FileNotFoundError ERROR {e}")  # pr
        except OSError as e:                                     # pragma: no cover: defense code
            LOGGER.error(f"getmtime: '{filename}' ERROR {e}")
            return None

    @staticmethod
    def timestamp_from_ls(d: dict):
        dt: datetime.datetime = d['date']
        timestamp = f"{dt.year:4}/{dt.month:02}/{dt.day:02}-{dt.hour:02}:{dt.minute:02}:{dt.second:02}"
        return timestamp

    def remote_run(self, cmd: str, forced=False, warn_if_error=True):  # , with_sudo=False):
        if self.dryrun and not forced:
            return None

        if self.ssh_connection:
            try:
                # if with_sudo:
                #    res = self.ssh_connection.sudo(cmd, hide=True, warn=True, encoding='utf8')
                # else:
                res = self.ssh_connection.run(cmd, hide=True, warn=True, encoding='utf8')
            except invoke.exceptions.ThreadException as e:
                LOGGER.warning(f"ssh('{cmd}') failed with unexpected exception {e}")
                return None

            if not res.ok:
                LOGGER.trace(f"CAVEAT remote '{cmd}' returned {res.stderr}")
                if warn_if_error:
                    LOGGER.warning(f"CAVEAT remote '{cmd}' returned {res.stderr}")  # pragma: no cover

            return res
        LOGGER.error("trying to run a ssh command without a ssh connection", cmd)  # pragma: no cover: defensive code

    @staticmethod
    def my_decode(item: str) -> str:
        """
        Manages the unknown encoding used by ls - paramiko - fabfile  
        returns the decoded string
        only chars in 'allowed_chars' are processed
        
        :param item: string to be decoded 
        :return: the decoded string"""  # noqa

        # only allowed chars
        table = {'\\302\\260': '°', '\\303\\240': 'à', '\\303\\242': 'â', '\\303\\244': 'ä', '\\303\\251': 'é',
                 '\\303\\250': 'è', '\\303\\252': 'ê', '\\303\\253': 'ë', '\\303\\257': 'ï', '\\303\\256': 'î',
                 '\\303\\264': 'ô', '\\303\\266': 'ö', '\\303\\271': 'ù', '\\303\\273': 'û', '\\303\\274': 'ü',
                 '\\303\\277': 'ÿ', '\\303\\247': 'ç', '\\303\\261': 'ñ', '\\303\\200': 'À', '\\303\\202': 'Â',
                 '\\303\\204': 'Ä', '\\303\\211': 'É', '\\303\\210': 'È', '\\303\\212': 'Ê', '\\303\\213': 'Ë',
                 '\\303\\217': 'Ï', '\\303\\216': 'Î', '\\303\\224': 'Ô', '\\303\\226': 'Ö', '\\303\\231': 'Ù',
                 '\\303\\233': 'Û', '\\303\\234': 'Ü', '\\305\\270': 'Ÿ', '\\303\\207': 'Ç', '\\303\\221': 'Ñ'}
        new_val = ''
        i = 0
        while i < len(item):
            s = item[i:i + 8]
            if s in table:
                new_val += table[s]
                i += 8
            elif item[i:i + 2] == '\\\\':  # pragma: no cover
                new_val += '\\'
                i += 2
            else:
                new_val += item[i]
                i += 1
        return new_val

    def remote_ls(self, directory, forced=False, warn_if_absent=False):
        directory = directory or '.'
        LOGGER.debug(f"ssh ls '{directory}' ")
        if not forced and self.dryrun:
            return {}  # pragma: no cover

        ls_cmd = self.ls_command.format(file=directory)
        try:
            result = self.remote_run(ls_cmd, forced=forced, warn_if_error=warn_if_absent)
        except FileNotFoundError:
            return {}
        res = self.my_decode(result.stdout)
        all_lines = res.split('\n')
        all_files: dict = {}
        for line in all_lines:
            dico = self.get_info_from_format(self.ls_output, line, 'ls-output')
            if dico:
                f_date = datetime.datetime(year=int(dico['Y']), month=int(dico['m']), day=int(dico['d']),
                                           hour=int(dico['H']), minute=int(dico['M']), second=int(dico['S']),
                                           microsecond=int(int(dico['ms']) / 1000) if 'ms' in dico else 0)
                # NB: datetime gets microseconds, but ls provides nanoseconds
                # TODO: manage timezone
                if dico['flags'][0] == 'd':
                    new_dico = {"date": f_date, "dir_name": dico['file'], "type": 'dir'}
                else:
                    new_dico = {"date": f_date, "size": int(dico['size']), "filename": dico['file'], 'type': 'file'}
                all_files[dico["file"]] = new_dico

        return all_files

    def remote_create(self, filename):
        self.remote_run(f"touch {filename}")

    def remote_isfile(self, filepath, forced=False, warn_if_absent=False):
        """

        :param filepath: file path , on the remote host, of file to test
        :param forced: if True, do it even if dryrun is True
        :param warn_if_absent: if True, issues a warning if file is absent
        :return: None if the file does not exist, dico of information if file exists
        """
        if self.dryrun and not forced:
            return None  # pragma: no cover: defensive code
        all_files = self.remote_ls(os.path.dirname(filepath), forced=forced, warn_if_absent=warn_if_absent)
        if all_files is not None and os.path.basename(filepath) in all_files.keys():
            LOGGER.debug(f"ssh file_exists '{filepath}' : YES")
            return all_files[os.path.basename(filepath)]
        LOGGER.debug(f"ssh file_exists '{filepath}' : NO")
        return None

    def remote_mkdir(self, directory):
        if directory in self.dir_made:
            return
        LOGGER.debug(f"remote mkdir '{directory}'")
        self.remote_run(f'mkdir -p "{directory}"')  # need "" to quote spaces
        self.dir_made.append(directory)  # self.dir_made is actually be cleaned at the end of run

    def remote_put(self, src, directory):   # ,with_sudo=False):
        LOGGER.debug(f"remote put '{src}' '{directory}'")
        if self.dryrun:
            return
        tmp_file = self.tmp_dir + '/' + src
        if self.ssh_connection:
            tmp_path = os.path.dirname(tmp_file)
            self.remote_mkdir(tmp_path)
            self.remote_mkdir(directory)
            sftp = self.ssh_connection.sftp()
            sftp.put(src, tmp_file, confirm=True)
            try:
                f_a_time = os.path.getatime(src)
                f_m_time = os.path.getmtime(src)
                sftp.utime(tmp_file, (f_a_time, f_m_time))
            except FileNotFoundError as e:
                LOGGER.warning(f"getatime '{src}'  FileNotFoundError ERROR {e}")  # pr
            except OSError as e:
                LOGGER.error(f"getatime: '{src}' ERROR {e}")  # pragma: no cover: defensive code

        self.remote_run(f'mv -vf "{tmp_file}" "{directory}"')  # , with_sudo=with_sudo)

    def remote_get(self, remote_file, local_file):
        LOGGER.debug(f"remote get '{remote_file}' -> '{local_file}'")
        # assuming  directory for local exists
        if self.dryrun:  # pragma: no cover
            return
        if self.ssh_connection:
            self.remote_mkdir(self.tmp_dir)
            tmp_file = self.tmp_dir + '/' + os.path.basename(local_file)
            # -p: preserve date -v: verbose -f: force (clobbers)
            self.remote_run(f'cp -pvf {remote_file} {tmp_file}')  # noqa
            sftp = self.ssh_connection.sftp()
            local_dir = os.path.dirname(local_file)  # noqa
            self.mkdirs(local_dir)
            sftp.get(tmp_file, local_file)
        else:
            LOGGER.error("trying to run a ssh command without a ssh connection",
                         f"remote get '{remote_file}' -> '{local_file}'")  # pragma: no cover: defensive code

    def remote_compute_md5(self, remote_file):
        LOGGER.debug(f"remote compute_md5 '{remote_file}'")
        if self.dryrun:
            return
        result = self.remote_run(f"md5sum '{remote_file}'")
        if result is None:
            LOGGER.internal_error(f"Unknown ssh error while remote compute_md5 '{remote_file}'")  # pragma: no cover
        if not result.ok:
            LOGGER.internal_error(f"ssh error {result.exited} while "
                                  f"remote compute_md5 '{remote_file}'")  # pragma: no cover: defensive code

        # output of md5sum: 'aa8fe00349ca160e8bf0f88f45f5cea7  /volume1/ph ... -cup.jpg'
        res = result.stdout.split()[0]
        return res

    def remote_delete(self, filename: str, msg: str = ''):
        LOGGER.trace(f"remote rm '{filename}'  {msg}")
        LOGGER.info(f"remote delete '{filename}' {msg}")
        self.remote_run(f'rm -f "{filename}"')  # if no connection, falls into remote_run() error raise

    def remote_move(self, src: str, dst: str):
        LOGGER.debug(f"remote mv '{src}' -> '{dst}'")
        # assuming  directory for remote exists
        self.remote_run(f'mv -vf "{src}"  "{dst}"')  # if no connection, falls into remote_run() error raise

    # for now, unused
    # def remote_copy(self, src: str, dst: str):
    #     LOGGER.debug(f"remote mv '{src}' -> '{dst}'")
    #     # assuming  directory for remote exists
    #     self.remote_run(f'cp -vf {src}  {dst}')     # if no connection, falls into remote_run() error raise # noqa

    def remote_rmtree(self, src: str, msg: str = ''):
        LOGGER.trace(f"remote rmdir '{src}' {msg}")
        # LOGGER.msg(f"remote rmdir '{src}' {msg}")
        self.remote_run(f'rm -rf "{src}"')  # if no connection, falls into remote_run() error raise

    def connect_ssh(self, config: dict):
        """
        :param config: configuration
        :return: Connection_done: bool, uname: str, cause:str, Error: bool
        """
        self.remote_host = config['ssh-host']
        self.remote_port = int(config['ssh-port']) if config['ssh-port'] else None
        self.remote_user = config['ssh-user']

        self.piwigo_user = config['piwigo-user']
        self.piwigo_level = config['piwigo-level']

        self.ls_output = config['ls-output']
        self.ls_command = config['ls-command']

        if self.ssh_connection is not None:
            return True, self.remote_uname, None, False

        # CAVEAT: here, we want to connect to SSH even if enable-remote-album or enable-remote-thumbnails are False,
        # because we will turn one of them True in the course of tests.

        remote = (config['remote-album'] or config['remote-thumbnails']) and self.remote_host and self.remote_port

        if not remote:
            return False, None, 'No remote parameters', False  # not connecting is not error here

        LOGGER.trace(f"connect host='{self.remote_host}' port='{self.remote_port}' user='{self.remote_user}'")
        if self.dryrun:  # pragma: no cover
            return False, None, "Dryrun", False  # not connecting is not error here

        # if config['enable-sudo'] and config['sudo-password']:
        #     ssh_config = fabric.Config(overrides={'sudo': {'password': config['sudo-password']}})
        # else:
        #     ssh_config = None

        self.ssh_connection = fabric.Connection(self.remote_host, self.remote_user, self.remote_port, )
        #                                        config=ssh_config)
        if self.ssh_connection is None:  # pragma: no cover
            LOGGER.trace("SSH error while Connecting")
            return False, None, "SSH error Connecting", True

        self.ssh_connection.open()
        # by default, self.ssh_connection.open() returns None
        if not self.ssh_connection.is_connected:  # pragma: no cover
            LOGGER.trace("SSH error while opening the connection")
            return False, None, "SSH error Connecting", True

        if sys.stdin.closed:  # pragma: no cover
            # This happened in rare conditions, with previous errors inside Paramiko, which closed stdin.
            LOGGER.debug("stdin was CLOSED, re-opening it")
            sys.stdin = open(0, "r")

        result = self.remote_run('echo $PATH')
        if result is None:  # pragma: no cover  usually, errors are discovered ahead
            # there was a serious error in run, we must abort and remember it
            self.remote_host = None
            self.remote_port = None
            self.ssh_connection = None

            return False, None, "SSH unknown error", True

        if not result.ok:  # pragma: no cover
            LOGGER.trace(f"ssh error {result.exited}")
            return False, None, f"SSH error {result.exited}", True
        res = result.stdout.strip()
        if res == "$PATH":  # pragma: no cover : having a Windows server is rare
            return True, "Windows", None, False
        else:
            result = self.remote_run('uname -rsvm')  # noqa

        uname = result.stdout.strip()
        sftp = self.ssh_connection.sftp()
        af = sftp.listdir('.')
        if self.tmp_dir in af:
            self.remote_rmtree(self.tmp_dir)
        sftp.mkdir(self.tmp_dir)
        self.remote_uname = uname
        return True, uname, None, False

    # ---------------------------------------------------------------------------------------------------
    # _________________________________ sql and md5
    #

    def sql_execute(self, query, msg, dirty=False):
        """
        Executes a SQL query
        :param query:
        :param msg: printed in case of error
        :param dirty: if True, will clean the user cache
        :return: maria_db.Cursor or None
        """
        if self.sql_connection is None:
            LOGGER.error(f"SQL Error Trying to execute without connection : {msg}")  # pragma: no cover: defensive code
            return None

        cur = self.sql_connection.cursor()
        try:
            cur.execute(query)
        except mariadb.Error as e:
            LOGGER.error(f"SQL Error {e} : {msg}")  # pragma: no cover: defensive code
        if dirty:
            LOGGER.incr_db_access()
        return cur

    def connect_sql(self, config: dict):
        """
        :param config: configuration
        :return: sql_connection, name of 1st album, error
        """
        if (not config['sql-host'] or not config['sql-port'] or not config['sql-user']
            or not config['sql-pwd']) or not config['sql-database'] or not config['enable-database'] \
                or config['dryrun']:
            return None, None, "No SQL configuration"

        if self.sql_connection and self.sql_first_album:
            return self.sql_connection, self.sql_first_album, None

        self.sql_host = config['sql-host']
        self.sql_port = int(config['sql-port'])
        self.sql_user = config['sql-user']
        self.sql_pwd = config['sql-pwd']
        self.sql_database = config['sql-database']
        self.sql_first_album = config['piwigo-album-name']
        LOGGER.debug(f"connect SQL '{self.sql_user}@{self.sql_host}:{self.sql_port}'")
        if self.sql_connection is None:
            try:
                conn = mariadb.connect(
                    user=self.sql_user,
                    password=self.sql_pwd,
                    host=self.sql_host,
                    port=self.sql_port,
                    database=self.sql_database)
            except mariadb.Error as e:
                LOGGER.trace(f"Error connecting to MariaDB Platform: {e}")  # pragma: no cover: defensive code
                self.sql_connection = None  # pragma: no cover: defensive code
                return None, None, e  # pragma: no cover: defensive code
            except NameError as e:
                LOGGER.trace(f"Error connecting to MariaDB Platform: {e}")  # pragma: no cover: defensive code
                self.sql_connection = None  # pragma: no cover: defensive code
                return None, None, e  # pragma: no cover: defensive code
            self.sql_connection = conn

        if not self.sql_first_album:
            # we need to look for it
            cur = self.sql_execute("SELECT name, id, dir, id_uppercat, uppercats, global_rank, rank, "  # noqa 
                                   " representative_picture_id \n"
                                   " FROM piwigo_categories "
                                   " WHERE global_rank=1",
                                   "get name of 1st album, something is wrong in your database ")

            for name, sql_id, path, upper, upper_cats, global_rank, rank, representative_picture_id in cur:
                self.sql_first_album = name
                self.sql_first_album_id = sql_id
                self.sql_first_album_path = path
                self.sql_first_album_upper_cat = upper
                self.sql_first_album_global_rank = global_rank
                self.sql_first_album_upper_cats = upper_cats
                self.sql_first_album_rank = rank
                self.sql_first_representative = representative_picture_id

                return self.sql_connection, name, None
            LOGGER.config_error("No Sql connection and album with global_rank=1,"
                                " please set album-name")  # pragma: no cover: defensive code

        # here, album-name is set
        cur = self.sql_execute("SELECT name, id, dir, id_uppercat, uppercats, global_rank, rank, " +  # noqa
                               " representative_picture_id \n"
                               " FROM piwigo_categories \n" +
                               f" WHERE name='{self.sql_first_album}'",
                               f" trying to get id of 1st album '{self.sql_first_album}' ")

        for name, sql_id, path, upper, upper_cats, global_rank, rank, rep_id in cur:
            upper = str(upper)  # in case this is an int
            if ',' not in upper:  # pragma: no cover
                # this is really a first level album
                self.sql_first_album_id = sql_id
                self.sql_first_album_path = path
                self.sql_first_album_upper_cat = upper
                self.sql_first_album_global_rank = global_rank
                self.sql_first_album_upper_cats = upper_cats
                self.sql_first_album_rank = rank
                self.sql_first_representative = rep_id
                return self.sql_connection, name, None

        LOGGER.config_error(f"--piwigo-album-name '{self.sql_first_album}' : "
                            " album is not known in piwigo database")  # pragma: no cover: defensive code

    @staticmethod
    def compute_md5(filename):
        h = hashlib.new('md5')
        try:
            with open(filename, "rb") as f:
                size = 2048
                while size == 2048:
                    data = f.read(2048)
                    size = len(data)
                    h.update(data)
                md5 = h.hexdigest()
            return md5
        except OSError as e:
            LOGGER.error(f"compute_md5: '{filename}' ERROR {e}")  # pragma: no cover: defensive code

    def build_sql_name(self, filename):
        if not self.sql_first_album:
            LOGGER.error("Trying to access database without proper first album set")  # pragma: no cover: defensive code
        if filename[0] != '/':
            LOGGER.error(f"db file name not starting with '/' : '{filename}' ")  # pragma: no cover: defensive code

        return "./galleries/" + self.sql_first_album + filename

    # piwigo_images
    # -------------
    #   id:     int
    #   file:   string
    #   date_available
    #   date_creation
    #   name :
    #   comment :
    #   author :
    #   hit :
    #   filesize :                  # noqa
    #   width :
    #   height :
    #   coi (center of interest) :
    #   representative_ext :
    #   date_metadata_update :
    #   rating_score :
    #   path : ./galleries/photo etc
    #   storage_category_id : int : aka ID of directory
    #   level :
    #   md5sum :
    #   added_by :  3
    #   rotation :
    #   latitude :
    #   longitude :
    #   lastmodified :           # noqa
    #

    # piwigo_groups
    # =============
    # id
    # name
    # is_default
    # last_modified

    # piwigo_group_access
    # ===================
    # group_id
    # cat_id

    # piwigo_user_cache
    # =================
    # user_id               3
    # need_update           false
    # cache_update_time
    # forbidden_categories
    # nb_total_images
    # nb_available_tags
    # nb_available_comments
    # image_access_type
    # image_access_list

    # piwigo_user_cache_categories
    # ============================
    # user_id                       3
    # cat_id                        1
    # date_last                     2023-06-27 14:26:21
    # max_date_last                 2025-01-17 16:56:42
    # nb_images                     1
    # count_images                  77130
    # nb_categories                 39
    # count_categories              2744
    # user_representative_picture_id    NULL

    def sql_get_file_info_from_id(self, requested_id: str):
        """
                get file information from the sql database, including md5
                :param requested_id: the ID of the file in the DB
                :return: FileInfo or None
                if not found, id is None
                """
        if not self.sql_connection:  # pragma: no cover
            return None

        LOGGER.debug(f"SQL get information file id = '{requested_id}'")

        cur = self.sql_execute("SELECT id, file, date_available, date_creation, name, author, filesize, " +  # noqa
                               " width, height, coi, date_metadata_update, path, storage_category_id, level, " +
                               " md5sum, added_by, latitude, longitude, representative_ext, lastmodified \n" +  # noqa
                               " FROM piwigo_images\n" +
                               f" WHERE id={requested_id}",
                               f"get file info of {requested_id} ")

        # affected_rows is always 0: no modifications

        for file_id, file, date_available, date_creation, name, author, file_size, width, height, coi, \
                date_metadata_update, path, storage_category_id, level, md5sum, added_by, latitude, longitude, \
                representative_ext, last_modified in cur:
            if file_id == requested_id:
                return FileInfo(file_id=file_id, file=file, date_available=date_available, date_creation=date_creation,
                                name=name, author=author, file_size=file_size, width=width, height=height,
                                date_metadata_update=date_metadata_update, path=path,
                                storage_category_id=storage_category_id, level=level,
                                md5sum=md5sum, added_by=added_by, latitude=latitude, longitude=longitude,
                                representative_ext=representative_ext,
                                last_modified=last_modified)
        # it is accepted to have no file with this ID
        return None

    def sql_get_file_info(self, filename: str) -> FileInfo or None:
        """
        get file information from the sql database, including md5
        :param filename: the path of the file, relative to album
        :return: FileInfo or None
        if not found, id is None
        """
        if not self.sql_connection:  # pragma: no cover
            return None

        LOGGER.debug(f"SQL get information '{filename}'")

        sql_name = self.build_sql_name(filename)

        cur = self.sql_execute("SELECT id, file, date_available, date_creation, name, author, filesize, " +  # noqa
                                " width, height, coi, date_metadata_update, path, storage_category_id, level, " +
                                " md5sum, added_by, latitude, longitude, representative_ext, lastmodified \n" +  # noqa
                                " FROM piwigo_images\n" +
                                f" WHERE path='{sql_name}'",
                                f"get file info of {sql_name} ")

        if cur.affected_rows > 1:
            LOGGER.error(f"SQL Error: get db info from {sql_name} "
                         f"produced {cur.affected_rows} affected row")  # pragma: no cover: defensive code

        for file_id, file, date_available, date_creation, name, author, file_size, width, height, coi, \
                date_metadata_update, path, storage_category_id, level, md5sum, added_by, latitude, longitude, \
                representative_ext, last_modified in cur:
            if path == sql_name:
                return FileInfo(file_id=file_id, file=file, date_available=date_available, date_creation=date_creation,
                                name=name, author=author, file_size=file_size, width=width, height=height,
                                date_metadata_update=date_metadata_update, path=path,
                                storage_category_id=storage_category_id, level=level,
                                md5sum=md5sum, added_by=added_by, latitude=latitude, longitude=longitude,
                                representative_ext=representative_ext,
                                last_modified=last_modified)
            LOGGER.error(f"""SQL Error: db already has file '{path}' 
with a different char case : '{sql_name}' 
Please change the picture or directory name to match what is already in database""")  # pragma: no cover: defensive code
        return None

    def sql_set_data(self, filename, md5, size, width, height, latitude, longitude, author,
                     warn_if_no_change=True):
        if not self.sql_connection:  # pragma: no cover
            return False

        width = width or 'NULL'
        height = height or 'NULL'
        LOGGER.debug(f"SQL SET information '{filename}'")

        sql_name = self.build_sql_name(filename)

        longitude = longitude or "NULL"
        latitude = latitude or "NULL"
        author = author or "NULL"
        date = datetime.datetime.now()  # self.format_for_sql()
        date_update = f"{date.year}-{date.month:02}-{date.day:02}"

        representative_ext = "NULL" if pathlib.Path(filename).suffix == '.jpg' else 'jpg'

        cur = self.sql_execute("UPDATE piwigo_images\n" +
                                f" SET md5sum ='{md5}', width={width}, height={height}, filesize={size},\n" +  # noqa
                                f" latitude={latitude}, longitude={longitude}, author='{author}', "
                                f" date_metadata_update='{date_update}',\n"
                                f" representative_ext='{representative_ext}' "
                                f" WHERE path='{sql_name}' """,
                                f"setting db info to {sql_name} ", dirty=True)

        if cur.affected_rows == 0 and warn_if_no_change:
            # defensive code that should not happen in normal conditions
            # but, nevertheless, no real need to stop processing
            LOGGER.info(f"Setting db info to {sql_name}: no effect, "    # pragma: no cover: defensive code
                        "values where already set to same value")
            return False                                                 # pragma: no cover: defensive code

        if cur.affected_rows > 1:
            # defensive code that should not happen in normal conditions
            # but, nevertheless, no real need to stop processing
            LOGGER.error(f"SQL Error: setting db info to {sql_name} "
                         f"produced {cur.affected_rows} affected row")  # pragma: no cover: defensive code
        return True

    def sql_get_user_id(self, username: str):
        if not self.sql_connection:
            # not self.sql_connection is supposed to have been trapped ahead
            LOGGER.internal_error("sql_get_user_id without SQL connection")  # pragma: no cover: defensive code

        LOGGER.debug(f"SQL get user id '{username}'")

        cur = self.sql_execute("SELECT id, username \n"
                               " FROM piwigo_users "
                               f" WHERE username='{username}'",
                               f"get user id '{username}'")

        if cur.affected_rows > 1:
            LOGGER.error(f"SQL Error: get user id '{username}' "
                         f"produced {cur.affected_rows} affected row")  # pragma: no cover: defensive code

        for index, name in cur:
            if name == username:
                return index

        LOGGER.config_error(f"--piwigo-user '{username}': "
                            "sql_get_user_id not found")  # pragma: no cover: defensive code

    def sql_insert_file(self, real_file: str, sql_filename: str,
                        allowed_groups: dict[str, int]) -> FileInfo or None:
        """
        insert sql_filename in the sql database, potentially creates the enclosing dir in the DB
        :param real_file: the path of the file to be inserted
        :param sql_filename: the path of the file, relative to album
        :param allowed_groups: dict of groups that should have access
        :return: sql_get_file_info()
        """
        if not self.sql_connection:
            return None  # pragma: no cover    : defensive code
        LOGGER.debug(f"SQL insert file '{sql_filename}'")

        file = os.path.basename(sql_filename)

        try:
            date_available = datetime.datetime.now()  # self.format_for_sql()
            date_creation = datetime.datetime.fromtimestamp(os.path.getmtime(real_file))
            name = file
            file_size = int(os.path.getsize(real_file) / 1024)
        except OSError as e:
            LOGGER.error(f"getmtime: '{real_file}' ERROR {e}")  # pragma: no cover: defensive code
            return None

        path = self.build_sql_name(sql_filename)

        father = os.path.dirname(sql_filename)
        father_info = self.sql_get_dir_info(father, allowed_groups, do_insert=True)

        if father_info is None:
            LOGGER.error(f"SQL Error: insert file '{sql_filename}' "
                         f"father '{father}' does not exist in db")  # pragma: no cover: defensive code

        level = self.piwigo_level
        added_by = self.sql_get_user_id(self.piwigo_user)

        # width and height will be inserted afterward, with author and other metadata
        representative_ext = '' if pathlib.Path(file).suffix == '.jpg' else 'jpg'

        src_md5 = ACTOR.compute_md5(real_file)

        # NB: other fields in the DB depend on the analysis of the file: jpg, mp4, etc...
        # inserting these values is done elsewhere
        date = datetime.datetime.now()  # self.format_for_sql()
        date_update = f"{date.year}-{date.month:02}-{date.day:02}"

        cur = self.sql_execute("INSERT INTO piwigo_images \n" +
                                f' SET file="{file}", date_available="{date_available}", '
                                f' date_creation="{date_creation}", ' +
                                f' name="{name}", filesize={file_size}, path="{path}", ' +  # noqa
                                f' storage_category_id={father_info.dir_id}, level={level}, '
                                f" date_metadata_update='{date_update}', " +  # noqa
                                f" added_by={added_by}, md5sum='{src_md5}', representative_ext='{representative_ext}'",
                                f"insert file '{sql_filename}'", dirty=True)

        if cur.affected_rows > 1:
            LOGGER.error(f"SQL Error: insert file '{sql_filename}' "
                         f"produced {cur.affected_rows} affected row")  # pragma: no cover: defensive code

        all_files = self.sql_get_dir_file_list(father_info)
        if file not in all_files:
            LOGGER.error(f"SQL Error: insert file '{sql_filename}' not inserted")  # pragma: no cover: defensive code

        sql_file_info: FileInfo = all_files[file]
        cur = self.sql_execute("INSERT INTO piwigo_image_category \n"
                               f" SET image_id={sql_file_info.file_id}, category_id={father_info.dir_id}",
                               f" insert file category_id'{sql_filename}'", dirty=True)

        if cur.affected_rows > 1:
            LOGGER.error(f"SQL Error: set file category_id '{sql_filename}' "
                         f"produced {cur.affected_rows} row")  # pragma: no cover: defensive code

        return sql_file_info

    #   images: piwigo_image_category:
    #       image_id:                                                                                   yes
    #       category_id:                                                                                yes
    #       rank:               SET ONLY for the picture that are representative of album <> from their dir.
    #       SELECT * FROM `piwigo_image_category` WHERE rank <> 'null'
    #           image_id = 15239, rank = 1, category_id = 1
    #           this is 2006-04-29-07h57-05-Aghios Nikolaios et Route.jpg                                                 # noqa
    #           representative of album

    #   directories: piwigo_categories
    #       id:                                                                             3
    #       name: defaults to dirname, without path                                      2003-07-Juillet-28-bord de mer   # noqa
    #       id_uppercat: null for root(i.e. photos), 1 for first level dir etc...          2 (id of 2003)                 # noqa
    #       comment:                                                                        NULL
    #       dir: dirname, without path                                                   2003-07-Juillet-28-bord de mer   # noqa
    #       rank: index in the enclosing dir, starting at 1                                 31
    #       status: private or public, defaults to private                                  private
    #       site_id: index of the root album, defaults to 1                                 1
    #       visible: true/false, defaults to true                                           true
    #       representative_picture_id: defaults to null                                     271
    #       uppercats: list of categories in path, separated by ',',                        1,2,3                         # noqa
    #       commentable: true/false, defaults to true                                       true
    #       global_rank: list of ranks, separated by '.', starting from root.               1.12.31
    #                    builds a strict order of directories
    #       image_order: defaults to NULL                                                   NULL
    #       permalink:  defaults to NULL                                                    NULL
    #       lastmodified : automatically set                                                2024-01-08 22:04:45           # noqa

    def sql_get_dir_info(self, sql_path, allowed_groups: dict[str, int],
                         father_info=None, do_insert=False) -> DirInfo or None:
        """
        sql_get_dir_info(self, sql_path, father_path="", father_id=1)

        :param sql_path: the path of the directory inside the father. if father is None, from root after photo
        :param father_info: info of the father.
        :param do_insert: if True, inserts the dir when absent
        :param allowed_groups: dict of groups that should have access
        :return: DirDescr
        """
        if not self.sql_connection:
            return None  # pragma: no cover: defensive code

        LOGGER.debug(f"SQL get dir id '{father_info}'/'{sql_path}'")

        if sql_path[0] == '/':
            sql_path = sql_path[1:]

        if '/' in sql_path:
            dir_name = sql_path.split('/')[0]
            path_len = len(dir_name) + 1
            next_path = sql_path[path_len:]
        else:
            dir_name = sql_path
            next_path = ""

        if father_info is None:
            father_info = DirInfo(name=self.sql_first_album,
                                  path=self.sql_first_album,
                                  dir_id=self.sql_first_album_id,
                                  rank=self.sql_first_album_rank,
                                  id_upper_cat=self.sql_first_album_upper_cat,
                                  upper_cats=self.sql_first_album_upper_cats,
                                  global_rank=self.sql_first_album_global_rank,
                                  representative_picture_id=self.sql_first_representative)

        sql_sons_descr = ACTOR.sql_get_dir_sub_dirs(father_info)

        if dir_name in sql_sons_descr.keys():
            son = sql_sons_descr[dir_name]
        elif do_insert:
            son = self.sql_insert_dir_and_reorder(dir_name, father_info, sql_sons_descr, allowed_groups)
        else:
            # dir_name was not found in father
            return None

        assert son, f"directory {dir_name} inserted incorrectly in {father_info}"
        if next_path == "":
            # we have reached the last item
            return son
        return self.sql_get_dir_info(next_path, allowed_groups, son, do_insert=do_insert)

    def sql_set_dir_representative(self, dir_info: DirInfo, file_id):
        LOGGER.trace(f"SQL Set dir {dir_info.dir_id} representative '{file_id}'")

        cur = self.sql_execute(" UPDATE piwigo_categories \n"
                                f' SET representative_picture_id="{file_id}" \n'  # noqa
                                f" WHERE id={dir_info.dir_id}",
                                f"Set dir {dir_info} representative '{file_id}'", dirty=True)

        if cur.affected_rows != 1:
            LOGGER.error(f"SQL Error: {cur.affected_rows} affected rows "
                         f"while Set dir {dir_info} rep '{file_id}'")  # pragma: no cover: defensive code

    #
    # piwigo_groups
    # -------------
    # id            int
    # name          string
    # is_default    bool
    # lastmodified  date    # noqa
    #
    # piwigo_group_access
    # -------------------
    # group_id      int
    # cat_id        int

    def sql_get_group_id(self, group_name):
        """
        Get the ID of group_name
        :param group_name:
        :return: ID
        """
        LOGGER.debug(f"SQL get group ID '{group_name}'")

        cur = self.sql_execute("SELECT id, name \n"
                               " FROM `piwigo_groups` "
                               f" WHERE name='{group_name}' ",
                               f"getting SQL get group ID '{group_name}'")

        for group_id, read_group_name in cur:
            if read_group_name == group_name:
                return group_id
        LOGGER.error(f"Group '{group_name}' not found while getting its group ID \n"
                     "probable cause: 'piwigo-groups-enabled' value is wrong"
                     )     # pragma: no cover: defensive code
        return 0                                                         # pragma: no cover: defensive code

    def sql_set_group_access_to_dir(self, group_name, group_id, cat_id):
        """
        Enables group with id group_id to access to directory with cat_id
                only if this was not already set
        :param group_name: name of group
        :param group_id: ID inside database
        :param cat_id:  ID inside database
        :return: None
        """
        if not self.sql_connection:  # pragma: no cover
            return None
        LOGGER.debug(f"SQL set group {group_id} access to {cat_id}")

        cur = self.sql_execute("SELECT group_id FROM piwigo_group_access \n" +
                               f' WHERE group_id="{group_id}" and cat_id="{cat_id}"',
                               f"SQL verify group {group_name} access to {cat_id}")

        for _ in cur:
            # the authorization is already set
            return

        cur = self.sql_execute("INSERT INTO piwigo_group_access \n" +
                               f' SET group_id="{group_id}", cat_id="{cat_id}"',
                               f"SQL set group {group_name} access to {cat_id}", dirty=True)

        if cur.affected_rows != 1:
            LOGGER.error(f"SQL Error: {cur.affected_rows} affected rows "
                         f"set group {group_id} access to {cat_id}")  # pragma: no cover: defensive code

    def sql_insert_dir_at_rank(self, dir_name: str, father_info: DirInfo, rank,
                               allowed_groups: dict[str, int]) -> DirInfo or None:
        """
        inserts dir_name inside father, which is not None
        Also reorders sons of father in increasing order
        CAVEAT: Does NOT check if other sons (in db) are also valid subdirectories (i.e. dir exist in filesystem)
        CAVEAT: does NOT reorder the sons

        :param dir_name: dir-name, without the full path
        :param father_info:
        :param rank: new rank
        :param allowed_groups: dict of groups that should have access
        :return: DirInfo
        """

        if not self.sql_connection:  # pragma: no cover
            return None
        LOGGER.debug(f"SQL insert dir {dir_name} in '{father_info}' at rank {rank} ")

        if not father_info:
            LOGGER.internal_error(f"NULL father for {dir_name}, rank={rank}")  # pragma: no cover: defensive code

        # CAVEAT: upper_cats ends with the directory OWN ID, that we do not know until it is created !
        global_rank = str(father_info.global_rank) + '.' + str(rank)
        cur = self.sql_execute("INSERT INTO piwigo_categories \n" +
                                f' SET name="{dir_name}", id_uppercat="{father_info.dir_id}", \n' +  # noqa
                                f' dir="{dir_name}", rank={rank}, status="private", site_id=1, \n' +
                                ' visible="true", commentable="true", \n' +
                                f' global_rank="{global_rank}" ',
                                f"INSERT dir {dir_name} in {father_info}", dirty=True)
        # image_order="NULL", permalink="null"
        # NB: RETURNING does not seem to be supported on all mariaDB implementations.
        # NB: uppercats=CONCAT("{father_info.upper_cats}", ",", id), does not work, id=0 # noqa

        if cur.affected_rows != 1:
            LOGGER.error(f"SQL Error: "
                         f"{cur.affected_rows} affected rows inserting dir {dir_name} ")  # pragma: no cover: defensive

        info = self.sql_get_dir_info(dir_name, allowed_groups, father_info=father_info, do_insert=False)
        if info is None:
            LOGGER.internal_error(f"SQL error dir {dir_name} not correctly inserted")  # pragma: no cover defensive code

        upper_cats = str(father_info.upper_cats) + ',' + str(info.dir_id)

        self.sql_execute(" UPDATE piwigo_categories \n" +
                         f' SET uppercats="{upper_cats}" \n' +  # noqa
                         f" WHERE id={info.dir_id}",
                         f"UPDATING uppercats for dir {dir_name} ", dirty=True)  # noqa

        info = self.sql_get_dir_info(dir_name, allowed_groups, father_info=father_info, do_insert=False)
        # we verify upper cats were inserted correctly
        if info is None:
            LOGGER.internal_error(f"SQL error dir {dir_name} "
                                  "not correctly inserted after update of upper cats")  # pragma: no cover: defensive

        if dir_name != "pwg_representative":
            for group_name in allowed_groups:
                self.sql_set_group_access_to_dir(group_name, allowed_groups[group_name], info.dir_id)

        LOGGER.trace(f"inserted dir '{dir_name}:{info.dir_id}' into database, uppercats = '{upper_cats}'")  # noqa
        return info

    def sql_insert_dir_and_reorder(self, dir_name, father_info: DirInfo, sql_sons_descr,
                                   allowed_groups: dict[str, int]) -> DirInfo:
        """
        inserts dir_name inside father, which is not None
        Also reorders sons of father in increasing order
        CAVEAT: Does NOT check if other sons (in db) are also valid subdirectories (i.e. dir exist in filesystem)

        :param dir_name: dir-name, without the full path
        :param father_info:
        :param sql_sons_descr:
        :param allowed_groups: dict of groups that should have access
        :return: DirInfo
        """

        file_list = list(sql_sons_descr.keys())
        file_list.append(dir_name)
        file_list.sort()
        info = None
        rank = 1
        for file in file_list:
            if file == dir_name:
                info = self.sql_insert_dir_at_rank(dir_name, father_info, rank, allowed_groups)
            else:
                son_info = sql_sons_descr[file]
                self.sql_change_dir_rank(father_info, son_info, rank)
            rank += 1

        return info

    def sql_change_dir_rank(self, father_info: DirInfo, son_info: DirInfo, new_rank):
        if not self.sql_connection:
            return None  # pragma: no cover: defensive code
        old_rank = son_info.rank
        if new_rank == old_rank:
            return son_info

        LOGGER.debug(f"SQL change dir {son_info} rank in '{father_info}'  {son_info.rank} -> {new_rank} ")

        le = len(str(old_rank)) + 1
        new_global_rank = str(son_info.global_rank)[:-le] + '.' + str(new_rank)

        cur = self.sql_execute("UPDATE piwigo_categories\n" +
                                f" SET rank='{new_rank}', global_rank='{new_global_rank}' \n" +
                                f" WHERE dir='{son_info.name}' and id_uppercat={father_info.dir_id}",  # noqa
                                f"change dir {son_info} rank {old_rank} -> {new_rank} in {father_info}",
                                dirty=True)

        if cur.affected_rows != 1:
            LOGGER.error(f"SQL Error: {cur.affected_rows} affected rows, change dir {son_info} "
                         f"rank in {father_info}")  # pragma: no cover: defensive code
        return True

    def sql_get_dir_file_list(self, dir_info: DirInfo) -> dict[str, FileInfo]:
        """
        sql_get_dir_file_list(self, path):
        :param dir_info: dir we are looking in the database
        :return: dictionary of files: result[basename]= FileInfo
        """
        if self.sql_connection is None or self.sql_connection is False:
            return {}  # pragma: no cover: defensive code

        if dir_info is None:
            return {}  # pragma: no cover

        LOGGER.debug(f"SQL get dir files '{dir_info}'")

        cur = self.sql_execute("SELECT id, file, date_available, date_creation, name, author, filesize, " +  # noqa
                               " width, height, date_metadata_update, path, storage_category_id, level, " +
                               " md5sum, added_by, latitude, longitude, representative_ext, lastmodified \n" +  # noqa
                               " FROM piwigo_images\n" +
                               f" WHERE storage_category_id={dir_info.dir_id}",
                               f"getting sql files of dir {dir_info}")

        result = {}

        for file_id, file, date_available, date_creation, name, author, file_size, width, height, \
                date_metadata_update, path, storage_category_id, level, md5sum, added_by, latitude, longitude, \
                representative_ext, last_modified in cur:
            father = os.path.dirname(path)
            if father != './galleries/' + dir_info.path:
                LOGGER.error(f"incoherent father '{father}' for file {file}:{id}")  # pragma: no cover: defensive code
            result[file] = FileInfo(file_id=file_id, file=file, date_available=date_available,
                                    date_creation=date_creation,
                                    name=name, author=author, file_size=file_size, width=width, height=height,
                                    date_metadata_update=date_metadata_update, path=path,
                                    storage_category_id=storage_category_id, level=level,
                                    md5sum=md5sum, added_by=added_by, latitude=latitude, longitude=longitude,
                                    representative_ext=representative_ext,
                                    last_modified=last_modified)

        return result

    def sql_get_dir_sub_dirs(self, dir_info: DirInfo):
        """
        sql_get_dir_sub_dirs(self, path):
        :param dir_info: info about dir we are looking in the database
        :return: dictionary of subdirectories: result[basename]= DirInfo
        """
        if not self.sql_connection:
            return {}  # pragma: no cover: defensive code

        if dir_info is None:
            return {}  # pragma: no cover

        LOGGER.debug(f"SQL get dir sub-dirs '{dir_info}'")

        cur = self.sql_execute("SELECT id, dir, rank, id_uppercat, global_rank, uppercats, " +  # noqa
                               " representative_picture_id \n"
                               " FROM piwigo_categories \n" +
                               f" WHERE id_uppercat={dir_info.dir_id}",  # noqa
                               f"getting sql files of dir {dir_info}")

        result = {}
        for sql_id, sql_dir, sql_rank, sql_upper, sql_global, upper_cats, rep_id in cur:
            new_path = dir_info.path + '/' + sql_dir
            result[sql_dir] = DirInfo(name=sql_dir, path=new_path, dir_id=sql_id, rank=sql_rank,
                                      id_upper_cat=sql_upper, global_rank=sql_global, upper_cats=upper_cats,
                                      representative_picture_id=rep_id)
        return result

    def sql_get_dir_category_content(self, dir_info: DirInfo):
        if not self.sql_connection:
            return None  # pragma: no cover: defensive code

        cur = self.sql_execute("SELECT image_id, rank \n"
                               " FROM piwigo_image_category "
                               f" WHERE category_id={dir_info.dir_id}",
                               f"getting dir {dir_info} content as a category")

        result = {}
        for sql_id, rank in cur:
            result[sql_id] = {'id': sql_id, 'rank': rank}
        return result

    def sql_remove_file_from_db(self, p_config: dict, file_info: FileInfo):
        if not self.sql_connection:
            return True  # pragma: no cover: defensive code

        LOGGER.msg(f"Database: Remove {file_info}")
        real_path = p_config["album"] + '/' + file_info.path

        if self.isfile(real_path):
            LOGGER.error(f"Error: file {real_path} prevents from removing "
                         f"{file_info} from database")  # pragma: no cover: defensive code

        self.sql_execute("DELETE FROM piwigo_images \n"
                         f" WHERE id={file_info.file_id}",
                         f"removing file {file_info} ", dirty=True)

        cur = self.sql_execute("DELETE FROM piwigo_image_category \n"
                               f" WHERE image_id={file_info.file_id}""",
                               f"while removing file {file_info} ", dirty=True)

        if cur.affected_rows != 1:
            LOGGER.error(f"SQL Error: {cur.affected_rows} affected rows "
                         f"removing {file_info}'")  # pragma: no cover: defensive code
        return True

    def sql_remove_dir_from_db(self, dir_info: DirInfo):
        """
        sql_remove_dir_from_db(self, dir_info: DirInfo):
        :param dir_info:  directory to remove from DB
        :return: True

        CAVEAT: if the directory is NOT empty, use sql_remove_dir_from_database_recursive
        """

        if not self.sql_connection:
            return False  # pragma: no cover: defensive code

        # first, test that all pictures and subdirectories have been deleted from database

        LOGGER.msg(f"Database: Remove {dir_info}")

        sql_file_descr = ACTOR.sql_get_dir_file_list(dir_info)
        if sql_file_descr:  # pragma: no cover: defensive code
            for file in sql_file_descr:
                LOGGER.info(f"found file {file}")
            LOGGER.error(f"SQL Error removing directory {dir_info} : "
                         "still holds files in DB")  # pragma: no cover: defensive code

        sql_file_descr = ACTOR.sql_get_dir_category_content(dir_info)
        if sql_file_descr:  # pragma: no cover: defensive code
            for file in sql_file_descr:
                LOGGER.info(f"found file {file}")
            LOGGER.error(f"SQL Error removing category {dir_info} : "
                         "still holds files in DB")  # pragma: no cover: defensive code

        sql_sons_descr = ACTOR.sql_get_dir_sub_dirs(dir_info)
        if sql_sons_descr:  # pragma: no cover: defensive code
            for file in sql_sons_descr:
                LOGGER.info(f"found subdir {file}")
            LOGGER.error(f"SQL Error removing directory {dir_info} : "
                         "still holds directories in DB")  # pragma: no cover: defensive code

        # then, do remove

        cur = self.sql_execute("DELETE FROM piwigo_categories \n"
                               f" WHERE id={dir_info.dir_id}",
                               f"removing directory {dir_info}", dirty=True)

        if cur.affected_rows != 1:
            LOGGER.error(f"SQL Error: {cur.affected_rows} affected rows "
                         f"removing directory {dir_info}")  # pragma: no cover: defensive code

        self.sql_execute("DELETE FROM piwigo_group_access \n"
                         f" WHERE cat_id={dir_info.dir_id}",
                         f"removing directory {dir_info} from piwigo_group_access", dirty=True)
        return True

    def sql_remove_dir_from_database_recursive(self, p_config: dict, dir_info: DirInfo):
        """
        sql_remove_dir_from_database_recursive
        :param p_config:
        :param dir_info: dir to remove
        :return: True

        Called when a directory is empty on the file system, but still has items in the database
        recursively deletes all sons,
        then deletes the dir itself

        while deleting the sons (directory and file), it is verified that these do not exist anymore in the filesystem
        so this method is safe
        """
        sql_file_descr = ACTOR.sql_get_dir_file_list(dir_info)
        for file in sql_file_descr:
            ACTOR.sql_remove_file_from_db(p_config, sql_file_descr[file])
            # will yell if the file still exists

        sql_sons_descr = ACTOR.sql_get_dir_sub_dirs(dir_info)
        for subdir in sql_sons_descr:
            self.sql_remove_dir_from_database_recursive(p_config, sql_sons_descr[subdir])
            # will yell if there are still files, but NOT if there are empty directories

        self.sql_remove_dir_from_db(dir_info)

    def sql_clear_user_caches(self):
        if LOGGER.db_access == 0:
            return False

        LOGGER.msg("Database: Clear cache")
        self.sql_execute("DELETE FROM piwigo_user_cache \n"
                         " WHERE 1", "while clear user cache")
        self.sql_execute("DELETE FROM piwigo_user_cache_categories \n "
                         "WHERE 1", "while clear user cache")

    # def trace_malloc_start(self):
    #     gc.enable()
    #     if not self.trace_malloc:
    #         return
    #     tracemalloc.start()      # noqa
    #
    # def trace_malloc_snapshot(self, name: str, snapshot1: tracemalloc.Snapshot or None = None, garbage=False):     # noqa
    #     if garbage:
    #         gc.collect(2)
    #     if not self.trace_malloc:
    #         return None
    #     LOGGER.msg("*** start gc garbage ***")
    #     LOGGER.msg(gc.garbage)
    #     LOGGER.msg("*** end gc garbage ***")
    #     snapshot2 = tracemalloc.take_snapshot()       # noqa
    #     if snapshot1:
    #         top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    #         LOGGER.msg(f"{name} : [ Top 10 differences ]")
    #         for item in top_stats[:10]:
    #             LOGGER.msg(item)
    #     return snapshot2


ACTOR = PwpActor()
