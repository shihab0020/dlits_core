<<<<<<< HEAD
# DLITS Core

`dlits_core` is a custom ERPNext app developed by DLITS to centralize all internal business logic and customizations.

## Features

- Custom fields and property setters
- Client and server scripts
- Doctype class overrides
- Centralized logic for Sales, HR, Inventory, and more

## Installation

```bash
# Get the app
bench get-app https://github.com/shihab0020/dlits_core.git

# Install it on your site
bench --site your-site-name install-app dlits_core
=======
### Dlits Core

Dlits Custom For ErpNext

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app dlits_core
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/dlits_core
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
>>>>>>> d1c6a49 (feat: Initialize App)
