### LIBRARIES ###
# Global libraries
import os
from termcolor import colored

# Custom libraries
from src.input_handler.load_from_txt import load_txt_file, load_txt_file_batch

### TESTING FUNCTIONS ###


def test_loading_txt(filepath):
    """
        Tests if loading with batch and loading the complete txt leads 
        to the same result.
    """
    list_from_file = load_txt_file(filepath)
    list_from_batch = []
    batch_loader = load_txt_file_batch(filepath)
    for line_log in batch_loader:
        list_from_batch.append(line_log)

    assert list_from_file == list_from_batch, "Lists aren't equal!"


### CODE ###
if __name__ == "__main__":
    test_loading_txt(os.path.join("data", "sample_csv.txt"))
    print(colored("Everything passed"))
