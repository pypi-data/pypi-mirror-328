from pathlib import Path
import pickle

from pyPhases.exporter.DataExporter import DataExporter
from pyPhases.Data import DataNotFound


class PickleExporter(DataExporter):
    supportedTypes = []

    try:
        import numpy

        supportedTypes.append(numpy.ndarray)
    except ImportError:
        pass

    """ An Exporter that supports a lot of default formats using pickle"""

    def checkType(self, type):
        return type in self.supportedTypes or issubclass(type, (str, int, bool, float, list, dict, tuple))

    def read(self, dataId, options={}):
        path = self.getPath(dataId)
        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            raise DataNotFound("Data was not found: %s" % (path))

    def write(self, dataId, object, options={}):
        # create data folder if not exist
        basePath = self.getOption("basePath")
        if not Path(basePath).exists():
            Path(basePath).mkdir(parents=True)

        with open(self.getPath(dataId), "wb+") as f:
            pickle.dump(object, f)
