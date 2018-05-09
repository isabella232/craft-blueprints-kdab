# -*- coding: utf-8 -*-

import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["5.9", "5.11", "dev"]:
          self.svnTargets[ver] = f"git://code.qt.io/pyside/pyside-setup.git|{ver}"
          self.targetConfigurePath[ver] = "sources/pyside2"
        self.defaultTarget = "dev"



    def setDependencies(self):
        self.buildDependencies["dev-utils/python2"] = None
        self.runtimeDependencies["kdab/shiboken2"] = None
        self.runtimeDependencies["libs/qt5"] = None
        self.runtimeDependencies["libs/llvm-meta/llvm"] = None


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        self.supportsNinja = False
        if ("Paths", "Python") in CraftCore.settings:
            python = os.path.join(CraftCore.settings.get("Paths", "Python"), f"python{CraftCore.compiler.executableSuffix}")
        if not os.path.exists(python):
            if CraftCore.compiler.isWindows:
                CraftCore.log.warning(f"Could not find {python} as provided by [Paths]Python, using {sys.executable} as a fallback")
            python = sys.executable
        self.subinfo.options.configure.args += f" -DPYTHON_EXECUTABLE=\"{python}\""
        self.subinfo.options.configure.args += f" -DLLVM_CONFIG=\"{os.path.join(CraftCore.standardDirs.craftRoot(), 'bin', 'llvm-config')}\""