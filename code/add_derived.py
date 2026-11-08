import csv, json, collections, statistics, os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
PKG=os.path.normpath(os.path.join(os.path.dirname(__file__),".."))
CHI=ZoneInfo("America/Chicago")
def ld(ms): return datetime.fromtimestamp(int(ms)/1000,tz=timezone.utc).astimezone(CHI).date() if ms else None
rows=list(csv.DictReader(open(os.path.join(PKG,"data","nashville_311_2025_raw.csv"))))
for r in rows: r["_gap"]=(ld(r["Date_Time_Closed"])-ld(r["Date_Time_Opened"])).days if r["Date_Time_Closed"] else None
s=json.load(open(os.path.join(PKG,"stats.json")))
def summ(grp):
    g=[r["_gap"] for r in grp if r["_gap"] is not None]
    gs=sorted(g)
    return {"opened":len(grp),"closed":len(g),"same_day_pct":round(100*sum(1 for x in g if x==0)/len(g),1) if g else None,
      "median_days":statistics.median(g) if g else None,"p90_days":gs[min(len(gs)-1,int(0.9*len(gs)))] if g else None,
      "over_30d_pct":round(100*sum(1 for x in g if x>30)/len(g),1) if g else None,"over_30d_n":sum(1 for x in g if x>30)}
fc=[r for r in rows if r["Request_Type"]=="Resolved by hubNashville on First Call"]
fw=[r for r in rows if r["Request_Type"]!="Resolved by hubNashville on First Call"]
s["first_call"]=summ(fc); s["excluding_first_call"]=summ(fw)
s["top5_types_share_pct"]=round(100*sum(list(s["type_counter"].values())[:5])/len(rows),1)
s["top5_types_n"]=sum(list(s["type_counter"].values())[:5])
s["unclosed_by_type"]=dict(collections.Counter(r["Request_Type"] for r in rows if not r["Date_Time_Closed"]).most_common())
s["district_missing_by_type"]={t:{"n":len(g),"missing":sum(1 for r in g if not r["Council_District"]),"missing_pct":round(100*sum(1 for r in g if not r["Council_District"])/len(g),1)} for t,g in ((t,[r for r in rows if r["Request_Type"]==t]) for t in s["type_counter"])}
bd=s["by_district"]
s["district_extremes"]={"same_day_min":{"district":min(bd,key=lambda d:bd[d]["same_day_pct"]),"pct":min(v["same_day_pct"] for v in bd.values())},
 "same_day_max":{"district":max(bd,key=lambda d:bd[d]["same_day_pct"]),"pct":max(v["same_day_pct"] for v in bd.values())},
 "p90_max":{"district":max(bd,key=lambda d:bd[d]["p90_days"]),"days":max(v["p90_days"] for v in bd.values())},
 "largest":{"district":max(bd,key=lambda d:bd[d]["n"]),"n":max(v["n"] for v in bd.values())}}
json.dump(s, open(os.path.join(PKG,"stats.json"),"w"), indent=1)
print(json.dumps({k:s[k] for k in ["first_call","excluding_first_call","top5_types_share_pct","district_extremes"]},indent=1))
