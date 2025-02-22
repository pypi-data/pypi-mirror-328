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

import os
import unittest
from pathlib import Path

from steam_pysigma.data import DataPySIGMA as dS
from steam_pysigma.plotters.PlotterRoxie import plot_all
from steam_pysigma.utils.Utils import get_user_settings, make_folder_if_not_existing, read_data_from_yaml


class TestBuildComsolModel(unittest.TestCase):

    def setUp(self):
        self.test_folder = Path(__file__).parent
        self.settings = get_user_settings(self.test_folder)

    def test_plot_all(self):
        magnet_names = ["MQXB", "MED_C_COMB", "MB_2COILS"] # Tests one normal multipole, one assymetric coil and one with elliptic arcs
        for magnet_name in magnet_names:
            output_sigma_path = os.path.join(Path(os.path.dirname(__file__)), "output", 'plotters')
            make_folder_if_not_existing(output_sigma_path)
            self.yaml_file = os.path.join(Path(os.path.dirname(__file__)).parent, 'tests', 'input', magnet_name, magnet_name + "_SIGMA.yaml")
            base_file_name = os.path.splitext(self.yaml_file)[0]
            self.roxie_data = read_data_from_yaml(f'{base_file_name}.geom', dS.SIGMAGeometry)
            plot_all(self.roxie_data.Roxie_Data)
