<!--
SPDX-FileCopyrightText: © 2024 University of Bristol
SPDX-License-Identifier: CC-BY-SA-4.0
-->

<!-- markdownlint-disable-file MD028 -->

# Isambard

The Isambard website is written using [Material for MkDocs][material].

## Material for MkDocs Installation

1. Create a Python virtual environment:
    - On macOS and Linux create a new virtual environment in a suitable location:

      ```bash
      python3 -m venv material
      ```

1. Activate the virtual environment:
    - On macOS and Linux:

      ```bash
      source material/bin/activate
      ```

1. Install MkDocs and other packages to build the docs (`requirements.txt`) and additional dependencies for development (`requirements-dev.txt`):

    ```bash
    pip install -r requirements.txt -r requirements-dev.txt
    ```

Alternatively, install in a Conda environment

```bash
conda env create --file environment.yml
conda activate isambard-apply-docs-env
```

## Dev container and GitHub Codespaces

A [dev container][containers.dev] [metadata JSON file][metadata-ref-containers.dev] ([devcontainer.json](./.devcontainer/devcontainer.json)) is provided that defines a `apply.isambard.ac.uk` documentation development environment.

The dev container builds on the [official Material for MkDocs Docker image][squidfunk-mkdocs-material-dockerhub], ensuring that processes run as an unprivileged user and additional dependencies for building and editing `apply.isambard.ac.uk` are installed for this user.
The container is set up to run `mkdocs serve` in the background when a development tool (e.g. VSCode) is attached and will automatically forward the port `mkdocs serve` is listening on.

The dev environment can be launched using [dev-container-compatible tooling][tooling-containers.dev], e.g. VSCode (with [Dev Containers extension][dev-containers-vscode-ext]) and [GitHub Codespaces][dev-containers-github-codespaces-docs].

The [dev container definition](./.devcontainer/devcontainer.json) will automatically be used when launching a GitHub Codespace for this repository, allowing a fully functional documentation writing environment to be rapidly started within a web browser in a few steps:

1. Open the repository in a web browser: <https://github.com/isambard-sc/apply.isambard.ac.uk>
1. Select the `<> Code` button to open a dialog, open the `Codespaces` tab in the dialog
1. Select the `+` button to start a Codespace (with default configuration) on the current branch, or select `New with options...` in the `...` menu to configure the Codespace
1. The Codespace will open in the web browser and take a short while to start the container and build the environment
1. When the environment is built `mkdocs serve` will be running in the background listening on port 8000 which is automatically forwarded (privately)
1. The documentation can now be edited in the Codespace using the [usual documentation development workflow](#updating-the-isambard-documentation-website), though with the repository automatically cloned into `/docs` and `mkdocs serve` already running in the background
1. To view a live preview of the documentation served by `mkdocs serve`, open the VSCode Ports view (`Ports: Focus on Ports View` from command palette), then alt-select the unique address under the `Forwarded Address` column and select one of `Open in Browser` or `Preview in Editor` from the menu

When finished with your Codespace (after committing and pushing any work to the GitHub repository), you can stop or delete it at <https://github.com/codespaces> by opening the `...` menu for the Codespace (listed under "Your codespaces") and selecting `Stop codespace` or `Delete`.

> [!NOTE]
> Ports forwarded by GitHub Codespaces are made available via a unique URL which is private and only accessible to the Codespace creator by default.
> The creator needs to authenticate to GitHub to access the forwarded port (though typically will already be authenticated when opening the URL in the same browser session as the Codespace is running).
> For more information on Codespaces port forwarding see [Forwarding ports in your codespace][forwarding-ports-github-codespaces-docs] and [Security in GitHub Codespaces][port-forwarding-security-github-codespaces-docs].

> [!TIP]
> Be aware that GitHub Codespaces are charged for based on compute and storage usage.
> Free accounts have a generous default allocation of storage and compute and no charges will be made beyond this unless your account is configured to enable this (see [About billing for GitHub Codespaces][billing-github-codespaces-docs]).
> Stopping or deleting a Codespace when not in use helps reduce chargeable usage.

[containers.dev]: https://containers.dev/
[metadata-ref-containers.dev]: https://containers.dev/implementors/json_reference/
[squidfunk-mkdocs-material-dockerhub]: https://hub.docker.com/r/squidfunk/mkdocs-material/
[tooling-containers.dev]: https://containers.dev/supporting
[dev-containers-vscode-ext]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
[dev-containers-github-codespaces-docs]: https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers
[forwarding-ports-github-codespaces-docs]: https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace
[port-forwarding-security-github-codespaces-docs]: https://docs.github.com/en/codespaces/reference/security-in-github-codespaces#port-forwarding
[billing-github-codespaces-docs]: https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces

## Updating the Isambard documentation website

1. Clone this repository in to a new directory using your preferred method (GitHub Desktop is ideal for beginners).
1. Create a new branch for your changes.
1. Activate the Python virtual environment like when creating the new environment instructions above.
Navigate to the repository you cloned and branched in a terminal.
1. Start serving the documentation set in the environment by running `mkdocs serve`. (If this doesn't work something is wrong with your virtual environment)
1. Browse to `http://127.0.0.1:8000` if a browser didn't open automatically with the previous command.
1. Edit the documentation with your preferred editor and view the changes live in the browser.
1. When finished push your changes back to your branch.
1. Create a pull request to request your changes be merged in to the `main` branch.
1. When your changes have been merged in to `main` the documentation will be built and published automatically.
1. Your branch can then be removed.

### Navigation

For a document to appear in the site navigation, add the path to the document to the list under the `nav` key in [`mkdocs.yml`](./mkdocs.yml).
Documents not in `nav` but under the `docs/` directory will be included in the site build and available via search, but will not appear in the site navigation menu.

### Draft documents

To merge work-in-progress documentation into `main` without including it in the built (and published) GitHub Pages site, add the path of the work-in-progress document to the list under the `draft_docs` key in [`mkdocs.yml`](./mkdocs.yml).
These documents will be available to view via `mkdocs serve` (marked "DRAFT"), but will not be included in the build, see [MkDocs Configuration][draft-docs-config-mkdocs-docs].

Draft documents should not be listed in `nav`, as this leads to blank entries in the site navigation menu.
If a draft document is to be included in `nav`, it is recommended to comment the line for that document under `nav`.

When the draft document is ready to publish, remove it from `draft_docs` and uncomment the corresponding line under `nav` (if present) in [`mkdocs.yml`](./mkdocs.yml).

[draft-docs-config-mkdocs-docs]: https://www.mkdocs.org/user-guide/configuration/#draft_docs

## [CSpell][cspell]

This repository uses `Code spell checker`.  Please see the details below on how to install it on your editor:

- Configuration file: [cspell.config.yaml](./cspell.config.yaml)
- CLI tool: [cspell-cli][cspell-cli-github]
- VSCode extension: [Code Spell Checker][vscode-spell-checker-extension]

[Material]: https://squidfunk.github.io/mkdocs-material/
[cspell]: https://cspell.org/
[cspell-cli-github]: https://github.com/streetsidesoftware/cspell-cli
[vscode-spell-checker-extension]: https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker

### [markdownlint][markdownlint-github]

This repository also uses `markdownlint`. See below for details on how to configure and install the tool:

- Configuration file: [.markdownlint.yaml](./.markdownlint.yaml)
- CLI tool: [markdownlint-cli][markdownlint-cli-github], [markdownlint-cli2][markdownlint-cli2-github]
- VSCode extension: [markdownlint][vscode-markdownlint-extension]

[markdownlint-github]: https://github.com/DavidAnson/markdownlint
[markdownlint-cli-github]: https://github.com/igorshubovych/markdownlint-cli
[markdownlint-cli2-github]: https://github.com/DavidAnson/markdownlint-cli2
[vscode-markdownlint-extension]: https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint
