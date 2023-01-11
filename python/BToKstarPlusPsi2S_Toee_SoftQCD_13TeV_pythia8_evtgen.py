#Author: G Karathanasis, CU Boulder, Rk group

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    comEnergy = cms.double(13000.0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            list_forced_decays = cms.vstring('MyB+','MyB-'),        
            operates_on_particles = cms.vint32(),    
            convertPythiaCodes = cms.untracked.bool(False),
            user_decay_embedded= cms.vstring(
"""
#
# This is the decay file for the decay B+ -> J/Psi Kstar + -> MU+ MU- K+
#
Alias      MyB+        B+
Alias      MyB-        B-
ChargeConj MyB+        MyB-
Alias      MyPsi       psi(2)
ChargeConj MyPsi       MyPsi
Alias      MyK*+       K*+
Alias      MyK*-       K*-
ChargeConj MyK*+       MyK*-
Alias      MyK_S0      K_S0
ChargeConj MyK_S0      MyK_S0
#
Decay MyB+
1.000    MyPsi      MyK*+             SVV_HELAMP 0.159 1.563 0.775 0.0 0.612 2.712;
Enddecay
Decay MyB-
1.000    MyPsi      MyK*-             SVV_HELAMP 0.159 1.563 0.775 0.0 0.612 2.712;
Enddecay
#
Decay MyPsi
1.000         e+       e-            PHOTOS VLL;
Enddecay
#
Decay MyK*+
1.000        MyK_S0    pi+              VSS;
Enddecay
CDecay MyK*-
#
Decay MyK_S0
1.000        pi+       pi-              PHSP;
Enddecay
End
"""

            )
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring('SoftQCD:nonDiffractive = on',
					'PTFilter:filter = on', # this turn on the filter
                                        'PTFilter:quarkToFilter = 5', # PDG id of q quark
                                        'PTFilter:scaleToFilter = 1.0'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
    )
)

###### Filters ##########
decayfilter = cms.EDFilter(
    "PythiaDauVFilter",
    verbose         = cms.untracked.int32(1),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID      = cms.untracked.int32(521),  ## Bu
    DaughterIDs     = cms.untracked.vint32(100443, 323), ## psi and K*+
    MinPt           = cms.untracked.vdouble(-1., -1.),
    MinEta          = cms.untracked.vdouble(-9999., -9999.),
    MaxEta          = cms.untracked.vdouble( 9999.,  9999.)
    )

psifilter = cms.EDFilter(
    "PythiaDauVFilter",
    verbose         = cms.untracked.int32(1),
    NumberDaughters = cms.untracked.int32(2),
    MotherID        = cms.untracked.int32(521), ## Bu
    ParticleID      = cms.untracked.int32(100443),  ## Psi
    DaughterIDs     = cms.untracked.vint32(11, -11),  ## mu-, mu+
    MinPt           = cms.untracked.vdouble(3.0, 3.0),
    MinEta          = cms.untracked.vdouble(-1.5, -1.5),
    MaxEta          = cms.untracked.vdouble( 1.5, 1.5)
    )


kstarfilter = cms.EDFilter(
    "PythiaDauVFilter",
    verbose         = cms.untracked.int32(1),
    NumberDaughters = cms.untracked.int32(2),
    MotherID        = cms.untracked.int32(521), ## Bu
    ParticleID      = cms.untracked.int32(323), ## K*+
    DaughterIDs     = cms.untracked.vint32(310, 211),  ## Ks(310), pi+(211)                                                            
    MinPt           = cms.untracked.vdouble(0.5, 0.5),
    MinEta          = cms.untracked.vdouble(-2.5, -2.5),
    MaxEta          = cms.untracked.vdouble(2.5, 2.5)
    )


 


ProductionFilterSequence = cms.Sequence(generator*decayfilter*psifilter*kstarfilter)

