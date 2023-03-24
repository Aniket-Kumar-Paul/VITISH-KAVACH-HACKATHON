# Backend

## Setup

### Create Env 

1. Execute ``python3 -m venv venv`` to create your local env
2. Activate the env using the required command
   1. Windows : ``.\venv\Scripts\activate``
   2. Linux : ``source ./venv/bin/activate``
   3. Mac : ``source ./venv/bin/activate``
3. Install dependencies : ``pip install -r requirements.txt``

### Setup DB

1. Start postgres
2. Create a database ion postgres for the project

### Setup ``.env``

1. Create ``.env`` in this directory
2. Define values that are listed in ``.env.sample``


### Execute

1. To run the project : ``sh dev.sh``