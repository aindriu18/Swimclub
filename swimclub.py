from statistics import mean
FOLDER = "swimdata/"


def read_swim_data(filename):
    """ Return swim data from a file"""

    swimmer, age, distance, stroke = filename.removesuffix("txt").split("-")

    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times = lines[0].strip("\n").split(",")

    converts = []
    for swim_times in times:
        if ":" in swim_times:
            minutes, rest = swim_times.split(":")
            seconds, hundreths = rest.split(".")
        else:
            minutes = 0
            seconds, hundreths = swim_times.split(".")
        converts.append((int(minutes) * 60 * 100) +
                        (int(seconds) * 100) + int(hundreths))

    average = mean(converts)
    min_secs, hundreths = str(round(average/100, 2)).split(".")
    min_secs = int(min_secs)
    minutes = min_secs // 60
    seconds = min_secs - minutes*60
    average = str(minutes) + ":" + str(seconds) + ":" + hundreths

    return swimmer, age, distance, stroke, times, average
