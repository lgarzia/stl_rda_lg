# Stores all values to support web scrapping
import enum

WEB_SCRAPPER_CONF = [
    {
        "hdir": "rda_datasets",
        "bdir": "WhereWeStand-8thEditionData",
        "bdir_1": "demographics",
        "fname": "wws08_data_Demographics_2020-03-27.csv",
        "ftype": "csv",
        "url": r"https://rdx.stldata.org/dataset/where-we-stand-8th-edition-data/resource/fcb9c4b2-6754-4f4f-998e-281befe7b523",
        "dl_type": "click_download",
        "xpath": r"//a[contains(@title, 'Demographics')][contains(@href, 'ewgateway')]",
    }
]


# %%
import enum


class Dl_types(enum.Enum):
    click_download: str = "click_download"
    api_call: str = "api_call"


# %%
