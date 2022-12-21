# GENfragments


```
# Init
cmsrel CMSSW_12_4_11
cd CMSSW_12_4_11/src
cmsenv
git cms-init

# Location of GEN fragments used by cmsDriver
git cms-addpkg Configuration/Generator

# Decay tables
git cms-addpkg GeneratorInterface/EvtGenInterface
rm -r GeneratorInterface/EvtGenInterface/data
git clone git@github.com:cms-data/GeneratorInterface-EvtGenInterface.git GeneratorInterface/EvtGenInterface/data

# This repository
git clone git@github.com:DiElectronX/GENfragments.git Configuration/GENfragments
```

The following script is used to download the GEN fragments used in 2018 (to be used once) 
```
. setup.sh
```
