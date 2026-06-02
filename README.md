# NOUR-2026-GitHub-Exercise
This is a small repository mimicking the basic structure of research code. There are some TODOs in all of the files that students should complete in separate branches, dealing with merge conflicts as they appear, and submit pull requests.

---

## Instructions

Below are a list of tasks to do, each student should decide which task to work on.

* `script.py`
    * Replace all instances of `print()` with `logging.info()`
    * Experiment one should print out a random number between 1-10
    * Store data in a DataFrame in a column called results
    * Return the average gotten from the `df` argument
    * Use `arg.repeats` to determine the number of repetitions for `experiment_one()`
    * Use `df.plot(kind="bar")` to output the results in main
    * Create your own experiment using the `df`, name your function `experiment_NAME(df: pd.DataFrame)` and insert it somewhere into the `main()` function

* `requirements.txt`
    * Create a `requirements.txt` file for users

* `run_script.sh`
    * Activate the virtual environment (called `venv`) and add `-r 10` flag to `python script.py` 
    * Create a `run_script.bat` for Windows users

* `.gitignore`
    * Ignore all files located in the `results/` folder, but **do not** ignore the `results/` folder itself