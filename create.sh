# Begin
cd $CMSSW_BASE/src/

# cmsDriver commands
cmsDriver.py Configuration/Generator/python/BuToKee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
cmsDriver.py Configuration/Generator/python/BuToKJpsi_Toee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
cmsDriver.py Configuration/Generator/python/BuToKPsi2S_Toee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
cmsDriver.py Configuration/Generator/python/BdToKstarEE_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
cmsDriver.py Configuration/Generator/python/BdToKstarJpsi_Toee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
cmsDriver.py Configuration/Generator/python/BdToKstarPsi2S_Toee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
