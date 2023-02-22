import logging
import os

log = logging.getLogger(__name__)

def files_exist(self):
    """Checks a given pipeline directory for required files.

    Iterates through the pipeline's directory content and checks that specified
    files are either present or absent, as required.

    .. note::
        This test raises an ``AssertionError`` if neither ``nextflow.config`` or ``main.nf`` are found.
        If these files are not found then this cannot be a Nextflow pipeline and something has gone badly wrong.
        All lint tests are stopped immediately with a critical error message.

    Files that *must* be present:

    .. code-block:: bash
        README.md
        main.nf
        nextflow.config
        modules/*
        LICENSE
        CHANGELOG.md
        .gitattributes
        .gitignore
        .editorconfig
        config/standard.config

    Files that *should* be present:

    .. code-block:: bash
        CITATION.cff
        config/nimbus.config
        config/gadi.config
        config/setonix.config

    Files that *should not* be present:

    .. code-block:: bash
        testScripts/*

    .. tip:: You can configure the ``nf-core lint`` tests to ignore any of these checks by setting
            the ``files_exist`` key as follows in your ``.nextflow.yml`` config file. For example:

            .. code-block:: yaml

            lint:
                files_exist:
                    - assets/multiqc_config.yml
    """

    passed = []
    warned = []
    failed = []
    ignored = []

    # NB: Should all be files, not directories
    # List of lists. Passes if any of the files in the sublist are found.
    #: test autodoc
    try:
        _, short_name = self.nf_config["manifest.name"].strip("\"'").split("/")
    except ValueError:
        log.warning("Expected manifest.name to be in the format '<repo>/<pipeline>'. Will assume it is '<pipeline>'.")
        short_name = self.nf_config["manifest.name"].strip("\"'").split("/")

    files_fail = [
        [".gitattributes"],
        [".gitignore"],
        [".editorconfig"],
        ["modules/*"],
        ["config/standard.config"],
        ["main.nf"],
        ["nextflow.config"],
        ["CHANGELOG.md"],
        ["CITATION.cff"],
        ["LICENSE"],
        ["README.md"],
    ]

    files_warn = [
        ["main.nf"],
    ]

    # TODO Remove files that should be ignored according to the linting config
    #ignore_files = self.lint_config.get("files_exist", [])

    def pf(file_path):
        return os.path.join(self.wf_path, file_path)

    # First - critical files. Check that this is actually a Nextflow pipeline
    if not os.path.isfile(pf("nextflow.config")) and not os.path.isfile(pf("main.nf")):
        failed.append("File not found: nextflow.config or main.nf")
        raise AssertionError("Neither nextflow.config or main.nf found! Is this a Nextflow pipeline?")

    # Files that cause an error if they don't exist
    for files in files_fail:
        if any([f in ignore_files for f in files]):
            continue
        if any([os.path.isfile(pf(f)) for f in files]):
            passed.append(f"File found: {self._wrap_quotes(files)}")
        else:
            failed.append(f"File not found: {self._wrap_quotes(files)}")

    # Files that cause a warning if they don't exist
    for files in files_warn:
        if any([f in ignore_files for f in files]):
            continue
        if any([os.path.isfile(pf(f)) for f in files]):
            passed.append(f"File found: {self._wrap_quotes(files)}")
        else:
            warned.append(f"File not found: {self._wrap_quotes(files)}")

    # Files that cause an error if they exist
    for file in files_fail_ifexists:
        if file in ignore_files:
            continue
        if os.path.isfile(pf(file)):
            failed.append(f"File must be removed: {self._wrap_quotes(file)}")
        else:
            passed.append(f"File not found check: {self._wrap_quotes(file)}")

    # Files that cause a warning if they exist
    for file in files_warn_ifexists:
        if file in ignore_files:
            continue
        if os.path.isfile(pf(file)):
            warned.append(f"File should be removed: {self._wrap_quotes(file)}")
        else:
            passed.append(f"File not found check: {self._wrap_quotes(file)}")

    # Files that are ignored
    for file in ignore_files:
        ignored.append(f"File is ignored: {self._wrap_quotes(file)}")

    return {"passed": passed, "warned": warned, "failed": failed, "ignored": ignored}
