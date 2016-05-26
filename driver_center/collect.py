from pkg_resources import iter_entry_points


def collect():

    result = {}

    for entry_point in iter_entry_points(group='driver_center.data_sources', name=None):
        data_source = entry_point.load()()

        name = entry_point.name
        data = data_source.collect()

        if not isinstance(data, dict):
            raise ValueError("Data source must return an instance of dict in collect()")

        filtered_data = data_source.filter(data)

        if not isinstance(filtered_data, dict):
            raise ValueError("Data source must return an instance of dict in filter()")

        result[name] = filtered_data

    return result
