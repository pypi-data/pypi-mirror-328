import shutil
import os
from typing import Union
from pathlib import Path


class Config:
    config_home: os.PathLike = None
    config_log: os.PathLike = None
    config_config: os.PathLike = None


def __set_path(attr_name, path: Union[str, os.PathLike]):
    path = Path(path)
    # if not os.path.exists(path):
    #     raise RuntimeError(f"path: {path} does not exist.")
    class_obj = globals()["Config"]
    setattr(class_obj, attr_name, path)


def set_home(path: Union[str, os.PathLike]):
    """Configure the main directory of Swordfish.

    Parameters
    ----------
    path : Union[str, os.PathLike]
        The directory where configuration files, license files,
        log files, and other related dependency files are located.
    """
    __set_path("config_home", path)


def set_log(path: Union[str, os.PathLike]):
    """Configure the log file path of Swordfish.

    Parameters
    ----------
    path : Union[str, os.PathLike]
        The path and name of the log file. The log file contains
        detailed information about server configuration, warnings, and error messages.
    """
    __set_path("config_log", path)


def set_config(path: Union[str, os.PathLike]):
    """Configure the config file path of Swordfish.

    Parameters
    ----------
    path : Union[str, os.PathLike]
        The path and name of the config file.
    """
    __set_path("config_config", path)


def __check_and_copy__(file: str, src: Path, dst: Path):
    src_file = src / file
    dst_file = dst / file
    if not dst_file.exists():
        if src_file.is_dir():
            shutil.copytree(src_file, dst_file)
        else:
            shutil.copyfile(src_file, dst_file)


__file_list = ["dolphindb.cfg", "dolphindb.dos"]
if os.name == "nt":
    __file_list.append("tzdb")


def convert_config():
    args = []

    if Config.config_home:
        home_path = Path(Config.config_home)
    else:
        home_path = Path(os.getcwd())
    src_path = Path(__file__).parent
    for file in __file_list:
        __check_and_copy__(file, src_path, home_path)
    arg_strs = ["-home", f"{home_path}"]
    args += arg_strs

    if Config.config_log:
        arg_strs = ["-logFile", f"{Config.config_log}"]
        args += arg_strs

    if Config.config_config:
        arg_strs = ["-config", f"{Config.config_config}"]
        args += arg_strs

    return args
