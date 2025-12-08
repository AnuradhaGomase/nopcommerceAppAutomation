call .venv\Scripts\activate.bat
@rem For Chrome
::pytest -s -v -m "sanity" --html=Reports\report_chrome.html .\testCases --mybrowser=chrome
::pytest -s -v -m "regression" --html=Reports\report.html .\testCases --mybrowser=chrome
::pytest -s -v -m "sanity or regression" --html=Reports\report.html .\testCases --mybrowser=chrome
::pytest -s -v -m "sanity and regression" --html=Reports\report.html .\testCases --mybrowser=chrome

@rem For Firefox
::pytest -s -v -m "sanity" --html=Reports\report_firefox.html .\testCases --mybrowser=firefox
pytest -s -v -m "regression" --html=Reports\report.html .\testCases --mybrowser=firefox
::pytest -s -v -m "sanity or regression" --html=Reports\report.html .\testCases --mybrowser=firefox
::pytest -s -v -m "sanity and regression" --html=Reports\report.html .\testCases --mybrowser=firefox

pause