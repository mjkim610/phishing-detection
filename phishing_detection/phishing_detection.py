import sys, getopt
from integrate import integrate

########
# Usage
# python phishing_detection.py -s [string] -f [file]
########

DEFAULT_URL = "https://www.naver.com/"

def call_integrate(url):
    try:
        return integrate(url)
    except:
        print("Error(001): integrate() failed")

def main(argv):
    url = DEFAULT_URL
    input_file_path = "files/urls.txt"

    try:
        opts, args = getopt.getopt(argv, "hs:f:", ["string=", "file="])
    except getopt.GetoptError:
        print("Error(000): invalid options")
        print("phishing_detection.py -s <string> -f <file>")
        sys.exit(2)

    if (not opts):
        print("Running script on default url.")
    else:
        for opt, arg in opts:
            if opt == '-h':
                print("phishing_detection.py -s <string> -f <file>")
                sys.exit()
            elif opt in ("-s", "--string"):
                url = arg
                call_integrate(url)
            elif opt in ("-f", "--file"):
                input_file_path = arg

                with open(input_file_path, "r") as input_file:
                    with open("files/results.txt", "w") as output_file:
                        # write header
                        output_file.write('url,verdict\n')

                        # call integrate for each url
                        urls = input_file.readlines()
                        for url in urls:
                            url = url.rstrip()
                            result = call_integrate(url)
                            output_file.write(url + "," + result + "\n")
                        output_file.close()
                        input_file.close()



if __name__ == "__main__":
    print("===============Starting phishing_detection.py===============")
    main(sys.argv[1:])
    print("===============Finishing phishing_detection.py==============")
