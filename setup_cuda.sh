python -m venv .venv
source .venv/bin/activate
cd ai-voice-cloning
./setup-cuda.sh
cd ..
cd RVC
pip install -r ./requirements.txt
cd ..

# put inference code stuff here

deactivate



