import pyft
import sys

file = sys.argv[1]

print(file, file=sys.stderr)


tbl = pyft.utils.read_footprint_table(file, long=True)

stub = file.replace("./tbls/", "")
stub = stub.replace(".fire.tbl", "")
ts = stub.split(".")


tbl["file"] = stub
tbl["type"] = ts[0]
tbl["sample"] = ".".join(ts[1:])

tbl.to_csv(sys.stdout, sep="\t", index=False)
