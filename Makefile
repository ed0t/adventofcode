PYLINT_FLAGS = -E
current_dir := advent_of_code
app_name            = advent_of_code
version             = $(or $(VERSION), latest)

python_version  = 3.12.1


pyenv:
	@pyenv install -s $(python_version)
	@pyenv virtualenvs | grep "$(python_version)/envs/$(current_dir)" || pyenv virtualenv $(python_version) $(current_dir)
	@echo $(python_version)/envs/$(current_dir) > .python-version


pyenv-uninstall:
	@rm .python-version
	@pyenv uninstall -f $(current_dir)


.PHONY: pyenv pyenv-uninstall

