import pytest
from stl_rda_lg.web_scraper.web_scrapper_conf import WEB_SCRAPPER_CONF, Dl_types
import stl_rda_lg.web_scraper as ws
from pathlib import Path
import os


def test_conf_import():
    assert WEB_SCRAPPER_CONF


def test_get_flat_file():
    inp_ = [{"dl_type": "click_download"}, {"dl_type": "api"}]
    res_ = ws.get_all_files_by_dl_type(Dl_types.click_download, conf=inp_)
    assert res_ == [{"dl_type": "click_download"}]


# TODO Parameterize
@pytest.fixture()
def d_input():
    return {
        "hdir": "rda_datasets",
        "bdir": "WhereWeStand-8thEditionData",
        "bdir_1": "demographics",
        "fname": "wws08_data_Demographics_2020-03-27.csv",
        "ftype": "csv",
        "url": r"https://rdx.stldata.org/dataset/where-we-stand-8th-edition-data/resource/fcb9c4b2-6754-4f4f-998e-281befe7b523",
        "dl_type": "click_download",
    }


@pytest.fixture()
def remove_directory(d_input):
    res_ = ws.build_data_directory(d_input)
    if res_.exists():
        res_.rmdir()
    yield
    res_.rmdir()


def test_build_data_dir(d_input):
    input = d_input
    # remove_directory
    res_ = ws.build_data_directory(input)
    assert res_ == Path(
        os.path.join(
            os.getcwd(), "rda_datasets", "WhereWeStand-8thEditionData", "demographics"
        )
    )
