import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0)
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    comEnergy = cms.double(13600.0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            list_forced_decays = cms.vstring('MyB0', 'Myanti-B0'),
            operates_on_particles = cms.vint32(),
            convertPythiaCodes = cms.untracked.bool(False),
	    user_decay_embedded= cms.vstring(
"""
Alias      MyB0        B0
Alias      Myanti-B0   anti-B0
ChargeConj MyB0        Myanti-B0
Alias      MyK*0       K*0
Alias      MyK*0bar    anti-K*0
ChargeConj MyK*0       MyK*0bar
#
Decay MyB0
  1.000        MyK*0     e+     e-               BTOSLLBALL 6;
Enddecay
Decay Myanti-B0
  1.000        MyK*0bar     e+     e-            BTOSLLBALL 6;
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
        #pythia8CommonSettingsBlock,
        #pythia8CP5SettingsBlock,
        #pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'SoftQCD:nonDiffractive = on',
            'PTFilter:filter = on', 
            'PTFilter:quarkToFilter = 5', 
            'PTFilter:scaleToFilter = 1.0'),
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings',
            #'pythia8PSweightsSettings',
            'processParameters'),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14', 
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
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
)

###### Filters ##########

bfilter = cms.EDFilter("PythiaFilter",
    MaxEta = cms.untracked.double(9999.0),
    MinEta = cms.untracked.double(-9999.0),
    ParticleID = cms.untracked.int32(511)
)

decayfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(-11, 11, 313),
    MaxEta = cms.untracked.vdouble(1.5, 1.5, 2.5),
    MinEta = cms.untracked.vdouble(-1.5, -1.5, -2.5),
    MinPt = cms.untracked.vdouble(3.0,3.0,0.5),
    NumberDaughters = cms.untracked.int32(3),
    ParticleID = cms.untracked.int32(511),
    verbose = cms.untracked.int32(1)
)

kstarfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(321, -211),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MinPt = cms.untracked.vdouble(0.5,0.5),
    MotherID = cms.untracked.int32(511),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID = cms.untracked.int32(313),
    verbose = cms.untracked.int32(1)
)

ProductionFilterSequence = cms.Sequence(generator*bfilter*decayfilter*kstarfilter)
