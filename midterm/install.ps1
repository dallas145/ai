if (Get-Command conda -ErrorAction SilentlyContinue) {
    conda create --name=translator python=3.9 -y
    conda activate translator
    pip install -r requirements.txt
    New-Item -Path . -Name "build" -ItemType "directory"
    Copy-Item -Path ".\translator.py" -Destination ".\build\translator.py"
    Copy-Item -Path ".\groq_1.py" -Destination ".\build\groq_1.py"
    Set-Location -Path ".\build"
    python -m PyInstaller -F .\translator.py
    Move-Item -Path ".\dist\translator.exe" -Destination "..\translator.exe"
    Set-Location -Path "..\"
    Remove-Item -Recurse -Force -Path ".\build"
    conda deactivate
    conda env remove --name=translator
}
else {
    Write-Host -BackgroundColor red -ForegroundColor white "conda not found. Please install conda first."
}