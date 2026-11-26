import csv, io, json, math, datetime, pathlib, urllib.request
path = pathlib.Path("market-data.json")
data = json.loads(path.read_text())
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS30"
with urllib.request.urlopen(url, timeout=30) as response:
    rows = list(csv.DictReader(io.StringIO(response.read().decode("utf-8-sig"))))
valid = []
for row in rows:
    try:
        date = datetime.date.fromisoformat(row.get("observation_date") or row["DATE"])
        value = float(row["DGS30"])
        if math.isfinite(value) and date <= datetime.date.today():
            valid.append((date, value))
    except (ValueError, KeyError, TypeError):
        continue
if not valid:
    raise RuntimeError("No valid DGS30 observations")
date, value = max(valid)
if date.isoformat() < data["DGS30"]["date"]:
    raise RuntimeError("Source observation older than stored observation")
data["DGS30"] = {"date": date.isoformat(), "value": value, "source": "FRED DGS30", "status": "daily"}
path.write_text(json.dumps(data, indent=2) + "\n")
