#/bin/bash
if ! command -v conda &> /dev/null
then
    echo "conda not found. Please install conda."
else
    eval "$(conda shell.bash hook)"
    conda create --name=translator python=3.9 -y
    conda activate translator
    pip install -r requirements.txt
    mkdir build
    cp translator.py ./build/translator.py
    cp groq_1.py ./build/groq_1.py
    cd build
    python -m PyInstaller -F translator.py
    mv dist/translator ../translator
    cd ..
    rm -rf build
    conda deactivate
    conda env remove --name=translator -y
fi