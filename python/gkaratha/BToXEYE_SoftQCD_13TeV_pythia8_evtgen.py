# Pythia 8 & evt gen fragment for the final state B -> eeXY. MuFilter also appied 
# Author: G. Karathanasis 
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
            operates_on_particles = cms.vint32(),    
            convertPythiaCodes = cms.untracked.bool(False),
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
           'SoftQCD:nonDiffractive = on',
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


mufilter = cms.EDFilter("MCMultiParticleFilter",
            src = cms.untracked.InputTag("generator", "unsmeared"),   
            Status = cms.vint32(1),
            ParticleID = cms.vint32(13),
            PtMin = cms.vdouble(6.0),
            NumRequired = cms.int32(1),
            EtaMax = cms.vdouble(2.5),
            AcceptMore = cms.bool(True)
            )

    
efilter = cms.EDFilter("MCMultiParticleFilter",
            src = cms.untracked.InputTag("generator", "unsmeared"),   
            Status = cms.vint32(1),
            ParticleID = cms.vint32(11),
            PtMin = cms.vdouble(0.0),
            NumRequired = cms.int32(2),
            EtaMax = cms.vdouble(999),
            AcceptMore = cms.bool(True)
            )


ProductionFilterSequence = cms.Sequence(generator*efilter*mufilter)
