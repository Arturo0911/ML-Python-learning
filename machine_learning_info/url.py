from urllib.request import urlopen

with urlopen("https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv") as csv_file:

    html = csv_file.read().decode('utf-8')
    outdir = open('fifaplayers.csv', 'w')
    outdir.write(html)
    outdir.close()