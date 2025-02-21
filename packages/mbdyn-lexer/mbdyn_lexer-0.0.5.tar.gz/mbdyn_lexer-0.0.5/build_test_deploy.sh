cd mbdyn-lexer || exit

echo "Prepare test environment"
source .testvenv/bin/activate || exit
pip uninstall --yes mbdyn_lexer
pip install pygments
pytest -v || exit # before build test
deactivate

exit

echo "Enter build environment"
source ../.venv/bin/activate
python -m build || exit
tar tf dist/*.tar.gz
unzip -l dist/*.whl
deactivate
echo "Leave build environment"
echo ""
echo "Enter test environment"
source ../.testvenv/bin/activate
pip install dist/mbdyn_lexer-0.0.5-py3-none-any.whl
pygmentize -H lexer mbdyn
deactivate
echo "Leave test environment"
echo ""
echo "Deploy"
