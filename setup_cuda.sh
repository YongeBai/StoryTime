#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
cd ai-voice-cloning
./setup-cuda.sh
cd ..
cd RVC
pip install -r ./requirements.txt
cd ..
pip install -r ./requirements.txt

# put inference code stuff here
./run.sh $1

deactivate



