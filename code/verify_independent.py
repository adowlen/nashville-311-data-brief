import json, urllib.request, urllib.parse, os
import pandas as pd
PKG=os.path.normpath(os.path.join(os.path.dirname(__file__),".."))
S=json.load(open(os.path.join(PKG,"stats.json")))
checks=[]
def chk(name, a, b): checks.append({"check":name,"package":a,"independent":b,"pass":bool(a==b)})
df=pd.read_csv(os.path.join(PKG,"data","nashville_311_2025_raw.csv"), low_memory=False)
chk("rows_2025", S["rows_2025"], len(df))
chk("type_top1_n", list(S["type_counter"].values())[0], int((df.Request_Type=="Resolved by hubNashville on First Call").sum()))
o=pd.to_datetime(df.Date_Time_Opened, unit="ms", utc=True).dt.tz_convert("America/Chicago").dt.date
c=pd.to_datetime(df.Date_Time_Closed, unit="ms", utc=True).dt.tz_convert("America/Chicago").dt.date
gap=(c-o).apply(lambda x: x.days if pd.notna(x) else None)
closed=gap.dropna()
chk("closed_n", S["closed"]["with_closed_date"], int(closed.shape[0]))
chk("same_day_n", S["closed"]["same_day_n"], int((closed==0).sum()))
chk("same_day_pct", S["closed"]["same_day_pct"], round(100*(closed==0).mean(),1))
chk("median_days", S["closed"]["median_days"], float(closed.median()))
chk("over_30d_n", S["closed"]["over_30d_n"], int((closed>30).sum()))
fc=df.Request_Type=="Resolved by hubNashville on First Call"
chk("fieldwork_same_day_pct", S["excluding_first_call"]["same_day_pct"], round(100*(gap[~fc].dropna()==0).mean(),1))
chk("fieldwork_median", S["excluding_first_call"]["median_days"], float(gap[~fc].dropna().median()))
pv=df.Request_Type=="Property Violations"
pvg=gap[pv].dropna()
chk("pv_median", S["by_type"]["Property Violations"]["median_days"], float(pvg.median()))
chk("pv_over30_pct", S["by_type"]["Property Violations"]["over_30d_pct"], round(100*(pvg>30).mean(),1))
chk("district_missing", S["district_missing"], int(df.Council_District.isna().sum()))
chk("district_19_n", S["by_district"]["19"]["n"], int((df.Council_District==19).sum()))
# live server aggregates (different path entirely)
base="https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/hubNashville_(311)_Service_Requests_1/FeatureServer/0/query"
def q(where):
    url=base+"?"+urllib.parse.urlencode({"where":where,"returnCountOnly":"true","f":"json"})
    with urllib.request.urlopen(url, timeout=30) as r: return json.load(r)["count"]
chk("live_2025_count", 248066, q("Date_Time_Opened >= TIMESTAMP '2025-01-01 06:00:00' AND Date_Time_Opened < TIMESTAMP '2026-01-01 06:00:00'"))
chk("live_full_count_matches_stats", S["full_series_rows_live_2026_11_08"], q("1=1"))
res={"pass":sum(1 for x in checks if x["pass"]), "total":len(checks), "checks":checks}
json.dump(res, open(os.path.join(PKG,"data","verify_independent_output.json"),"w"), indent=1)
print(f"PASS {res['pass']}/{res['total']}")
for x in checks:
    if not x["pass"]: print("FAIL", x)
