### LIBRARIES ###
# Global libraries
import os
import yaml
from termcolor import colored

# Custom libraries

### CODE ###


def convert_type(variable, type_info):
    """
        Given a variable, converts it to the given type. 
    """
    if type_info == "str":
        return str(variable)
    elif type_info == "int":
        return int(variable)
    elif type_info == "bool":
        return variable == "True"
    elif type_info == "float":
        return float(variable)


def load_input_config():
    """
        Loads the config file `configs/input.yml`
    """
    with open(os.path.join("configs", "input.yml"), "r") as yml_file:
        return yaml.safe_load(yml_file)


def load_txt_file(filepath):
    """
        Given the path of a .txt file (in HTTP access log format), loads the file.
    """
    # Load the config file for the input
    cfg = load_input_config()

    log_lines = []

    with open(filepath, "r") as f:
        line_headers = f.readline()
        try:
            # If such a line exists, process the headers
            headers = line_headers.replace(
                "\"", "").replace("\n", "").split(",")

            line = line_headers
            while line:
                line = f.readline()
                # Process the log line to get the infos
                log_infos = line.replace(
                    "\"", "").replace("\n", "").split(",")
                log_item = {}
                for i, info in enumerate(log_infos):
                    header = headers[i]
                    log_item[header] = convert_type(
                        info, cfg["headers_type"][header])
                # Save this log line in a list
                log_lines.append(log_item)

        except Exception as e:
            print(colored("ERROR: {}".format(e), "red"))

    return log_lines


def load_txt_file_batch(filepath):
    """
        Given the path of a .txt file (in HTTP access log format), loads the file
        and yields line by line.
    """
    # Load the config file for the input
    cfg = load_input_config()

    with open(filepath, "r") as f:
        line_headers = f.readline()
        try:
            # If such a line exists, process the headers
            headers = line_headers.replace(
                "\"", "").replace("\n", "").split(",")

            line = line_headers
            while line:
                line = f.readline()
                # Process the log line to get the infos
                log_infos = line.replace("\"", "").replace("\n", "").split(",")
                log_item = {}
                for i, info in enumerate(log_infos):
                    header = headers[i]
                    log_item[header] = convert_type(
                        info, cfg["headers_type"][header])
                # Yield this log line
                yield log_item
        except Exception as e:
            print(colored("ERROR: {}".format(e), "red"))
