import re
import sqlite3

## TODO ##
# Instructions for Agent Ransack export

# TODO use Chest object to reference sqlite obj
# There is currently a sqlite dependency on anything that uses Plunder
class Chest:

    # TODO generate a dbname for the Chest, with a custom override
    def __init__(self, dbname="plunder.sqlite"):
        pass

def add_results_to_db(filename, dbname="plunder.sqlite", override=False):
    "add Agent Ransack results to SQLite3 DB"

    SKIP_LINES = 16 # magic

    conn = sqlite3.connect(dbname)
    conn.text_factory = str

    conn.execute("CREATE TABLE IF NOT EXISTS results (file_name text, file_location text, last_modified text, hits integer, line_num integer, context text)")

    if override:
        conn.execute("DELETE FROM results")

    with open(filename, "r") as infile:
        # skip most of meta at front of file
        for i in range(SKIP_LINES):
            infile.next()

        # TODO grab column widths
        column_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r"\w+", infile.next())]

        # skip blank line after column names
        infile.next()

        for line in infile:
            # ignore non-results lines
            if (line.startswith("Report")):
                # TODO improve this later
                continue

            # process line
            items = []
            for i in range(len(column_indexes)):
                if i + 1 < len(column_indexes):
                    items.append(line[column_indexes[i][0]:column_indexes[i+1][0]].strip())
                else:
                    items.append(line[column_indexes[i][0]:].strip())

            if len(items) < 2:
                # TODO handle this case better later
                continue
            elif len(items) < 6:
                print(items)
            else:
                conn.execute("INSERT INTO results (file_name, file_location, last_modified, hits, line_num, context) VALUES (?, ?, ?, ?, ?, ?)", items)

    conn.commit()
    conn.close()
