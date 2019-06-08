# python_vscode_project_template

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

## ツール
- black
    - 参考: [もうPythonの細かい書き方で議論しない。blackで自動フォーマットしよう](https://blog.hirokiky.org/entry/2019/06/03/202745)
    - 2019/06/08現在、blackを使用するとバージョンエラーが出るため、Pipfileに`prerelease = true`を記載
        - [Pipenvでよく出喰わす問題](https://pipenv-ja.readthedocs.io/ja/translate-ja/diagnose.html)
- pytest
    - 参考: [pytest入門 - 闘うITエンジニアの覚え書き](https://www.magata.net/memo/index.php?pytest%C6%FE%CC%E7)
