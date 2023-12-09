import re
def parse_string(string):
    res = re.split('(\d+)', string)
    final = { "first_name": res[0], "last_name":res[2], "id": str(int(res[3]))}
    print(final)

parse_string('Robert000Smith000123')


