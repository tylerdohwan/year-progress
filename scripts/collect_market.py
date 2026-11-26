import csv, datetime, io, json, math, pathlib, urllib.request

def parse(raw):
    rows = {}
    for row in csv.DictReader(io.StringIO(raw)):
        day = datetime.date.fromisoformat(row["observation_date"] if "observation_date" in row else row["DATE"])
        try:
            value = float(row["DGS30"])
        except (ValueError, TypeError):
            continue
        if math.isfinite(value) and day <= datetime.date.today():
            rows[day.isoformat()] = value
    if len(rows) < 2:
        raise ValueError("Insufficient valid observations")
    return sorted(rows.items())

def main():
    path = pathlib.Path("market-data.json")
    data = json.loads(path.read_text()) if path.exists() else {}
    start = (datetime.date.today()-datetime.timedelta(days=100)).isoformat()
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS30&cosd=" + start
    with urllib.request.urlopen(url, timeout=30) as response:
        rows = parse(response.read().decode("utf-8-sig"))
    day, value = rows[-1]
    if day < data.get("DGS30", {}).get("date", ""):
        raise ValueError("Source older than saved observation")
    data["DGS30"] = {"date": day, "value": value, "source": "FRED DGS30 / Federal Reserve H.15", "status": "daily", "change_bp": round((value-rows[-2][1])*100, 2), "history": [{"date": d, "value": v} for d,v in rows[-60:]]}
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(data, indent=2, ensure_ascii=False)+"\n")
    temp.replace(path)

if __name__ == "__main__":
    main()
