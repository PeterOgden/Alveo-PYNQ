#  Copyright (C) 2020 Xilinx, Inc
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import setup, find_packages
import os
from pynq.utils import build_py


__author__ = "Giuseppe Natale"
__copyright__ = "Copyright 2020, Xilinx"
__email__ = "pynq_support@xilinx.com"


# global variables
module_name = "pynq_alveo_examples"
_data_files = []


def _extend_package(path):
    if os.path.isdir(path):
        _data_files.extend(
            [os.path.join("..", root, f)
             for root, _, files in os.walk(path) for f in files]
        )
    elif os.path.isfile(path):
        _data_files.append(os.path.join("..", path))


_extend_package(os.path.join(module_name, "notebooks"))

setup(name=module_name,
      version="1.0.alpha5",
      description="Alveo-PYNQ",
      author="Giuseppe Natale",
      author_email="pynq_support@xilinx.com",
      url="https://github.com/giunatale/Alveo-PYNQ",
      packages=find_packages(),
      download_url="https://test.pypi.org/project/pynq-alveo-examples/",
      package_data={
          "": _data_files,
      },
      python_requires='>=3.5.2',
      # keeping 'setup_requires' only for readability - relying on
      # pyproject.toml and PEP 517/518
      setup_requires=[
          "pynq>=2.5.1a1"
      ],
      install_requires=[
          "pynq>=2.5.1a1",
          "jupyter",
          "jupyterlab",
          "plotly"
      ],
      extras_require={
          ':python_version<"3.6"': [
              'matplotlib<3.1'
          ],
          ':python_version>="3.6"': [
              'matplotlib'
          ]
      },
      entry_points={
          "pynq.notebooks": [
              "0-welcome-to-pynq = pynq_alveo_examples.notebooks."
              "0_welcome_to_pynq",
              "1-introduction = pynq_alveo_examples.notebooks.1_introduction",
              "2-kernel-optimization = pynq_alveo_examples.notebooks."
              "2_kernel_optimization",
              "3-advanced-features = pynq_alveo_examples.notebooks."
              "3_advanced_features",
              "4-building-and-emulation = pynq_alveo_examples.notebooks."
              "4_building_and_emulation"
          ]
      },
      cmdclass={"build_py": build_py},
      license="Apache License 2.0"
      )
