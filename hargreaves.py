# The Spatial Processes in HYdrology (SPHY) model:
# A spatially distributed hydrological model that calculates soil-water and
# cryosphere processes on a cell-by-cell basis.
#
# Copyright (C) 2013  Wilco Terink
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Email: w.terink@futurewater.nl OR terinkw@gmail.com

#-Authorship information-###################################################################
__author__ = "Wilco Terink"
__copyright__ = "Wilco Terink"
__license__ = "GPL"
__version__ = "2.1"
__email__ = "w.terink@futurewater.nl, terinkw@gmail.com"
__date__ ='1 January 2017'
############################################################################################

#-Extraterrestrial radiation    
def extrarad(self, pcr):
    DayNo = self.timecalc.julian(self)[0]
    LatRad = self.Lat * (self.pi / 180)
    dr = 1 + 0.033 * pcr.cos((2 * self.pi * DayNo) /  365)
    delta = 0.409 * pcr.sin(((2 * self.pi * DayNo) / 365) - 1.39)
    omegas = pcr.acos(-1 * pcr.tan(LatRad) * pcr.tan(delta))
    Ra = ((24 * 60) / self.pi) * self.Gsc * dr * (pcr.scalar(omegas) * pcr.sin(LatRad) * pcr.sin(delta) +\
        pcr.cos(LatRad) * pcr.cos(delta) * pcr.sin(omegas))
    return Ra    

#-Modified Hargreaves for calculation of ETref
def Hargreaves(pcr, ra, temp, tempmax, tempmin):
    ETref = pcr.max(0.0023 * 0.408 * ra * (temp + 17.8) * (pcr.max(tempmax - tempmin, 0))**0.5, 0)
    return ETref