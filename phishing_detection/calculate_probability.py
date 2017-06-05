import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier

from modules.can_access import can_access
from modules.check_post_action import check_post_action
from modules.has_correct_favicon import has_correct_favicon
from modules.has_password_field import has_password_field
from modules.html_has_same_domain import html_has_same_domain
from modules.is_masquerading import is_masquerading
from modules.naver.check_title import check_title
from modules.naver.uses_stylesheet_naver import uses_stylesheet_naver

TRAINING_SET_FILE_PATH = "files/training_set.csv"
RAW_DATA_FILE_PATH = "files/raw_data.csv"
MODIFIED_DATA_FILE_PATH = "files/modified_data.csv"
UNKNOWN = "U"

def calculate_features():
    with open(RAW_DATA_FILE_PATH, "w") as raw_data_file:  # this causes error when calling from a different path
        # write header
        raw_data_file.write("is_phishing,is_masquerading,can_access,html_has_same_domain,has_password_field,uses_stylesheet_naver,check_title,has_correct_favicon,check_post_action\n")

        with open(TRAINING_SET_FILE_PATH, "r") as training_set:
            lines = training_set.readlines()
            for line in lines:
                line = line.rstrip()
                url = line.split(",")[0]
                is_phishing = line.split(",")[1]

                raw_data_file.write(is_phishing+",")

                # calculate each feature
                result, mod = is_masquerading(url)
                raw_data_file.write(result+",")

                result, resp, mod = can_access(url)
                raw_data_file.write(result+",")
                # if web page cannot be accessed, other modules will not work
                if result != UNKNOWN:

                    result, mod = html_has_same_domain(url, resp)
                    raw_data_file.write(result + ",")

                    result, mod = has_password_field(resp)
                    raw_data_file.write(result + ",")

                    result, mod = uses_stylesheet_naver(resp)
                    raw_data_file.write(result + ",")

                    result, mod = check_title(url, resp)
                    raw_data_file.write(result + ",")

                    result, mod = has_correct_favicon(url, resp)
                    raw_data_file.write(result + ",")

                    result, mod = check_post_action(resp)
                    raw_data_file.write(result)

                else:
                    raw_data_file.write("U,U,U,U,U,U")

                raw_data_file.write("\n")
        training_set.close()

def calculate_probability():
    calculate_features()