from process import process_datasets

"""Runs the algorithms on Inspec and 500N datasets and outputs stats. """


def main(algorithm="saliencerank", data_set="inspec"):
    algorithms = {"textrank": 0, "tpr": 1, "saliencerank": 2, "singletpr": 3}
    if algorithm in algorithms:
        print("running algorithm:", algorithm)
        process_datasets(algorithms[algorithm], data_set)


if __name__ == "__main__":
    algorithm = "tpr"  # Set this to "textrank", "tpr", "singletpr" or "saliencerank"
    # algorithm = "saliencerank"  # Set this to "textrank", "tpr", "singletpr" or "saliencerank"

    data_set = "500N"
    main(algorithm, data_set)
