# python_vscode_init

## 目的
- Visual Studio Code を使ってpythonのプロジェクトを作成するために必要な開発環境用の構成を揃える

## 前提
- python3
    - python3.6以上を使う
- pyenv
- pipenv
    - プロジェクトごとに.venvディレクトリを作成する
        - bash: `export PIPENV_VENV_IN_PROJECT=true`
        - fish: `set -x PIPENV_VENV_IN_PROJECT true`