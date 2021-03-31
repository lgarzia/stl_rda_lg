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
    res_ = ws.build_data_directory_path(d_input)
    if res_.exists():
        res_.rmdir()
    yield
    n_dir = len([v for k, v in d_input.items() if "dir" in k])
    res_.rmdir()  # delete data dir
    for i in range(n_dir - 1):
        print(i)
        p = res_.parents[i]
        p.rmdir()


def test_build_data_dir_path(d_input):
    input = d_input
    # remove_directory
    res_ = ws.build_data_directory_path(input)
    assert res_ == Path(
        os.path.join(
            os.getcwd(), "rda_datasets", "WhereWeStand-8thEditionData", "demographics"
        )
    )


@pytest.mark.skip(reason="validating directory will work")
def test_make_data_dir(remove_directory, d_input):
    input = d_input
    # remove_directory
    res_ = ws.build_data_directory_path(input)
    ws.make_data_directory_path(res_)
    assert res_.exists()


def test_download_file_exists(tmpdir):
    import os

    d_conf = {
        "fname": "wws08_data_Demographics_2020-10-02.csv",
        "url": r"https://rdx.stldata.org/dataset/where-we-stand-8th-edition-data/resource/fcb9c4b2-6754-4f4f-998e-281befe7b523",
        "xpath": r"//a[contains(@title, 'Demographics')][contains(@href, 'ewgateway')]",
    }
    fname = os.path.join(tmpdir, d_conf["fname"])
    fname_p = ws.extract_click_download_file(Path(tmpdir), d_conf)
    assert fname_p.exists()