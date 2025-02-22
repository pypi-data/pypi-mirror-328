from pydantic import BaseModel,Field
from scilens.config.models.reader_format_txt import ReaderTxtIgnoreConfig,ReaderTxtConfig
from scilens.config.models.reader_format_csv import ReaderCsvConfig
from scilens.config.models.reader_format_netcdf import ReaderNetcdfConfig
class ReadersConfig(BaseModel):txt:ReaderTxtConfig=Field(default=ReaderTxtConfig(),description='Configuration des readers txt.');csv:ReaderCsvConfig=Field(default=ReaderCsvConfig(),description='Configuration des readers csv.');netcdf:ReaderNetcdfConfig=Field(default=ReaderNetcdfConfig(),description='Configuration des readers NetCDF.')