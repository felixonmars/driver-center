from driver_center.data_source import DataSource
from driver_center.util import fetch_file


class AlsaDataSource(DataSource):
    def collect(self):
        return fetch_file("/proc/asound/cards")
