import csv, json, collections, os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
HERE=os.path.dirname(__file__); DATA=os.path.normpath(os.path.join(HERE,"..","data"))
CHI=ZoneInfo("America/Chicago")
def ldate(ms):
    if ms in (None,""): return None
    return datetime.fromtimestamp(int(ms)/1000, tz=timezone.utc).astimezone(CHI).date()
rows=list(csv.DictReader(open(os.path.join(DATA,"nashville_311_2025_raw.csv"))))
out=[]
def p(*a): s=" ".join(str(x) for x in a); out.append(s); print(s)
p("ROWS", len(rows))
for col in ["Status","Request_Type","Subrequest_Type","Request_Origin"]:
    c=collections.Counter(r[col] for r in rows)
    p(f"COUNTER {col} n_unique={len(c)}")
    for k,v in c.most_common(60): p(f"  {k!r}: {v}")
    if len(c)>60: p(f"  ... {len(c)-60} more values, total tail rows {sum(v for k,v in c.most_common()[60:])}")
# district raw values
dc=collections.Counter(r["Council_District"] for r in rows)
p("COUNTER Council_District raw", dict(sorted(dc.items(), key=lambda x: str(x[0]))))
zc=collections.Counter((r["ZIP"] or "").strip() for r in rows)
p("ZIP unique", len(zc), "blank", zc.get("",0))
p("ZIP top15", zc.most_common(15))
# id uniqueness
p("OBJECTID unique", len(set(r["OBJECTID"] for r in rows)))
p("Request__ unique", len(set(r["Request__"] for r in rows)), "blank Request__", sum(1 for r in rows if not r["Request__"]))
# dates
neg=0; closed=0; closed_before_year=0
for r in rows:
    o=ldate(r["Date_Time_Opened"]); c=ldate(r["Date_Time_Closed"])
    assert o and o.year==2025, ("opened out of window", r["OBJECTID"], o)
    if c:
        closed+=1
        if (c-o).days<0: neg+=1
p("closed rows (Date_Time_Closed present)", closed, "negative gap rows", neg)
# status x closed cross-tab
xt=collections.Counter((r["Status"], bool(r["Date_Time_Closed"])) for r in rows)
p("STATUS x HAS_CLOSED_DATE", dict(sorted(xt.items(), key=lambda x: str(x[0]))))
# midnight placeholder check: hour census of opened timestamps UTC
hc=collections.Counter(datetime.fromtimestamp(int(r["Date_Time_Opened"])/1000, tz=timezone.utc).hour for r in rows if r["Date_Time_Opened"])
p("opened UTC hour census", dict(sorted(hc.items())))
hc2=collections.Counter(datetime.fromtimestamp(int(r["Date_Time_Closed"])/1000, tz=timezone.utc).hour for r in rows if r["Date_Time_Closed"])
p("closed UTC hour census", dict(sorted(hc2.items())))
exact_midnight=sum(1 for r in rows if r["Date_Time_Opened"] and int(r["Date_Time_Opened"])%86400000==0)
p("opened exactly UTC midnight", exact_midnight)
open(os.path.join(DATA,"audit_output.txt"),"w").write("\n".join(out)+"\n")
