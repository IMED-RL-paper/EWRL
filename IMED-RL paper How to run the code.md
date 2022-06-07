# IMED-RL paper: How to run the code

You can run our code by running `python3 main_SSH.py` from within the main directory.
This will fill the file `./experiments/results` with plots that can be interpreted.

Within the `main_SSH.py` you can decide the environment by uncommenting the one you want to test, decide the time horizon and the number of replicates.

If your system is windows, please go to the `./experiments/utils.py` file, comment the line 14 and uncomment the line 13. Then you can proceed as usual.

Be aware that this code will run on how many cores are available.

## Installing requirements

Depending on preferences, both a file `requirements.txt` and a `setup.py` file are given.
