## Runs our paper's experiments and outputs their results
## TODO: Replace all instances of print() with logging.info
## NOTE: Should be imported as logging, use logging.info()
import pandas as pd
import logging
import argparse

from pathlib import Path


# TODO: Experiment one should print out a random number between 1-10
# NOTE: This will include importing random, use random.randint()
def experiment_one() -> int:
    result: int = -1
    logging.info(f"Experiment one produced a result of {result}")
    return result


## TODO: Store data in a DataFrame in a column called results
def experiment_two(data: list) -> pd.DataFrame:
    df: pd.DataFrame = pd.DataFrame()
    logging.info(df.info())
    return df


## TODO: Return the average gotten from the df
def experiment_three(df: pd.DataFrame) -> int:
    avg: float = -1.0
    logging.info(f"The average is {avg:0.3}")
    return avg


## TODO: Use args.repeats to determine the number of times experiment_one repeats
def main(args: argparse.Namespace) -> None:

    data = [experiment_one() for i in range(50)]
    df = experiment_two(data)
    avg = experiment_three(df)

    logging.info("Experiments finished")



def add_args(parser: argparse.ArgumentParser):

    parser.add_argument(
        "-r",
        "--repeats",
        type=int,
        required=False,
        help="Number of times to repeat experiment one\n \n",
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog=f"{__file__.split('/')[-1]}",
        formatter_class=argparse.RawTextHelpFormatter,
        description="Run our paper experiments",
        epilog="Created by Alejandro Ciuba, alc307@pitt.edu",
    )

    add_args(parser)
    args = parser.parse_args()
    main(args)
