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

def call_integrate_for_file(input_file_path, output_file_path):
    with open(input_file_path, "r") as input_file:
        with open(output_file_path, "w") as output_file:  # this causes error when calling from a different path
            # write header
            output_file.write("url,verdict\n")

            # call integrate for each url
            urls = input_file.readlines()
            for url in urls:
                url = url.rstrip()
                result = call_integrate(url)
                output_file.write(url + "," + result + "\n")
        output_file.close()
    input_file.close()

def main(argv):
    url = DEFAULT_URL
    has_infile = False
    has_outfile = False
    input_file_path = "files/urls.csv"
    output_file_path = "files/results.csv"

    try:
        opts, args = getopt.getopt(argv, "hs:i:o:", ["help", "string=", "infile=", "outfile="])
    except getopt.GetoptError:
        print("Error(000): invalid options")
        print("phishing_detection.py -s <string> -i <input_file> -o <output_file>")
        return

    if (not opts):
        print("Running script on default url.")
        call_integrate(url)
    else:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("phishing_detection.py -s <string> -i <input_file> -o <output_file>")
                return
            elif opt in ("-s", "--string"):
                url = arg
                call_integrate(url)
            elif opt in ("-i", "--infile"):
                has_infile = True
                input_file_path = arg
            elif opt in ("-o", "--outfile"):
                has_outfile = True
                output_file_path = arg

            if (has_outfile and not has_infile):
                print("Error(002): requires input_file")
            if (has_infile):
                call_integrate_for_file(input_file_path, output_file_path)

if __name__ == "__main__":
    print("===============Starting phishing_detection.py===============")
    main(sys.argv[1:])
    print("===============Finishing phishing_detection.py==============")
