# Load libraries
import pandas
"""
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
"""

# Load modules
from modules.can_access import can_access
from modules.check_post_action import check_post_action
from modules.has_correct_favicon import has_correct_favicon
from modules.has_password_field import has_password_field
from modules.html_has_same_domain import html_has_same_domain
from modules.is_masquerading import is_masquerading
from modules.naver.check_title import check_title
from modules.naver.uses_stylesheet_naver import uses_stylesheet_naver

# Define constants
TRAINING_SET = "files/training_set.csv"
TRAINING_SET_ANALYZED = "files/training_set_analyzed.csv"

def calculate_features():
    with open(TRAINING_SET_ANALYZED, "w") as ts_analyzed: # this causes error when calling from a different path
        # write header
        ts_analyzed.write("url,is_phishing,is_masquerading,can_access,html_has_same_domain,has_password_field,uses_stylesheet_naver,check_title,check_post_action\n")

        with open(TRAINING_SET, "r") as training_set:
            lines = training_set.readlines()
            counter = 0
            for line in lines[1:]:
                line = line.rstrip()

                url = line.split(",")[0]
                is_phishing = line.split(",")[1]

                counter += 1
                print("Count: " + str(counter))
                print("Analyzing: " + url)

                ts_analyzed.write(url+",")
                ts_analyzed.write(is_phishing+",")

                # calculate each feature
                result, mod = is_masquerading(url)
                ts_analyzed.write(result+",")

                result, resp, mod = can_access(url)
                ts_analyzed.write(result+",")
                # if web page cannot be accessed, other modules will not work
                if result != "U":

                    result, mod = html_has_same_domain(url, resp)
                    ts_analyzed.write(result + ",")

                    result, mod = has_password_field(resp)
                    ts_analyzed.write(result + ",")

                    result, mod = uses_stylesheet_naver(resp)
                    ts_analyzed.write(result + ",")

                    result, mod = check_title(url, resp)
                    ts_analyzed.write(result + ",")

                    """
                    result, mod = has_correct_favicon(url, resp)
                    raw_data_file.write(result + ",")
                    """

                    result, mod = check_post_action(resp)
                    ts_analyzed.write(result)

                else:
                    ts_analyzed.write("U,U,U,U,U,U")

                ts_analyzed.write("\n")
        training_set.close()
    ts_analyzed.close()

if __name__ == "__main__":
    # Load dataset
    dataset = pandas.read_csv(TRAINING_SET)

    # shape
    # how many instances (rows) and how many attributes (columns)
    print(dataset.shape)
    # head
    print(dataset.head(20))
    # descriptions
    print(dataset.describe())
    # class distribution
    print(dataset.groupby('is_phishing').size())

    calculate_features()