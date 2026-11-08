# Sources

## Primary source for every figure in this brief

1. **hubNashville 311 Service Requests (full-series service hubNashville_(311)_Service_Requests_1), Metropolitan Government of Nashville and Davidson County via hubNashville open data (Nashville Open Data Portal).** ArcGIS FeatureServer layer 0, services2.arcgis.com/HdTo6HJqh92wn4D8. Snapshot pulled November 8, 2026: the full series held 2,120,937 records on the pull date; the analysis population is the 248,066 records opened in calendar 2025 (America/Chicago local dates), pulled with a server-side date filter whose returned row count matches the server's own count for the same window exactly. Layer metadata archived in this package at data/source-metadata-layer.json; the layer's data was last edited November 7, 2026 per the service listing.
   - Service: https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/hubNashville_(311)_Service_Requests_1/FeatureServer
   - Fields used (public names): Request #, Status, Request_Type, Subrequest_Type, Request_Origin, Council_District, ZIP, Date_Time_Opened, Date_Time_Closed. The layer's field descriptions are carried in its public metadata; the metadata does not define its Status values, and Request_Origin is blank on every record in the 2025 population.
   - Yearly opened counts (2017-2026) were counted server-side with the same Chicago calendar-year boundaries; they sum exactly to the full-series total (internal control, recorded in verification.md).

## Comparison source (companion Machine Readable brief)

2. **Denver 311 (Machine Readable, published October 12, 2026)** - 1.38 million cases over its three-year population, 84 percent closing the same day on its all-cases basis. Cited once, for series context only, with its basis printed in the brief; the two same-day figures are not a like-for-like comparison. Repository: https://github.com/adowlen/denver-311-data-brief.

## Repository and license

Full code, charts, panels, and verification notes: https://github.com/adowlen/nashville-311-data-brief
Brief text and data products: CC BY 4.0 (LICENSE in the package). The underlying records are published by Metro Nashville as government open data.
