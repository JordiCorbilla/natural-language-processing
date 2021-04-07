# natural-language-processing

Python Samples for NLP using `sklearn`

# NLP

NLP is the technology behind machine translation. It's alsu useful for Text-to-speech (translating voice commands into text), caption generation (visualizing an image and generating a brief description) and question-answering type of projects (questioning a computer and receiving an intelligent answer).

Language is something that is fairly new in terms of evolution and it only relates to humans. Trying to build a computer that could understand language as we do would mean building an intelligent computer and we are still quite far away from it. 

# Preparing the conda environment using Python 3.8

```bash
(base) C:\Users\thund>conda create --name nlp python=3.8
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.8.3
  latest version: 4.9.2

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: C:\Users\thund\Anaconda3\envs\nlp

  added / updated specs:
    - python=3.8


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2021.1.19  |       haa95532_1         119 KB
    certifi-2020.12.5          |   py38haa95532_0         141 KB
    openssl-1.1.1k             |       h2bbff1b_0         4.8 MB
    pip-21.0.1                 |   py38haa95532_0         1.8 MB
    python-3.8.8               |       hdbf39b2_4        15.9 MB
    setuptools-52.0.0          |   py38haa95532_0         726 KB
    sqlite-3.35.4              |       h2bbff1b_0         761 KB
    vc-14.2                    |       h21ff451_1           8 KB
    vs2015_runtime-14.27.29016 |       h5e58377_2        1007 KB
    wheel-0.36.2               |     pyhd3eb1b0_0          33 KB
    ------------------------------------------------------------
                                           Total:        25.3 MB

The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2021.1.19-haa95532_1
  certifi            pkgs/main/win-64::certifi-2020.12.5-py38haa95532_0
  openssl            pkgs/main/win-64::openssl-1.1.1k-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.0.1-py38haa95532_0
  python             pkgs/main/win-64::python-3.8.8-hdbf39b2_4
  setuptools         pkgs/main/win-64::setuptools-52.0.0-py38haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.35.4-h2bbff1b_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.36.2-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py38_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
ca-certificates-2021 | 119 KB    | ############################################################################ | 100%
certifi-2020.12.5    | 141 KB    | ############################################################################ | 100%
setuptools-52.0.0    | 726 KB    | ############################################################################ | 100%
sqlite-3.35.4        | 761 KB    | ############################################################################ | 100%
openssl-1.1.1k       | 4.8 MB    | ############################################################################ | 100%
python-3.8.8         | 15.9 MB   | ############################################################################ | 100%
wheel-0.36.2         | 33 KB     | ############################################################################ | 100%
vs2015_runtime-14.27 | 1007 KB   | ############################################################################ | 100%
pip-21.0.1           | 1.8 MB    | ############################################################################ | 100%
vc-14.2              | 8 KB      | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate nlp
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\thund>conda activate nlp

(nlp) C:\Users\thund>pip install future
Collecting future
  Downloading future-0.18.2.tar.gz (829 kB)
     |████████████████████████████████| 829 kB 819 kB/s
Building wheels for collected packages: future
  Building wheel for future (setup.py) ... done
  Created wheel for future: filename=future-0.18.2-py3-none-any.whl size=491059 sha256=ec75b21043eeb7e04cc92b93a5ca9acfb416c0f6fa5237d5056bf9459f1083db
  Stored in directory: c:\users\thund\appdata\local\pip\cache\wheels\8e\70\28\3d6ccd6e315f65f245da085482a2e1c7d14b90b30f239e2cf4
Successfully built future
Installing collected packages: future
Successfully installed future-0.18.2

(nlp) C:\Users\thund>pip install numpy
Collecting numpy
  Downloading numpy-1.20.2-cp38-cp38-win_amd64.whl (13.7 MB)
     |████████████████████████████████| 13.7 MB 344 kB/s
Installing collected packages: numpy
Successfully installed numpy-1.20.2

(nlp) C:\Users\thund>pip install sklearn
Collecting sklearn
  Downloading sklearn-0.0.tar.gz (1.1 kB)
Collecting scikit-learn
  Downloading scikit_learn-0.24.1-cp38-cp38-win_amd64.whl (6.9 MB)
     |████████████████████████████████| 6.9 MB 467 kB/s
Collecting joblib>=0.11
  Downloading joblib-1.0.1-py3-none-any.whl (303 kB)
     |████████████████████████████████| 303 kB 656 kB/s
Collecting scipy>=0.19.1
  Downloading scipy-1.6.2-cp38-cp38-win_amd64.whl (32.7 MB)
     |████████████████████████████████| 32.7 MB 328 kB/s
Collecting threadpoolctl>=2.0.0
  Downloading threadpoolctl-2.1.0-py3-none-any.whl (12 kB)
Requirement already satisfied: numpy>=1.13.3 in c:\users\thund\anaconda3\envs\nlp\lib\site-packages (from scikit-learn->sklearn) (1.20.2)
Building wheels for collected packages: sklearn
  Building wheel for sklearn (setup.py) ... done
  Created wheel for sklearn: filename=sklearn-0.0-py2.py3-none-any.whl size=1316 sha256=007e7a885aa8a530a13ff8775ea6556efe729bf8a76429821ac7ccd77097e639
  Stored in directory: c:\users\thund\appdata\local\pip\cache\wheels\22\0b\40\fd3f795caaa1fb4c6cb738bc1f56100be1e57da95849bfc897
Successfully built sklearn
Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn, sklearn
Successfully installed joblib-1.0.1 scikit-learn-0.24.1 scipy-1.6.2 sklearn-0.0 threadpoolctl-2.1.0
```
