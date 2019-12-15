### LIBRARIES ###
# Global libraries
import os
# Custom libraries
from tests.test_input_loader import test_loading_txt

test_loading_txt(os.path.join("data", "sample_csv.txt"))
