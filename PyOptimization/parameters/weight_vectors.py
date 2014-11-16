"""
Copyright (C) 2014, 申瑞珉 (Ruimin Shen)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import numpy
import pyotl.utility
import pyoptimization.utility

def flat(config, count, dimension):
	path = os.path.join(pyoptimization.utility.get_pyoptimization_path(config), 'Data', 'PF_%u' % count)
	return numpy.loadtxt(os.path.join(path, 'DTLZ1', str(dimension) + '.csv'), ndmin = 2) * 2

def sphere(config, count, dimension):
	path = os.path.join(pyoptimization.utility.get_pyoptimization_path(config), 'Data', 'PF_%u' % count)
	return numpy.loadtxt(os.path.join(path, 'DTLZ2', str(dimension) + '.csv'), ndmin = 2)

def nbi_moea_d(config, count, dimension):
	division = {
		100:	{
			2:	[12],
			3:	[23] * (dimension - 1),
			4:	[9] * (dimension - 1),
			5:	[5] * (dimension - 1),
			6:	[5] * (dimension - 1),
			10:	[3] * (dimension - 1),
			15:	[2] * (dimension - 1),
		},
	}[count][dimension]
	return pyotl.utility.NormalBoundaryIntersection_Real(pyotl.utility.PyList2Vector_size_t(division))

def nbi_nsga_iii(config, count, dimension):
	division = {
		100:	{
			2:	[100],
			3:	[12] * (dimension - 1),
			5:	[6] * (dimension - 1),
			8:	[3] * (dimension - 1),
		},
	}[count][dimension]
	return pyotl.utility.NormalBoundaryIntersection_Real(pyotl.utility.PyList2Vector_size_t(division))