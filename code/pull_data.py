import urllib.request, urllib.parse, json, csv, time, os
BASE="https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/hubNashville_(311)_Service_Requests_1/FeatureServer/0/query"
FIELDS="OBJECTID,Request__,Status,Request_Type,Subrequest_Type,Request_Origin,Council_District,ZIP,Date_Time_Opened,Date_Time_Closed"
WHERE="Date_Time_Opened >= TIMESTAMP '2025-01-01 06:00:00' AND Date_Time_Opened < TIMESTAMP '2026-01-01 06:00:00'"
out=os.path.join(os.path.dirname(__file__),"..","data","nashville_311_2025_raw.csv")
out=os.path.normpath(out)
offset=0; total=0
with open(out,"w",newline="",encoding="utf-8") as f:
    w=None
    while True:
        params={"where":WHERE,"outFields":FIELDS,"returnGeometry":"false","orderByFields":"OBJECTID","resultOffset":offset,"resultRecordCount":1000,"f":"json"}
        url=BASE+"?"+urllib.parse.urlencode(params)
        for attempt in range(5):
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    j=json.load(r)
                break
            except Exception as e:
                print("retry",offset,e); time.sleep(2)
        feats=j.get("features",[])
        if not feats: break
        for ft in feats:
            a=ft["attributes"]
            if w is None:
                w=csv.DictWriter(f, fieldnames=list(a.keys())); w.writeheader()
            w.writerow(a); total+=1
        print("pulled",total, flush=True)
        if not j.get("exceededTransferLimit"): break
        offset+=1000
print("DONE",total)
with open(os.path.join(os.path.dirname(out),"pull_log.json"),"w") as pf:
    json.dump({"where":WHERE,"fields":FIELDS,"rows":total,"source":BASE},pf,indent=2)
