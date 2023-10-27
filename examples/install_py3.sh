python3 -m venv .venv
source .venv/bin/activate
pip3 install build
python3 -m build --outdir dist ../ 
pip3 install dist/plexpy-0.0.1-py3-none-any.whl