"""
This module loads the interface to the pwind c++ code
"""

import numpy as np
import os
import os.path as osp
import numpy.ctypeslib as npct
from ctypes import c_double, c_void_p, c_bool, c_ulong

# Type definition
array_1d_double = npct.ndpointer(dtype=np.double, ndim=1,
                                 flags="CONTIGUOUS")

# Load the library, compiling it if required
libdir = osp.dirname(osp.realpath(__file__))
try:
    libpwind = npct.load_library("libpwind", libdir)
except OSError:
    print "Failed to load libpwind... trying to compile it"
    os.system("cd "+libdir+"; make")
    libpwind = npct.load_library("libpwind", libdir)

# Allocation / de-allocation methods

# Geometries
libpwind.pwind_geom_sphere_new.restype = c_void_p
libpwind.pwind_geom_sphere_new.argtypes = [ ]
libpwind.pwind_geom_cone_new.restype = c_void_p
libpwind.pwind_geom_cone_new.argtypes = [ c_double, c_double ]
libpwind.pwind_geom_cone_sheath_new.restype = c_void_p
libpwind.pwind_geom_cone_sheath_new.argtypes \
    = [ c_double, c_double, c_double ]

# Ideal winds
libpwind.pwind_ideal_pa_new.restype = c_void_p
libpwind.pwind_ideal_pa_new.argtypes \
    = [ c_double, c_double, c_void_p, c_double, c_double, c_double ]
libpwind.pwind_ideal_pi_new.restype = c_void_p
libpwind.pwind_ideal_pi_new.argtypes \
    = [ c_double, c_double, c_void_p, c_double, c_double, c_double ]
libpwind.pwind_ideal_ps_new.restype = c_void_p
libpwind.pwind_ideal_ps_new.argtypes \
    = [ c_double, c_double, c_void_p, c_double, c_double, c_double ]
libpwind.pwind_ideal_ia_new.restype = c_void_p
libpwind.pwind_ideal_ia_new.argtypes \
    = [ c_double, c_double, c_void_p, c_double, c_double, c_double ]
libpwind.pwind_ideal_ii_new.restype = c_void_p
libpwind.pwind_ideal_ii_new.argtypes \
    = [ c_double, c_double, c_void_p, c_double, c_double, c_double ]
libpwind.pwind_ideal_is_new.restype = c_void_p
libpwind.pwind_ideal_is_new.argtypes \
    = [ c_double, c_double, c_void_p, c_double, c_double, c_double ]

# Radiation-driven winds
libpwind.pwind_rad_pa_new.restype = c_void_p
libpwind.pwind_rad_pa_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double ]
libpwind.pwind_rad_pi_new.restype = c_void_p
libpwind.pwind_rad_pi_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double ]
libpwind.pwind_rad_ps_new.restype = c_void_p
libpwind.pwind_rad_ps_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double ]
libpwind.pwind_rad_ia_new.restype = c_void_p
libpwind.pwind_rad_ia_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double ]
libpwind.pwind_rad_ii_new.restype = c_void_p
libpwind.pwind_rad_ii_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double ]
libpwind.pwind_rad_is_new.restype = c_void_p
libpwind.pwind_rad_is_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double ]

# Hot gas-driven winds
libpwind.pwind_hot_pa_new.restype = c_void_p
libpwind.pwind_hot_pa_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double, c_double, c_double ]
libpwind.pwind_hot_pi_new.restype = c_void_p
libpwind.pwind_hot_pi_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double, c_double, c_double ]
libpwind.pwind_hot_ps_new.restype = c_void_p
libpwind.pwind_hot_ps_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double, c_double, c_double ]
libpwind.pwind_hot_ia_new.restype = c_void_p
libpwind.pwind_hot_ia_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double, c_double, c_double ]
libpwind.pwind_hot_ii_new.restype = c_void_p
libpwind.pwind_hot_ii_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double, c_double, c_double ]
libpwind.pwind_hot_is_new.restype = c_void_p
libpwind.pwind_hot_is_new.argtypes \
    = [ c_double, c_double, c_double, c_void_p,
        c_double, c_double, c_double, c_double, c_double ]

# Free
libpwind.pwind_free.restype = None
libpwind.pwind_free.argtypes = [ c_void_p ]
libpwind.pwind_geom_free.restype = None
libpwind.pwind_geom_free.argtypes = [ c_void_p ]

# Information return methods
libpwind.Gamma.restype = c_double
libpwind.Gamma.argtypes = [ c_void_p ]
libpwind.mach.restype = c_double
libpwind.mach.argtypes = [ c_void_p ]
libpwind.epsrel.restype = c_double
libpwind.epsrel.argtypes = [ c_void_p ]
libpwind.epsabs.restype = c_double
libpwind.epsabs.argtypes = [ c_void_p ]
libpwind.fcrit.restype = c_double
libpwind.fcrit.argtypes = [ c_void_p ]
libpwind.xcrit.restype = c_double
libpwind.xcrit.argtypes = [ c_void_p ]
libpwind.sx.restype = c_double
libpwind.sx.argtypes = [ c_void_p ]
libpwind.zetaM.restype = c_double
libpwind.zetaM.argtypes = [ c_void_p ]
libpwind.zetaA.restype = c_double
libpwind.zetaA.argtypes = [ c_void_p ]
libpwind.umax.restype = c_double
libpwind.umax.argtypes = [ c_void_p ]

# Simple setting methods
libpwind.set_mach.restype = None
libpwind.set_mach.argtypes = [ c_double, c_void_p ]
libpwind.set_epsrel.restype = None
libpwind.set_epsrel.argtypes = [ c_double, c_void_p ]
libpwind.set_epsabs.restype = None
libpwind.set_epsabs.argtypes = [ c_double, c_void_p ]
libpwind.set_fcrit.restype = None
libpwind.set_fcrit.argtypes = [ c_double, c_void_p ]
libpwind.set_geometry.restype = None
libpwind.set_geometry.argtypes = [ c_void_p, c_void_p ]

# Kinematics methods
libpwind.y.restype = c_double
libpwind.y.argtypes = [ c_double, c_void_p ]
libpwind.m.restype = c_double
libpwind.m.argtypes = [ c_double, c_void_p ]
libpwind.dyda.restype = c_double
libpwind.dyda.argtypes = [ c_double, c_void_p ]
libpwind.X.restype = c_double
libpwind.X.argtypes = [ c_double, c_double, c_void_p ]
libpwind.U2.restype = c_double
libpwind.U2.argtypes = [ c_double, c_double, c_void_p ]
libpwind.dU2dx.restype = c_double
libpwind.dU2dx.argtypes = [ c_double, c_double, c_void_p ]
libpwind.dU2da.restype = c_double
libpwind.dU2da.argtypes = [ c_double, c_double, c_void_p ]

# Limit methods
libpwind.alimits.restype = c_ulong
libpwind.alimits.argtypes = [ c_double, c_double, c_double, c_void_p,
                              array_1d_double ]
libpwind.xlimits.restype = c_ulong
libpwind.xlimits.argtypes = [ c_double, c_void_p,
                              array_1d_double ]
libpwind.amax.restype = c_double
libpwind.amax.argtypes = [ c_double, c_void_p ]
libpwind.amax_abs.restype = c_double
libpwind.amax_abs.argtypes = [ c_void_p ]
libpwind.s_crit.restype = c_ulong
libpwind.s_crit.argtypes = [ c_double, c_double, c_double, c_void_p,
                             array_1d_double ]
libpwind.a_crit.restype = c_ulong
libpwind.a_crit.argtypes = [ c_double, c_double, c_double, c_void_p,
                             array_1d_double ]

# Computation methods
libpwind.pdot_approx.restype = c_double
libpwind.pdot_approx.argtypes = [ c_double, c_void_p ]
libpwind.pdot_exact.restype = c_double
libpwind.pdot_exact.argtypes = [ c_double, c_double, c_double, c_void_p ]
libpwind.Phi_uc.restype = c_double
libpwind.Phi_uc.argtypes = [ c_double, c_double, c_double, c_double,
                             c_double, c_void_p ]
libpwind.Phi_c.restype = c_double
libpwind.Phi_c.argtypes = [ c_double, c_double, c_double, c_double,
                            c_double, c_double, c_void_p ]
libpwind.tau_uc.restype = c_double
libpwind.tau_uc.argtypes = [ c_double, c_double, c_double, c_double,
                             c_double, c_double, c_double, c_double, c_void_p ]
libpwind.tau_uc_vec.restype = c_double
libpwind.tau_uc_vec.argtypes = [ c_double, array_1d_double, array_1d_double,
                                 c_double, c_double,
                                 c_ulong, c_double, c_double, c_double,
                                 c_double, c_void_p ]
libpwind.tau_c.restype = c_double
libpwind.tau_c.argtypes = [ c_double, c_double, c_double, c_double, c_double,
                            c_double, c_double, c_double, c_double, c_void_p ]
libpwind.tau_c_vec.restype = c_double
libpwind.tau_c_vec.argtypes = [ c_double, array_1d_double, array_1d_double,
                                c_double, c_double,
                                c_ulong, c_double, c_double, c_double,
                                c_double, c_double, c_void_p ]
libpwind.Xi.restype = c_double
libpwind.Xi.argtypes = [ c_double, c_double, c_double, c_void_p ]
libpwind.xi.restype = c_double
libpwind.xi.argtypes = [ c_double, c_double, c_void_p ]
libpwind.eta.restype = c_double
libpwind.eta.argtypes = [ c_double, c_double, c_double, c_double, c_bool,
                          c_double, c_double, c_double, c_bool, c_void_p ]
libpwind.Psi.restype = c_double
libpwind.Psi.argtypes = [ c_double, c_double, c_double, c_bool,
                          c_double, c_double, c_double, c_bool, c_void_p ]
