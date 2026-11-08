import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
PKG=os.path.normpath(os.path.join(os.path.dirname(__file__),".."))
S=json.load(open(os.path.join(PKG,"stats.json")))
CHAR="#232323"; AMBER="#e8a33d"; TEAL="#2a9d8f"; LIGHT="#f2f2f2"
plt.rcParams.update({"text.color":LIGHT,"axes.edgecolor":LIGHT,"axes.labelcolor":LIGHT,"xtick.color":LIGHT,"ytick.color":LIGHT,"figure.facecolor":CHAR,"axes.facecolor":CHAR,"savefig.facecolor":CHAR})
def save(fig,name): fig.tight_layout(); fig.savefig(os.path.join(PKG,"charts",name),dpi=200); plt.close(fig)
# 1 top types
items=list(S["type_counter"].items())[:10][::-1]
fig,ax=plt.subplots(figsize=(8,4.6))
ax.barh([k for k,_ in items],[v for _,v in items],color=TEAL)
for i,(_,v) in enumerate(items): ax.text(v+2500,i,f"{v:,}",va="center",fontsize=9)
ax.set_xlabel("Requests opened in 2025"); ax.set_title("Nashville 311 in 2025 - requests by type (top 10 of all recorded types)")
save(fig,"chart_types_top10.png")
# 2 median days by type (types with >=1000 closed nonneg)
bt={k:v for k,v in S["by_type"].items() if v["closed_nonneg"]>=1000}
items=sorted(bt.items(), key=lambda x: (x[1]["median_days"] if x[1]["median_days"] is not None else -1))[-10:]
fig,ax=plt.subplots(figsize=(8,4.6))
ax.barh([k for k,_ in items],[v["median_days"] for _,v in items],color=AMBER)
for i,(_,v) in enumerate(items): ax.text(v["median_days"]+0.4,i,f"{v['median_days']}",va="center",fontsize=9)
ax.set_xlabel("Median days from opened to closed (Chicago local dates, closed requests only)")
ax.set_title("Closure time differs by request type - median days (types with 1,000+ closed requests)"); ax.set_xlim(0,8.2)
save(fig,"chart_median_by_type.png")
# 3 same-day share by type >=1000
_srt=sorted(bt.items(), key=lambda x: x[1]["same_day_pct"])
items=sorted(_srt[:5]+_srt[-5:], key=lambda x: x[1]["same_day_pct"])
fig,ax=plt.subplots(figsize=(8,4.6))
ax.barh([k for k,_ in items],[v["same_day_pct"] for _,v in items],color=TEAL)
for i,(_,v) in enumerate(items): ax.text(v["same_day_pct"]+1,i,f"{v['same_day_pct']}%",va="center",fontsize=9)
ax.set_xlabel("Share closed the same day they opened (%)"); ax.set_title("Same-day closure share by request type (types with 1,000+ closed requests)")
save(fig,"chart_sameday_by_type.png")
# 4 districts median
bd={k:v for k,v in S["by_district"].items() if v["closed_nonneg"]>=500}
items=sorted(bd.items(), key=lambda x: x[1]["median_days"])[-10:]
fig,ax=plt.subplots(figsize=(8,4.6))
ax.barh([f"District {k}" for k,_ in items],[v["median_days"] for _,v in items],color=AMBER)
for i,(_,v) in enumerate(items): ax.text(v["median_days"]+0.4,i,f"{v['median_days']}  (n={v['n']:,})",va="center",fontsize=8)
ax.set_xlabel("Median days opened to closed"); ax.set_title("Slowest council districts by median closure time (districts with 500+ closed requests)")
save(fig,"chart_districts_median.png")
print("charts done")
