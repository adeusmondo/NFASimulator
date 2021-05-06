# Python Template Repository

## Running the project in a local environment or virtual machine

First you must have on your machine:

- Python 3.8 or higher
- This project

#### To run this project on Windows (if you are using PowerShell)

```powerShell
    pip install virtualenv
    Set-ExecutionPolicy AllSigned
    Set-ExecutionPolicy RemoteSigned

    virtualenv .\venv
    .\venv\scripts\activate
    pip install -r requirements.txt
```

#### To run this on Linux

```Bash
    pip3 install virtualenv
    virtualenv /venv
    source /venv/bin/activate
    pip3 install -r requirements.txt
```

#### Exec project

At the root of the project: 

```Bash
python3 -m src.nfa
```

## Running the project in repl.it

You can [access here](https://replit.com/@carlosmondo/NFASimulator)

## DATA

In src / data are the input and output files for this NFA.

The files `definition_automaton` and `inputs` you must fill in with the definition of the automation and the inputs to be executed.

The files `accepted_states` and `process_steps` are the results of the processes