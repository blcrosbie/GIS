# -*- coding: utf-8 -*-
"""
/***************************************************************************
 geemap
                                 A QGIS plugin
 This plugin provides a GUI interface for Google Earth Engine and Python using the geemap module
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-07-21
        copyright            : (C) 2020 by Brandon Crosbie
        email                : jamwamb7@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load geemap class from file geemap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geemap import geemap
    return geemap(iface)
