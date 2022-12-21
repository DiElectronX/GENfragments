# Begin
cd $CMSSW_BASE/src/

# Download
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIIFall18GS-00214 --retry 3 --create-dirs -o Configuration/GenProduction/python/BPH-RunIIFall18GS-00214-fragment.py
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIIFall18GS-00212 --retry 3 --create-dirs -o Configuration/GenProduction/python/BPH-RunIIFall18GS-00212-fragment.py
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIIFall18GS-00162 --retry 3 --create-dirs -o Configuration/GenProduction/python/BPH-RunIIFall18GS-00162-fragment.py
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIIFall18GS-00179 --retry 3 --create-dirs -o Configuration/GenProduction/python/BPH-RunIIFall18GS-00179-fragment.py
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIIFall18GS-00184 --retry 3 --create-dirs -o Configuration/GenProduction/python/BPH-RunIIFall18GS-00184-fragment.py
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIIFall18GS-00208 --retry 3 --create-dirs -o Configuration/GenProduction/python/BPH-RunIIFall18GS-00208-fragment.py

# Copy to GENfragments repo
cp Configuration/GenProduction/python/BPH-RunIIFall18GS-00214-fragment.py  Configuration/GENfragments/python/BuToKee_SoftQCD_pythia8_evtgen.py
cp Configuration/GenProduction/python/BPH-RunIIFall18GS-00212-fragment.py  Configuration/GENfragments/python/BuToKJpsi_Toee_SoftQCD_pythia8_evtgen.py
cp Configuration/GenProduction/python/BPH-RunIIFall18GS-00162-fragment.py  Configuration/GENfragments/python/BuToKPsi2S_Toee_SoftQCD_pythia8_evtgen.py
cp Configuration/GenProduction/python/BPH-RunIIFall18GS-00179-fragment.py  Configuration/GENfragments/python/BdToKstarEE_SoftQCD_pythia8_evtgen.py
cp Configuration/GenProduction/python/BPH-RunIIFall18GS-00184-fragment.py  Configuration/GENfragments/python/BdToKstarJpsi_Toee_SoftQCD_pythia8_evtgen.py
cp Configuration/GenProduction/python/BPH-RunIIFall18GS-00208-fragment.py  Configuration/GENfragments/python/BdToKstarPsi2S_Toee_SoftQCD_pythia8_evtgen.py

# Remove old soft links
rm Configuration/Generator/python/BuToKee_SoftQCD_pythia8_evtgen.py
rm Configuration/Generator/python/BuToKJpsi_Toee_SoftQCD_pythia8_evtgen.py
rm Configuration/Generator/python/BuToKPsi2S_Toee_SoftQCD_pythia8_evtgen.py
rm Configuration/Generator/python/BdToKstarEE_SoftQCD_pythia8_evtgen.py
rm Configuration/Generator/python/BdToKstarJpsi_Toee_SoftQCD_pythia8_evtgen.py
rm Configuration/Generator/python/BdToKstarPsi2S_Toee_SoftQCD_pythia8_evtgen.py

# Create new soft links
cd Configuration/Generator/python/
ln -s ../../../Configuration/GENfragments/python/B*ToK*_SoftQCD_pythia8_evtgen.py .
cd -

# cmsDriver commands
cmsDriver.py Configuration/Generator/python/BuToKee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
cmsDriver.py Configuration/Generator/python/BuToKJpsi_Toee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
cmsDriver.py Configuration/Generator/python/BuToKPsi2S_Toee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
cmsDriver.py Configuration/Generator/python/BdToKstarEE_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
cmsDriver.py Configuration/Generator/python/BdToKstarJpsi_Toee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec
cmsDriver.py Configuration/Generator/python/BdToKstarPsi2S_Toee_SoftQCD_pythia8_evtgen.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --fileout file:step0.root --no_exec

# End
cd $CMSSW_BASE/src/
