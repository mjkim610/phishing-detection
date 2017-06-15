# Load libraries
import sys

# Load modules
from modules.can_access import can_access
from modules.check_post_action import check_post_action
from modules.has_password_field import has_password_field
from modules.html_has_same_domain import html_has_same_domain
from modules.is_masquerading import is_masquerading
from modules.naver.uses_stylesheet_naver import uses_stylesheet_naver
from modules.naver.check_title import check_title
from modules.has_correct_favicon import has_correct_favicon

# Define constants
TRAINING_SET = "files/training_set.csv"
TRAINING_SET_ANALYZED = "files/training_set_analyzed.csv"
LOG = "logs/log"
ERROR_LOG = "logs/error_log"

def calculate_features():

    def write_encoded_features(write_file, result):
        result_encoded = "0"
        if (result == "U"):
            result_encoded = "0"
        elif (result == "SL"):
            result_encoded = "-0.5"
        elif (result == "S"):
            result_encoded = "-1"
        elif (result == "PL"):
            result_encoded = "0.5"
        elif (result == "P"):
            result_encoded = "1"
        write_file.write("," + result_encoded)

    with open(TRAINING_SET_ANALYZED, "w") as ts_analyzed: # this causes error when calling from a different path
        # write header
        ts_analyzed.write("url,is_phishing,is_masquerading,html_has_same_domain,has_password_field,check_post_action\n")

        with open(TRAINING_SET, "r") as training_set:
            lines = training_set.readlines()
            counter = 0
            can_access_error_count = 0
            for line in lines[1:]:
                try:
                    line = line.rstrip()

                    url = line.split(",")[0]
                    is_phishing = line.split(",")[1]

                    counter += 1
                    with open(LOG, "a+") as log:
                        log.write("Count " + str(counter) + ": " + url + "\n")
                        print("Count " + str(counter) + ": " + url)
                    log.close()

                    # if web page cannot be accessed, other modules will not work
                    result, resp, mod = can_access(url)
                    if result != "U":

                        ts_analyzed.write(url)
                        ts_analyzed.write("," + is_phishing)

                        # calculate each feature
                        result, mod = is_masquerading(url)
                        write_encoded_features(ts_analyzed, result)

                        result, mod = html_has_same_domain(url, resp)
                        write_encoded_features(ts_analyzed, result)

                        result, mod = has_password_field(resp)
                        write_encoded_features(ts_analyzed, result)

                        """
                        result, mod = uses_stylesheet_naver(resp)
                        write_encoded_features(ts_analyzed, result)

                        result, mod = check_title(url, resp)
                        write_encoded_features(ts_analyzed, result)

                        result, mod = has_correct_favicon(url, resp)
                        write_encoded_features(ts_analyzed, result)
                        """

                        result, mod = check_post_action(resp)
                        write_encoded_features(ts_analyzed, result)

                        ts_analyzed.write("\n")
                    else:
                        can_access_error_count += 1
                        with open(LOG, "a+") as log:
                            log.write("can_access error\n")
                            print("can_access error")
                        log.close()
                except:
                    with open(ERROR_LOG, "a+") as error_log:
                        error_log.write("Count " + str(counter) + ": " + url + "\n")
                        error_log.write(sys.exc_info()[0])
                    error_log.close()
        training_set.close()
    ts_analyzed.close()

if __name__ == "__main__":
    calculate_features()