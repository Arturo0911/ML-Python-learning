from urllib.request import urlopen
import time

class Scrapper:

    def __init__(self):

        with urlopen('https://covid19.who.int/WHO-COVID-19-global-data.csv') as url:

            csv_file = url.read().decode('utf-8')
            outdir = open("csv/WHO-COVID-19-global-data.csv", "w")
            outdir.write(csv_file)
            outdir.close()

if __name__ == "__main__":

    scrapper = Scrapper()