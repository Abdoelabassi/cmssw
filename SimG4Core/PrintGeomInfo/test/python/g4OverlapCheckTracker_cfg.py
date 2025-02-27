import FWCore.ParameterSet.Config as cms

process = cms.Process("G4PrintGeometry")

#process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2017Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2021Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D17Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D45Reco_cff')

from SimG4Core.PrintGeomInfo.g4TestGeometry_cfi import *
process = checkOverlap(process)

# enable Geant4 overlap check 
process.g4SimHits.CheckGeometry = True

# Geant4 geometry check 
process.g4SimHits.G4CheckOverlap.OutputBaseName = cms.string("Tracker2021")
process.g4SimHits.G4CheckOverlap.OverlapFlag = cms.bool(True)
process.g4SimHits.G4CheckOverlap.Tolerance  = cms.double(0.0)
process.g4SimHits.G4CheckOverlap.Resolution = cms.int32(10000)
process.g4SimHits.G4CheckOverlap.Depth      = cms.int32(-1)
# tells if NodeName is G4Region or G4PhysicalVolume
process.g4SimHits.G4CheckOverlap.RegionFlag = cms.bool(True)
# list of names
process.g4SimHits.G4CheckOverlap.NodeNames  = cms.vstring('TrackerDeadRegion','TrackerSensRegion')
# enable dump gdml file 
process.g4SimHits.G4CheckOverlap.gdmlFlag   = cms.bool(False)
# if defined a G4PhysicsVolume info is printed
process.g4SimHits.G4CheckOverlap.PVname     = 'Tracker'
# if defined a list of daughter volumes is printed
process.g4SimHits.G4CheckOverlap.LVname     = 'Tracker'

# extra output files, created if a name is not empty
process.g4SimHits.FileNameField   = ''
process.g4SimHits.FileNameGDML    = ''
process.g4SimHits.FileNameRegions = ''
#
