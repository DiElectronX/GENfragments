import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *


generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            convertPythiaCodes = cms.untracked.bool(False),
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            list_forced_decays = cms.vstring('MyB0', 
                'Myanti-B0'),
            operates_on_particles = cms.vint32(),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            #user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Bd_Kstarmm_Kpi.dec')
	    user_decay_embedded= cms.vstring(
"""
#
# This is the decay file for the decay B0 -> mu+ mu- K*0(-> K+ pi-)
#
# EventType: 13144001
#
# Descriptor: [B0 -> mu+ mu- {,gamma} {,gamma} (K*0 -> K+ pi-)]cc
#
# NickName: 
#
# Physics: Includes radiative mode
#
# Tested: Never
# By: 
# Date: 
#
Alias      MyB0        B0
Alias      Myanti-B0   anti-B0
ChargeConj MyB0        Myanti-B0
Alias      MyK*0       K*0
Alias      MyK*0bar    anti-K*0
ChargeConj MyK*0       MyK*0bar
#
Decay MyB0
  1.000        MyK*0     mu+     mu-               BTOSLLBALL 6;
Enddecay
Decay Myanti-B0
  1.000        MyK*0bar     mu+     mu-            BTOSLLBALL 6;
Enddecay
#
Decay MyK*0
  1.000        K+        pi-                    VSS;
Enddecay
Decay MyK*0bar
  1.000        K-        pi+                    VSS;
Enddecay 
End
"""
	    ),
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'processParameters'),
        processParameters = cms.vstring('SoftQCD:nonDiffractive = on', 
            'PTFilter:filter = on', 
            'PTFilter:quarkToFilter = 5', 
            'PTFilter:scaleToFilter = 1.0'),
        pythia8CP5Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'PDF:pSet=20', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)

###### Filters ##########

bfilter = cms.EDFilter("PythiaFilter",
    MaxEta = cms.untracked.double(9999.0),
    MinEta = cms.untracked.double(-9999.0),
    ParticleID = cms.untracked.int32(511)
)

decayfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(-13, 13, 313),
    MaxEta = cms.untracked.vdouble(9999.0, 9999.0, 9999.0),
    MinEta = cms.untracked.vdouble(-9999.0, -9999.0, -9999.0),
    MinPt = cms.untracked.vdouble(-1.,-1.,-1.),
    NumberDaughters = cms.untracked.int32(3),
    ParticleID = cms.untracked.int32(511),
    verbose = cms.untracked.int32(1)
)

kstarfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(321, -211),
    MaxEta = cms.untracked.vdouble(9999.0, 9999.0),
    MinEta = cms.untracked.vdouble(-9999.0, -9999.0),
    MinPt = cms.untracked.vdouble(-1.,-1.),
    MotherID = cms.untracked.int32(511),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID = cms.untracked.int32(313),
    verbose = cms.untracked.int32(1)
)

mufilter = cms.EDFilter("MCMultiParticleFilter",
            src = cms.untracked.InputTag("generator", "unsmeared"),   
            Status = cms.vint32(1),
            ParticleID = cms.vint32(13),
            PtMin = cms.vdouble(6.0),
            NumRequired = cms.int32(1),
            EtaMax = cms.vdouble(2.5),
            MotherID = cms.untracked(511),
            AcceptMore = cms.bool(True)
            )


ProductionFilterSequence = cms.Sequence(generator*bfilter*decayfilter*kstarfilter*mufilter)
