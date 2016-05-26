import hashlib
from driver_center.data_source import DataSource
from driver_center.util import run_cmd


class BootDataSource(DataSource):
    def collect(self):
        result = run_cmd("journalctl --list-boots")

        for cmd in result:
            raw_data = result[cmd].decode('utf-8')

            data = []
            for line in raw_data.split("\n"):
                line = line.split()
                if len(line) != 9:
                    continue

                line[5:6] = line[5].split("-")
                data.append({
                    "boot-id": line[1],
                    "start": " ".join(line[2:6]),
                    "end": " ".join(line[6:10]),
                })

            result[cmd] = data

        return result

    def filter(self, data):
        for cmd in data:
            for item in data[cmd]:
                item["boot-id"] = hashlib.sha256(item["boot-id"].encode('utf-8') + b"driver_center encoded").hexdigest()

        return data
