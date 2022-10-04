# Lab 02

# Project name: Math Series

## Author: Mohammad Alfayoume

## Links and Resources
* https://realpython.com/python-optional-arguments/

* https://stackabuse.com/test-driven-development-with-pytest/

## setup new project

mkdir math-series

cd math-series

touch README.md

mkdir math_series

cd math_series

touch math_script.py

mkdir tests

cd tests

touch __init__.py

python -m venv .venv

source .venv/bin/activate

touch .gitignore

**Before you complete the steps fill the gitignore with content:**

https://www.toptal.com/developersgitignore/api/python

pip freeze > requirements.txt

pip install pytest

git init

git add .

git commit -m "first commit"

**Create a new repo in github without README.md file**

git remote add origin the_url_you_copied_that_ends_with_git

git branch -M main

git push -u origin main

## How to test your application

Write this command in your terminal

> pytest