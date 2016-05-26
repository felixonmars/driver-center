import abc
import six


@six.add_metaclass(abc.ABCMeta)
class DataSource(object):

    @abc.abstractmethod
    def collect(self):
        raise NotImplementedError

    def filter(self, data):
        return data
