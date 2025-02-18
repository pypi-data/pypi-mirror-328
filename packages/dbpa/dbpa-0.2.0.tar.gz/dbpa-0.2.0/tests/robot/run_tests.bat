@echo off
echo Running DBPA Robot Framework Tests

REM Create virtual environment if it doesn't exist
if not exist venv (
    python -m venv venv
    call venv\Scripts\activate
    pip install -r ../../requirements.txt
    pip install -e ../..
) else (
    call venv\Scripts\activate
)

REM Run tests in parallel using pabot
pabot --processes 2 ^
    --outputdir results ^
    --report report.html ^
    --log log.html ^
    --output output.xml ^
    tests/installation/package_installation.robot ^
    tests/functional/database_operations.robot ^
    tests/functional/ai_integration.robot

REM Generate combined reports
rebot --outputdir results ^
    --report report.html ^
    --log log.html ^
    --output output.xml ^
    results/output.xml

echo Test execution completed. Check results/report.html for the test report.
