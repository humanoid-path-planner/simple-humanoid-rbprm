#!/usr/bin/env python
# Copyright (c) 2019 CNRS
# Author: Pierre Fernbach
#
# This file is part of hpp-rbprm-robot-data.
# hpp_tutorial is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# hpp_tutorial is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp_tutorial.  If not, see
# <http://www.gnu.org/licenses/>.

from hpp.corbaserver.rbprm.rbprmbuilder import Builder as Parent


class Robot(Parent):
    ##
    #  Information to retrieve urdf and srdf files.
    rootJointType = 'freeflyer'
    packageName = 'simple-humanoid-rbprm'
    meshPackageName = 'simple-humanoid-rbprm'
    urdfName = 'simple_humanoid_trunk'
    urdfNameRom = ['simple_humanoid_lleg_rom', 'simple_humanoid_rleg_rom']
    urdfSuffix = ""
    srdfSuffix = ""
    name = urdfName

    # reference position of the end effector position for each ROM
    # TODO
    ref_EE_lLeg = [0, 0.1, -1.]
    ref_EE_rLeg = [0, -0.1, -1.]

    def __init__(self, name=None, load=True, client=None, clientRbprm=None):
        if name is not None:
            self.name = name
        Parent.__init__(self, self.name, self.rootJointType, load, client, None, clientRbprm)
        self.setReferenceEndEffector('simple_humanoid_lleg_rom', self.ref_EE_lLeg)
        self.setReferenceEndEffector('simple_humanoid_rleg_rom', self.ref_EE_rLeg)
