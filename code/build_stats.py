import csv, json, collections, statistics, os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
HERE=os.path.dirname(__file__); PKG=os.path.normpath(os.path.join(HERE,"..")); DATA=os.path.join(PKG,"data")
CHI=ZoneInfo("America/Chicago")
def ldate(ms):
    if ms in (None,""): return None
    return datetime.fromtimestamp(int(ms)/1000, tz=timezone.utc).astimezone(CHI).date()
def pct(a,b): return round(100*a/b,1) if b else None
rows=list(csv.DictReader(open(os.path.join(DATA,"nashville_311_2025_raw.csv"))))
for r in rows:
    r["_o"]=ldate(r["Date_Time_Opened"]); r["_c"]=ldate(r["Date_Time_Closed"])
    r["_gap"]=(r["_c"]-r["_o"]).days if r["_c"] else None
    try: r["_dist"]=int(float(r["Council_District"])) if r["Council_District"] not in (None,"") else None
    except: r["_dist"]=None
N=len(rows)
closed=[r for r in rows if r["_gap"] is not None]
nonneg=[r for r in closed if r["_gap"]>=0]
neg=[r for r in closed if r["_gap"]<0]
def med(xs): return statistics.median(xs) if xs else None
def p90(xs):
    if not xs: return None
    xs=sorted(xs); import math; return xs[min(len(xs)-1, math.ceil(0.9*len(xs))-1)]
gaps=[r["_gap"] for r in nonneg]
stats={}
stats["dataset"]="hubNashville 311 Service Requests (hubNashville_(311)_Service_Requests_1, layer 0), full-series service; analysis population = requests opened in calendar 2025 (America/Chicago)"
stats["snapshot_date"]="2026-11-08"; stats["rows_2025"]=N
stats["full_series_rows_live_2026_11_08"]=2120937
stats["yearly_opened_counts_chicago"]={"2017":30196,"2018":82991,"2019":155426,"2020":239784,"2021":317027,"2022":260797,"2023":272959,"2024":277019,"2025":248066,"2026_partial_to_snapshot":236672}
stats["status_counter"]=dict(collections.Counter(r["Status"] for r in rows).most_common())
stats["type_counter"]=dict(collections.Counter(r["Request_Type"] for r in rows).most_common())
stats["origin_counter"]=dict(collections.Counter(r["Request_Origin"] for r in rows).most_common())
stats["closed"]={"with_closed_date":len(closed),"without_closed_date":N-len(closed),"negative_gap":len(neg),"nonneg":len(nonneg),
 "same_day_n":sum(1 for g in gaps if g==0),"same_day_pct":pct(sum(1 for g in gaps if g==0),len(gaps)),
 "median_days":med(gaps),"p90_days":p90(gaps),"max_days":max(gaps) if gaps else None,
 "within_1d_pct":pct(sum(1 for g in gaps if g<=1),len(gaps)),"within_7d_pct":pct(sum(1 for g in gaps if g<=7),len(gaps)),
 "over_30d_n":sum(1 for g in gaps if g>30),"over_30d_pct":pct(sum(1 for g in gaps if g>30),len(gaps)),
 "over_90d_n":sum(1 for g in gaps if g>90)}
stats["per_day_2025"]=round(N/365,1)
# by type
byt={}
for t,grp in sorted(collections.defaultdict(list, { }).items()): pass
groups=collections.defaultdict(list)
for r in rows: groups[r["Request_Type"]].append(r)
for t,grp in groups.items():
    gg=[r["_gap"] for r in grp if r["_gap"] is not None and r["_gap"]>=0]
    byt[t]={"n":len(grp),"share_pct":pct(len(grp),N),"closed_nonneg":len(gg),
      "same_day_pct":pct(sum(1 for g in gg if g==0),len(gg)),"median_days":med(gg),"p90_days":p90(gg),
      "over_30d_pct":pct(sum(1 for g in gg if g>30),len(gg))}
stats["by_type"]=byt
# subrequest top 25
stats["subrequest_top25"]=dict(collections.Counter(r["Subrequest_Type"] for r in rows).most_common(25))
# by district
gd=collections.defaultdict(list)
for r in rows:
    if r["_dist"] is not None: gd[r["_dist"]].append(r)
byd={}
for d,grp in sorted(gd.items()):
    gg=[r["_gap"] for r in grp if r["_gap"] is not None and r["_gap"]>=0]
    byd[str(d)]={"n":len(grp),"share_pct":pct(len(grp),sum(len(v) for v in gd.values())),"closed_nonneg":len(gg),
      "same_day_pct":pct(sum(1 for g in gg if g==0),len(gg)),"median_days":med(gg),"p90_days":p90(gg)}
stats["by_district"]=byd
stats["district_missing"]=N-sum(len(v) for v in gd.values())
stats["district_count"]=len(gd)
dcounts=sorted(len(v) for v in gd.values())
stats["district_median_count"]=med(dcounts)
# by origin timing
go=collections.defaultdict(list)
for r in rows: go[r["Request_Origin"]].append(r)
stats["by_origin"]={o:{"n":len(g),"median_days":med([r["_gap"] for r in g if r["_gap"] is not None and r["_gap"]>=0]),"same_day_pct":pct(sum(1 for r in g if r["_gap"]==0),len([r for r in g if r["_gap"] is not None and r["_gap"]>=0]))} for o,g in go.items()}
# monthly
stats["monthly_2025"]=dict(sorted(collections.Counter(r["_o"].strftime("%Y-%m") for r in rows).items()))
# zip
zc=collections.Counter((r["ZIP"] or "").strip() for r in rows)
stats["zip_top10"]=dict(zc.most_common(10)); stats["zip_blank"]=zc.get("",0)
json.dump(stats, open(os.path.join(PKG,"stats.json"),"w"), indent=1)
# panels
with open(os.path.join(DATA,"type_panel.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["request_type","n","share_pct","closed_nonneg","same_day_pct","median_days","p90_days","over_30d_pct"])
    for t,v in sorted(byt.items(), key=lambda x:-x[1]["n"]): w.writerow([t,v["n"],v["share_pct"],v["closed_nonneg"],v["same_day_pct"],v["median_days"],v["p90_days"],v["over_30d_pct"]])
with open(os.path.join(DATA,"district_panel.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["district","n","share_pct","closed_nonneg","same_day_pct","median_days","p90_days"])
    for d,v in byd.items(): w.writerow([d,v["n"],v["share_pct"],v["closed_nonneg"],v["same_day_pct"],v["median_days"],v["p90_days"]])
print(json.dumps({k:stats[k] for k in ["rows_2025","closed","per_day_2025","district_count","district_missing"]},indent=1))
print("types:", list(stats["type_counter"].items())[:12])
