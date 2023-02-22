# Testing of nf-core linting 

This markdown document contains summary of testing process and outcomes for nf-core tools/lint utility. All work was performed on Nimbus inside the autoTesting-nf repository, using VScode. 

Before running, need to [install nf-core tools](https://nf-co.re/tools/#installation):  

```
pip install nf-core
```

Tested installation with:
```
python3 -m nf_core
```
## Testing with IndexReferenceFasta-nf 

Performed testing and developed lint tests using the `IndexReferenceFasta-nf` workflow as it is small, contains test data. Before testing, cloned the repo with: 

```
git clone https://github.com/Sydney-Informatics-Hub/IndexReferenceFasta-nf.git
```

### Run the default nf-core lint tests 

nf-core lint tests assume nf-core lint scripts are housed in `/data/autoTesting-nf/nf-core_tools/tests/lint` in the nf-core tools repository. Scripts are written in python and contain various tests, including the following that may be relevant to SIH: 

* test_licenses 
* test_modules 
* files_exist 

To test nf-core lint tests on `IndexReferenceFasta-nf` without customisation will not work. For example, ran the following and got a bunch of python errors:  

```
cd /data/autoTesting-nf/IndexReferenceFasta-nf
python3 -m nf_core lint
```
