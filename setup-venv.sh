#!/bin/bash

set -o errexit

if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <path-to-unziped-facial-classification-dir>"
	exit 1
fi

cd $(dirname "$0")

# Create virtualenv and set up environment
python3 -m venv venv
source venv/bin/activate

# Install xnornet
pushd "$1"
python3 -m pip uninstall xnornet || true
python3 -m pip install xnornet*.whl
popd

# Install other modules
python3 -m pip install -r requirements.txt

# Done!
cat <<EOF


Done! Start your environment via:

  source venv/bin/activate

And run:

  ./src/hello.py
EOF
