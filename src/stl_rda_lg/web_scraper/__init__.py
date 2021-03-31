"""Main module to support Web Scrapping/Downloading File"""
import selenium
from .web_scrapper_conf import WEB_SCRAPPER_CONF, Dl_types
from typing import Dict, List, Optional
import os
import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
import time


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


def build_data_directory_path(d_conf: Dict[str, str]) -> Path:
    """Assemble Directory to build path

    args:
        d_conf: instance of data
    """
    dirs_ = [v for k, v in d_conf.items() if "dir" in k]
    p = Path(os.getcwd())
    for d in dirs_:
        p = p.joinpath(d)
    return p


def make_data_directory_path(path: Path) -> None:
    """Creates Directory"""
    path.mkdir(parents=True, exist_ok=True)


def click_download_file_(url: str, xpath: str, download_dir: Path) -> None:
    """Internal Function to execute download csv in headless chrome

    Args:
        url: Website of CSV download
        xpath: find tag element
        download_path: where to store file
    """
    #    chrome_driver = r"C:\Users\lgarzia\Documents\projects\stl_rda_lg\src\stl_rda_lg\web_scraper\chromedriver.exe"
    chrome_driver = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
    # sys.path.insert(0, ph_path)
    # print(sys.path[:5])
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(
        chrome_options=chrome_options,
        executable_path=chrome_driver,
    )

    driver.get(url)
    e = driver.find_element_by_xpath(xpath=xpath)

    if not isinstance(e, WebElement):
        raise ValueError("Result is not WebElement")

    print(e.tag_name, e.text, e.get_attribute("href"))

    params = {"behavior": "allow", "downloadPath": str(download_dir)}
    driver.execute_cdp_cmd("Page.setDownloadBehavior", params)
    e.click()
    time.sleep(3)
    driver.quit()


def extract_click_download_file(download_dir: Path, d_conf: Dict[str, str]) -> Path:
    click_download_file_(d_conf["url"], d_conf["xpath"], download_dir)
    fpath = download_dir.joinpath(d_conf["fname"])
    return fpath


def run_download_process():
    print("running extract")
    dl = get_all_files_by_dl_type(Dl_types.click_download)
    for d in dl:
        p = build_data_directory_path(d)
        make_data_directory_path(p)
        # stuff data in here
