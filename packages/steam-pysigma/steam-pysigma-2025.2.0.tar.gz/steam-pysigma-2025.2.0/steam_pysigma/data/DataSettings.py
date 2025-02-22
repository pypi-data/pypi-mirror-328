# STEAM PySigma is a python wrapper of STEAM-SIGMA written in Java.
# Copyright (C) 2023, CERN, Switzerland. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from pydantic import BaseModel

class DataSettings(BaseModel):
    """
        Dataclass of settings for STEAM analyses
        This will be populated either form a local settings file (if flag_permanent_settings=False)
        or from the keys in the input analysis file (if flag_permanent_settings=True)
    """
    comsolexe_path:        str = None  # full path to comsol.exe, only COMSOL53a is supported
    JAVA_jdk_path:         str = None  # full path to folder with java jdk
    CFunLibPath:           str = None  # full path to dll files with material properties