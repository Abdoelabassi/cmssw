import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_DDD_cff import Run3_DDD
process = cms.Process("PROD",Run3_DDD)
process.load("Configuration.Geometry.GeometryExtended2021Reco_cff")

#from Configuration.Eras.Era_Run3_dd4hep_cff import Run3_dd4hep
#process = cms.Process("PROD",Run3_dd4hep)
#process.load("Configuration.Geometry.GeometryDD4hepExtended2021Reco_cff")

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("IOMC.EventVertexGenerators.VtxSmearedGauss_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.StandardSequences.Generator_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff"
)
from Configuration.AlCa.GlobalTag import GlobalTag 
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.G4cerr=dict()

process.load("IOMC.RandomEngine.IOMC_cff")
process.RandomNumberGeneratorService.generator.initialSeed = 456789
process.RandomNumberGeneratorService.g4SimHits.initialSeed = 9876
process.RandomNumberGeneratorService.VtxSmeared.initialSeed = 123456789

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000)
)

process.source = cms.Source("EmptySource")

process.generator = cms.EDProducer("FlatRandomEGunProducer",
    PGunParameters = cms.PSet(
        PartID = cms.vint32(211),
        MinEta = cms.double(0.1305),
        MaxEta = cms.double(0.1305),
        MinPhi = cms.double(-3.14159265359),
        MaxPhi = cms.double(3.14159265359),
        MinE   = cms.double(30.0),
        MaxE   = cms.double(30.0)
    ),
    Verbosity       = cms.untracked.int32(0),
    AddAntiParticle = cms.bool(False),
    firstRun        = cms.untracked.uint32(1)
)

process.output = cms.OutputModule("PoolOutputModule",
    process.FEVTSIMEventContent,
    fileName = cms.untracked.string('simevent030eta2.root')
)

process.Timing = cms.Service("Timing")

process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.out_step = cms.EndPath(process.output)

process.g4SimHits.Physics.type = 'SimG4Core/Physics/QGSP_FTFP_BERT_EML'
#process.g4SimHits.G4Commands = ['/tracking/verbose 1']
# Schedule definition                                                          
process.schedule = cms.Schedule(process.generation_step,
                                process.simulation_step,
                                process.out_step
                                )

# filter all path with the production filter sequence                          
for path in process.paths:
        getattr(process,path)._seq = process.generator * getattr(process,path)._seq

