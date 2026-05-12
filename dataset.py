import re

from tokenizer import DAY_TO_IDX
from tokenizer import MONTH_TO_IDX
from tokenizer import BOOL_TO_IDX

def load_data(path):

    X = []
    Y = []

    with open(path, "r") as f:

        lines = f.readlines()

    for line in lines:

        line = line.strip()

        pattern = r"\[(.*?)\] \[(.*?)\] \[(.*?)\] \[(.*?)\] (.*)"

        match = re.match(pattern, line)

        if match:

            day_cond = match.group(1)
            month_cond = match.group(2)
            leap_cond = match.group(3)
            decade_cond = match.group(4)
            date = match.group(5)

            x = [
                DAY_TO_IDX[day_cond],
                MONTH_TO_IDX[month_cond],
                BOOL_TO_IDX[leap_cond],
                int(decade_cond)
            ]

            day, month, year = date.split("-")

            y = [
                int(day),
                int(month),
                int(year)
            ]

            X.append(x)
            Y.append(y)

    return X, Y