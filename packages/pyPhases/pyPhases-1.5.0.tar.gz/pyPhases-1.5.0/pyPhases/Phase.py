from typing import Type, TypeVar

from pyPhases import Project
from pyPhases.Data import Data
from pyPhases.util.Optionizable import Optionizable
from pyPhases.util.pdict import pdict

T = TypeVar('T')

class Phase(Optionizable):
    name = ""
    config = pdict({})
    metrics = {}
    summary = {}
    inputs = []
    model = None
    runMethod = "main"
    project: Project = None
    decorators = None

    def __init__(self, exportData=None, options=None) -> None:
        if options is None:
            options = {}
        super().__init__(options)
        self.exportData = exportData or []
        self.exportDataStrings = None
        self._prepared = False

    def prepare(self):
        if self._prepared:
            return
        self.logDebug(f"Prepare phase: {self.name}")
        self.exportData = list(map(lambda s: Data.create(s, self.project), self.exportData))
        self.exportDataStrings = list(map(lambda data: data.name, self.exportData))
        self.prepareConfig()
        self._prepared = True

        phaseName = self.getId()
        if phaseName in self.project.config:
            for index in self.project.config[phaseName]:
                value = self.project.config[phaseName][index]
                self.logDebug(f"Overwrite Config {index} for phase {phaseName} with {value}")
                setattr(self, index, value)

        def configChanged(changed):
            if changed is None:
                self.prepareConfig()
                self.project.addConfig(self.config)

        self.project.on("configChanged", configChanged)

    def prepareConfig(self):
        pass

    def getDecorators(self):
        if self.decorators is not None:
            return self.decorators

        self.decorators = []
        for decorator in self.project.decorators:
            if decorator.filter(self):
                self.decorators.append(decorator)

        return self.decorators

    def getConfig(self, configName, defaultValue=None):
        return self.project.getConfig(configName, defaultValue)

    def setConfig(self, configName, value):
        return self.project.setConfig(configName, value)

    def getData(self, dataName: str, expectedReturnType: Type[T] =None, version: str = "current", options=None, generate=True, **kwargs) -> T:
        if options is None:
            options = {}
        return self.project.getData(
            dataName=dataName,
            expectedReturnType=expectedReturnType,
            version=version,
            options=options,
            generate=generate,
            **kwargs
        )

    def registerData(self, dataName: str, data, version: str = "current", save: bool = True):
        return self.project.registerData(dataName=dataName, data=data, version=version, save=save)

    def generateData(self, name):
        self.run()

    def getId(self):
        return self.name or type(self).__name__

    def run(self):
        phaseName = self.getId()
        self.log(f"RUN phase {phaseName}: {self.name}")

        def methodNotFound():
            self.logError(f"The current phase needs the following method defined: {self.runMethod}")

        method = getattr(self, self.runMethod, methodNotFound)
        decorators = self.getDecorators()

        for decorator in decorators:
            decorator.before(self)

        method()

        for decorator in decorators:
            decorator.after(self)
