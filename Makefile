.PHONY: help lab validate

help:
	@echo "make lab       - launch JupyterLab to open and edit the lesson notebooks"
	@echo "make validate  - execute every notebook to confirm it runs clean (the test suite)"

lab:
	jupyter lab

validate:
	@find . -name '*.ipynb' -not -path './.venv/*' -print0 \
	  | xargs -0 -I{} jupyter nbconvert --to notebook --execute --stdout "{}" > /dev/null \
	  && echo "all notebooks executed clean"
