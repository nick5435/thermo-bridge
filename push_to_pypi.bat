@ECHO ON
cd ThermoPyle/
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/* -r testpypi
twine upload dist/*