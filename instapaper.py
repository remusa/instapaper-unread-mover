import csv

from pyinstapaper.instapaper import Instapaper, Folder

# https://pyinstapaper.readthedocs.io/en/latest/readme.html

""""
artofmanliness
austinkleon
calnewport
elsyreyes
fourhourworkweek
freecodecamp
jamesaltucher
lifehacker
marksdailyapple
scotthyoung
youarenotsosmart
"""

INSTAPAPER_KEY = 'MY_INSTAPAPER_API_KEY'
INSTAPAPER_SECRET = 'MY_INSTAPAPER_API_SECRET'
INSTAPAPER_LOGIN = 'rene.as.himself@gmail.com'
INSTAPAPER_PASSWORD = 'gdCt3CP^#dX9%r$489Q9*@#d2'

# instapaper = Instapaper(INSTAPAPER_KEY, INSTAPAPER_SECRET)
# instapaper.login(INSTAPAPER_LOGIN, INSTAPAPER_PASSWORD)

file_original = "instapaper-export.csv"
filter_term = "fourhourworkweek"
filter_folder = "Unread"
file_input = "input.csv"
file_output = "output-" + filter_folder + "-" + filter_term + ".csv"


def remove_not_unread():
    with open(file_original, "r", newline="", encoding="utf8") as fin, open(file_input, "w", newline="",
                                                                            encoding="utf8") as fout:

        reader = csv.reader(fin, delimiter=",")
        writer = csv.writer(fout, delimiter=",", quotechar="'")

        for row in reader:
            try:
                for i in row:
                    if i == filter_folder:
                        writer.writerow(row)

            except IndexError:
                print("Error: ", row)


def filter_unread():
    with open(file_input, "r", newline="", encoding="utf8") as fin, open(file_output, "w", newline="",
                                                                         encoding="utf8") as fout:

        reader = csv.reader(fin, delimiter=" ")
        writer = csv.writer(fout, delimiter=" ", quotechar="|")

        for row in reader:
            try:
                if filter_term in row[0]:
                    writer.writerow(row)

            except IndexError:
                print("Error: ", row)


def instapaper():
    print("test")


def main():
    remove_not_unread()
    filter_unread()
    instapaper()


if __name__ == '__main__':
    main()

main()
