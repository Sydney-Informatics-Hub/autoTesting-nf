# **autoTesting-nf**

Automated testing testing for SIH Nextflow workflows. This repository houses testing and outcomes for testing various code linting tools that can be integrated into SIH Nextflow workflows. 

# Focus and priorities 

Standardisation and automated testing of SIH Nextflow workflows. Devising a set of rules and protocol for linting workflows. Starting with basic formatting and set up of repositories, following DSL2 template:

* README contains sections from [documentation guide](https://github.com/AustralianBioCommons/doc_guidelines), if not give warning
* Code base directory structure matches [template](https://github.com/AustralianBioCommons/Nextflow_DSL2_template)
    * config/
    * modules/
    * main.nf 
    * nextflow.config
    * README.md 
    * CITATION.cff
* All .nf and config files formatted according to...? 
    * EditorConfig 

# Linters 

Linters have rules about how code should look and be structured, they check the code and let you know where pass/fails are. They are a way to inspect code for standardisation. Automated tests support code review and improve code quality. Makes sure everyone stays up to date with formatting rules/guidelines as they change over time. 

## Editorconfig 

[EditorConfig](https://editorconfig.org/) maintains consistent coding styles for multiple developers working on different editors and IDEs. EditorConfig has its own file formatting [specifications](https://spec.editorconfig.org/) that can be used along with custom formatting options. For example, this is the editorconfig specifications used by the [nf-core/rnaseq](https://raw.githubusercontent.com/nf-core/rnaseq/master/.editorconfig) workflow. 

Install the EditorConfig plugin for your chosen editor, go [here](https://editorconfig.org/#download) and follow instructions for downloading and installing the plugin. Note: some editors have limited support for various EditorConfig properities. This extension is activated whenever you open a new text editor, switch tabs into an existing one or focus into the editor you already have open. When activated, it uses editorconfig to resolve the configuration for that particular file and applies any relevant editor settings.

### Outcome

* Mandate `.editorcofig` file in all workflows
* Lint test file exists 
* TODO upload to template

Current `.editorconfig`: 
```
root = true

[main.nf]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_size = 4
indent_style = space

[modules/**]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_size = 4
indent_style = space

[*.{md,yml,yaml,html,css,scss,js,cff}]
indent_size = 2
```

## Prettier

Code formatter that can be used to automatically format your code in a consistent way. It supports several languages, including JavaScript, Python, and HTML. You can use prettier to format your code as part of your Nextflow workflow by running it as a process.

## NPM Groovy linter 

Lint, formats, and auto-fixes Groovy/ Jenkinsfile/ Gradle files. Has a [VScode extension](https://github.com/nvuillam/vscode-groovy-lint). 

## nf-core lint

Lint tools are available and customisable for both pipeline and modules by nf-core tools. Can do high-level checks for things like which files exist, but does not perform any code formatting. Just a set of rules, a way to inspect code for standardisation. The lint command determines which linting tests to run based on the pipeline's linting configuration.  

* Only works on nf-core template workflows 
* Forked repo to get it working on our template 
* TODO identify which files/configs are needed to get it running

https://www.youtube.com/watch?v=DiXh3Dvpq5E 

# Github Actions integration

See https://www.youtube.com/watch?v=ZO4lSma3OA8

# Resources 

* [Recommendations](https://www.nextflow.io/blog/2021/nextflow-developer-environment.html) on setting up Nextflow dev environment 
* [nf-core code linting tools bytesize talk](https://www.youtube.com/watch?v=ZO4lSma3OA8)
* [NPM groovy linter](https://www.npmjs.com/package/npm-groovy-lint) 
* [Prettier](https://github.com/prettier/prettier)
* [EditorConfig](https://editorconfig.org/)
* [VS code groovy lint](https://github.com/nvuillam/vscode-groovy-lint)
* [NPM groovy lint Medium article](https://nicolas.vuillamy.fr/a-groovy-journey-to-open-source-during-covid-19-npm-groovy-lint-8d88c7eecebc)
* [nf-core linting docs](https://github.com/nf-core/tools/#linting-a-workflow)
* [nf-core configuring lint tests](https://www.youtube.com/watch?v=DiXh3Dvpq5E)