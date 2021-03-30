"""Main module to support Web Scrapping/Downloading File"""
from .web_scrapper_conf import WEB_SCRAPPER_CONF, Dl_types
from typing import Dict, List, Optional
import os
from pathlib import Path


def get_all_files_by_dl_type(
    dl_type: Dl_types, conf: Optional[List[Dict[str, str]]] = None
) -> List[Dict[str, str]]:
    """helper function to parse config; returns all file based on download type

    args:
        dl_type: specify download types
        conf: optional configuration overide default
    """

    results = [d for d in (conf or WEB_SCRAPPER_CONF) if d["dl_type"] == dl_type.value]
    return results


def build_data_directory(d_conf: Dict[str, str]) -> Path:
    """Assemble Directory to build path

    args:
        d_conf: instance of data
    """
    dirs_ = [v for k, v in d_conf.items() if "dir" in k]
    p = Path(os.getcwd())
    for d in dirs_:
        p = p.joinpath(d)
    return p


def extract_click_download_file(st: Path, d_conf: Dict[str, str]) -> None:
    pass