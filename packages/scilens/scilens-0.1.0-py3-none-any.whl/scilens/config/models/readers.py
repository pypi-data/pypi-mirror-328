from pydantic import BaseModel,Field
from scilens.config.models.reader_format_txt import ReaderTxtIgnoreConfig,ReaderTxtConfig
from scilens.config.models.reader_format_csv import ReaderCsvConfig
class ReadersConfig(BaseModel):txt:ReaderTxtConfig=Field(default=ReaderTxtConfig(),description='Configuration des readers txt.');csv:ReaderCsvConfig=Field(default=ReaderCsvConfig(),description='Configuration des readers csv.')