import random

TRAINING_SET_PHISH = "files/raw_data/verified_online.csv"
TRAINING_SET_SAFE = "files/raw_data/top-1m.csv"
TRAINING_SET_COMBINED = "files/training_set.csv"

def prepare_data():
    with open(TRAINING_SET_COMBINED, "w") as training_set_combined:  # this causes error when calling from a different path
        with open(TRAINING_SET_PHISH, "r") as training_set_phish:

            counter = 0
            lines = training_set_phish.readlines()
            for line in lines:
                line = line.rstrip()
                url = line.split(",")[1]
                is_phishing = line.split(",")[4]
                is_online = line.split(",")[6]

                if (is_phishing == "yes" and is_online == "yes"):
                    training_set_combined.write(url + "," + "1")
                    training_set_combined.write("\n")
                    counter += 1

                if (counter >= 1000):
                    break
        training_set_phish.close()

        with open(TRAINING_SET_SAFE, "r") as training_set_safe:

            counter = 0
            lines = training_set_safe.readlines()
            for line in lines:
                line = line.rstrip()
                url = line.split(",")[1]

                training_set_combined.write("http://" + url + "," + "0")
                training_set_combined.write("\n")
                counter += 1

                if (counter >= 9000):
                    break
        training_set_safe.close()

    training_set_combined.close()

def shuffle_data():
    with open(TRAINING_SET_COMBINED, "r") as file:
        lines = file.readlines()
    file.close()

    random.shuffle(lines)

    with open(TRAINING_SET_COMBINED, "w") as file:
        # write header
        file.write("url,is_phishing\n")
        file.writelines(lines)
    file.close()

if __name__ == "__main__":
    prepare_data()
    shuffle_data()