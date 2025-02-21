# Copyright 2019-2024 French Alternative Energies and Atomic Energy Commission
#
# This file is part of t4_geom_convert.
#
# t4_geom_convert is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# t4_geom_convert is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# t4_geom_convert.  If not, see <https://www.gnu.org/licenses/>.
#
# vim: set fileencoding=utf-8 :

from math import pi, fabs
import numpy as np

from ..Progress import Progress
from ..Surface.ESurfaceTypeMCNP import ESurfaceTypeMCNP as MS
from ..Surface.CollectionDict import CollectionDict
from .ESurfaceTypeT4 import ESurfaceTypeT4 as T4S
from .SurfaceT4 import SurfaceT4
from .SurfaceCollection import SurfaceCollection
from .SurfaceConversionError import SurfaceConversionError
from ..VectUtils import rotation_from_vectors


def convert_mcnp_surfaces(dic_surface_mcnp):
    '''Method which convert MCNP surface and constructing the dictionary of
    Surface T4.'''
    dic_surface_t4 = CollectionDict()

    with Progress('converting surface',
                  len(dic_surface_mcnp), max(dic_surface_mcnp)) as progress:
        for i, (key, val) in enumerate(dic_surface_mcnp.items()):
            progress.update(i, key)
            t4_surfs = convert_mcnp_surface(key, val)
            dic_surface_t4[key] = t4_surfs

    return dic_surface_t4


def convert_mcnp_surface(key, val):
    '''Perform the actual conversion of an MCNP surface.'''
    surf_colls = []
    for surf, side in val:
        try:
            surf_coll = conversion_surface_params(key, surf)
        except SurfaceConversionError as err:
            msg = f'{err} (while converting surface {key})'
            raise SurfaceConversionError(msg) from None
        surf_colls.append((surf_coll, side))
    try:
        t4_surfs = SurfaceCollection.join(surf_colls)
    except SurfaceConversionError as err:
        msg = f'{err} (while converting surface {key})'
        raise SurfaceConversionError(msg) from None
    return t4_surfs


def conversion_surface_params(key, val):
    '''Convert the MCNP surface described by `val` into a TRIPOLI-4 surface.'''
    if val.type_surface in (MS.K_X, MS.K_Y, MS.K_Z, MS.KX, MS.KY, MS.KZ, MS.K):
        return convert_cone(int(key), val)

    transform = None

    if val.type_surface in (MS.P, MS.PX, MS.PY, MS.PZ):
        type_surface, param = convert_plane(val)
    elif val.type_surface in (MS.C_X, MS.C_Y, MS.C_Z, MS.CX, MS.CY, MS.CZ,
                              MS.C):
        type_surface, param = convert_cylinder(val)
    elif val.type_surface in (MS.SO, MS.S, MS.SX, MS.SY, MS.SZ):
        type_surface, param = convert_sphere(val)
    elif val.type_surface == MS.SQ:
        type_surface, param = convert_special_quadric(val)
    elif val.type_surface == MS.GQ:
        type_surface, param = convert_quadric(val)
    elif val.type_surface in (MS.TX, MS.TY, MS.TZ, MS.T):
        type_surface, param, transform = convert_torus(val)
    else:
        msg = f'Unrecognized surface type: {val.type_surface}'
        raise SurfaceConversionError(msg)

    surf = SurfaceT4(type_surface, param, transform=transform)
    return SurfaceCollection([(surf, 1)])


def convert_plane(val):
    '''Convert the parameters for planes.'''
    tuple_param = val.param_surface
    p_x, p_y, p_z = tuple_param[0]
    u_x, u_y, u_z = tuple_param[1]
    pos = -(u_x * p_x + u_y * p_y + u_z * p_z)
    if u_x == 0. and u_y == 0. and u_z > 0.:
        type_surface = T4S.PLANEZ
        param = [-pos / u_z]
    elif u_y == 0. and u_z == 0. and u_x > 0.:
        type_surface = T4S.PLANEX
        param = [-pos / u_x]
    elif u_z == 0. and u_x == 0. and u_y > 0.:
        type_surface = T4S.PLANEY
        param = [-pos / u_y]
    else:
        type_surface = T4S.PLANE
        param = [u_x, u_y, u_z, pos]
    return type_surface, param


def convert_cylinder(val):
    '''Convert the parameters for cylinders.'''
    tuple_param = val.param_surface
    p_x, p_y, p_z = tuple_param[0]
    u_x, u_y, u_z = tuple_param[1]
    radius = val.compl_param[0]
    if u_x == 0 and u_y == 0:
        type_surface = T4S.CYLZ
        param = [p_x, p_y, radius]
    elif u_y == 0 and u_z == 0:
        type_surface = T4S.CYLX
        param = [p_y, p_z, radius]
    elif u_z == 0 and u_x == 0:
        type_surface = T4S.CYLY
        param = [p_x, p_z, radius]
    else:
        param = [p_x, p_y, p_z, radius, u_x, u_y, u_z]
        type_surface = T4S.CYL
    return type_surface, param


def convert_sphere(val):
    '''Convert the parameters for spheres.'''
    tuple_param = val.param_surface
    p_x, p_y, p_z = tuple_param[0]
    radius = val.compl_param[0]
    type_surface = T4S.SPHERE
    param = [p_x, p_y, p_z, radius]
    return type_surface, param


def convert_special_quadric(val):
    '''Convert the parameters for a quadric in SQ form.'''
    sq_params = val.compl_param
    asq = sq_params[0]
    bsq = sq_params[1]
    csq = sq_params[2]
    dsq = sq_params[3]
    esq = sq_params[4]
    fsq = sq_params[5]
    gsq = sq_params[6]
    xsq = sq_params[7]
    ysq = sq_params[8]
    zsq = sq_params[9]
    gq_params = [asq, bsq, csq, 0.0, 0.0, 0.0,
                 2.0 * dsq - 2.0 * asq * xsq,
                 2.0 * esq - 2.0 * bsq * ysq,
                 2.0 * fsq - 2.0 * csq * zsq,
                 asq * xsq**2 + bsq * ysq**2 + csq * zsq**2
                 - 2.0 * (dsq * xsq + esq * ysq + fsq * zsq) + gsq]
    if eval_quadric(gq_params, (xsq, ysq, zsq)) > 0.0:
        gq_params = [-param for param in gq_params]
    return T4S.QUAD, gq_params


def eval_quadric(params, point):
    '''Evaluate the quadric represented by `params` at `point`.

    >>> quad = [1.0, 1.0, 1.0,  # this is a sphere of radius 1.0
    ...         0.0, 0.0, 0.0,
    ...         0.0, 0.0, 0.0, -1.0]
    >>> eval_quadric(quad, (0.0, 0.0, 0.0)) < 0.0
    True
    >>> eval_quadric(quad, (0.999, 0.0, 0.0)) < 0.0
    True
    >>> eval_quadric(quad, (1.001, 0.0, 0.0)) > 0.0
    True
    >>> eval_quadric(quad, (2.000, 0.0, 0.0)) > 0.0
    True
    '''
    x, y, z = point  # pylint: disable=invalid-name
    return (params[0] * x**2 + params[1] * y**2 + params[2] * z**2
            + params[3] * x * y + params[4] * y * z + params[5] * z * x
            + params[6] * x + params[7] * y + params[8] * z + params[9])


def convert_quadric(val):
    '''Convert the parameters for a quadric.'''
    return T4S.QUAD, val.compl_param


def convert_torus(val):
    '''Convert the parameters for tori.'''
    center, axis = val.param_surface
    abs_axis = np.abs(axis)
    param = list(center) + list(val.compl_param)
    transform = None
    if np.allclose(abs_axis, [1.0, 0.0, 0.0]):
        type_surface = T4S.TORUSX
    elif np.allclose(abs_axis, [0.0, 1.0, 0.0]):
        type_surface = T4S.TORUSY
    elif np.allclose(abs_axis, [0.0, 0.0, 1.0]):
        type_surface = T4S.TORUSZ
    else:
        # type_surface = T4S.TORUSZ
        # transform_tr = np.array(center)
        # transform_mat = rotation_from_vectors((0.0, 0.0, 1.0), axis)
        # transform = (transform_tr, transform_mat)
        type_surface = T4S.TORUSZ
        transform_mat = rotation_from_vectors((0.0, 0.0, 1.0), axis)
        center = transform_mat.T.dot(center)
        param[:3] = list(center.flat)
        transform = (np.zeros(3), transform_mat)
    return type_surface, param, transform


def convert_cone(key, val):
    '''Convert the parameters for cones.'''
    p_x, p_y, p_z = val.param_surface[0]
    u_x, u_y, u_z = val.param_surface[1]
    theta = 180. * val.compl_param[1] / pi
    if u_x == 0. and u_y == 0.:
        type_surface = T4S.CONEZ
        param = [p_x, p_y, p_z, theta]
    elif u_y == 0. and u_z == 0.:
        type_surface = T4S.CONEX
        param = [p_x, p_y, p_z, theta]
    elif u_z == 0. and u_x == 0.:
        type_surface = T4S.CONEY
        param = [p_x, p_y, p_z, theta]
    else:
        type_surface = T4S.CONE
        param = [p_x, p_y, p_z, theta, u_x, u_y, u_z]
    cone = SurfaceT4(type_surface, param)

    nappe = val.compl_param[2] if len(val.compl_param) == 3 else None
    if nappe is None or nappe == 0:
        return SurfaceCollection([(cone, 1)])

    pos = -(u_x * p_x + u_y * p_y + u_z * p_z)
    if u_x == 0 and u_y == 0:
        type_surface = T4S.PLANEZ
        param = [-pos / u_z]
    elif u_y == 0 and u_z == 0:
        type_surface = T4S.PLANEX
        param = [-pos / u_x]
    elif u_z == 0 and u_x == 0:
        type_surface = T4S.PLANEY
        param = [-pos / u_y]
    else:
        type_surface = T4S.PLANE
        param = [u_x, u_y, u_z, pos]
    plane = SurfaceT4(type_surface, param,
                      [f'aux plane for cone {key}'])
    return SurfaceCollection([(cone, 1), (plane, -int(nappe))])
