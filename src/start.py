import os

if not os.path.exists('.venv'):
    os.mkdir('.venv')
    os.system('pip install pipenv')
    os.system('pipenv --three')
    os.system('pipenv install')
    os.system('alembic upgrade head')
