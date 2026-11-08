# Nashville 311 in 2025: a third of requests end on the first call, and property violations carry the longest tail

**One-line summary:** Of the 248,066 service requests opened with hubNashville in 2025, 78,753 (31.7 percent) were recorded as resolved on the first call and every closed one of them closed the same day; among the other 161,645 closed requests, 44.0 percent closed the same day and the median wait was 1 day, while closed property-violation requests (20,564) waited a median of 6 days and 21.1 percent of them took more than 30 days.

Start with the scale. Nashville opened 248,066 hubNashville service requests in calendar 2025, about 680 a day (derived). This brief measures that year in Metro's own service-request ledger: what residents asked for, how long requests took to close, and where the ledger itself cannot answer - a third of its records carry no council district, and its request-origin field is blank on every record. It repeats the analysis form of the Denver 311 brief in this series (October 12, 2026) in the second locality.

Machine Readable pulled the 2025 population from the full-series hubNashville 311 service on November 8, 2026: 248,066 records opened between January 1 and December 31, 2025 (America/Chicago local dates), out of 2,120,937 records in the full series on the pull date. One record is one service request. A closed date in the ledger records that the request was closed in the system; this brief measures requests as recorded, not work performed in the field.

## A third of the system ends on the first call

- Five request types hold 230,871 of the 248,066 requests (93.1 percent): Resolved by hubNashville on First Call (78,753, 31.7 percent), Public Safety (52,799, 21.3 percent), Trash, Recycling & Litter (51,551, 20.8 percent), Streets, Roads & Sidewalks (25,146, 10.1 percent), and Property Violations (22,622, 9.1 percent). The remaining 12 recorded types share 17,195 requests.
- The first-call type is a resolution category, not a topic: its only subrequest type is itself (78,753 records), and 78,752 of its records carry a closed date, all of them the same day they opened (100.0 percent). The topics inside those calls are not recorded separately in this layer.
- Inside the topic types, the largest single asks are Public Safety's towing control-number requests (26,277 subrequests) and trash cart work: Cart Service (17,244), Missed Pickup - Trash Cart Service (13,564), and Missed Pickup - Recycle Cart Service (10,560). Non-emergency police assistance adds 7,880.
- Request volume by month runs from 16,057 opened in November 2025 to 23,772 in April 2025. The brief reports the counts as recorded and does not assign a cause to the seasonal pattern.

## Two closure clocks

Counted over every closed request, Nashville looks fast: 240,397 of the 248,066 requests carry a closed date, 149,842 of them (62.3 percent) closed the same day they opened, the median gap is 0 days, and 88.3 percent closed within 7 days. That citywide figure is carried by the first-call population above. On the rest of the system - the 169,313 requests opened under a topic type - the clock reads differently:

- 161,645 topic-type requests carry a closed date. Of those, 44.0 percent closed the same day, the median gap is 1 day, the 90th percentile is 17 days, and 10,131 (6.3 percent) took more than 30 days. Every one of the 10,131 over-30-day closures in the 2025 population sits in this topic-type population.
- Public Safety is the fastest of the five largest types by same-day share: 52,297 closed, 86.2 percent the same day, median 0 days, 90th percentile 1 day. (Two smaller types post higher same-day shares on much smaller bases: Other Metro Services and Forms at 93.0 percent of 4,137 closed, and Transit at 72.6 percent of 1,281 closed.)
- Trash, Recycling & Litter: 51,498 closed, 13.9 percent the same day, median 3 days, 90th percentile 14 days.
- Streets, Roads & Sidewalks: 24,833 closed, 32.1 percent the same day, median 1 day, 90th percentile 23 days, 2,034 (8.2 percent) over 30 days.

## The slow lane: property violations

Property Violations is the fifth-largest type, and among types with at least 1,000 closed requests it carries the highest share of closures taking more than 30 days.

- 22,622 requests opened in 2025; 20,564 carry a closed date. Their median gap is 6 days, the 90th percentile is 64 days, and 4,343 of them (21.1 percent) took more than 30 days to close - about one in five (derived). One other type with at least 1,000 closed requests carries a higher median on a much smaller base: Parks and Environment (1,528 closed), at a median of 7 days, a 90th percentile of 66 days, and a lower over-30-day share of 19.2 percent.
- A further 2,058 property-violation requests (9.1 percent of the type) carry no closed date on the November 8, 2026 snapshot - the largest unclosed count of any topic type except the "Public_Works_WO" spelling variant (2,591 unclosed of its 2,686 records, covered in the recording-gaps section below). Requests opened late in 2025 have had less time to close than requests opened early in the year, so the unclosed count is printed as a snapshot count, not a completion rate.
- One smaller lane is slower still on its closed records: Electric & Water General (1,968 opened, 950 closed) carries a median gap of 9.5 days and 37.6 percent of its closed requests over 30 days, and 1,018 of its requests carry no closed date. Its counts are smaller than the property-violation lane's, and both figures are printed with their populations.

## Districts: the differences are in the tail, and a third of records have no district

Council district is recorded on 168,640 of the 248,066 requests (68.0 percent). The missing third is not spread evenly, and the pattern matters for every district figure below: 68,610 of the 78,753 first-call records (87.1 percent) carry no district, while the large topic types are nearly complete (Trash, Recycling & Litter missing 0.4 percent, Streets, Roads & Sidewalks 1.0 percent, Property Violations 1.4 percent, Public Safety 17.7 percent). District figures in this brief therefore describe the district-recorded population, which is mostly the topic-type system.

- All 35 council districts appear. District 19 (downtown) holds the most district-recorded requests, 14,068 (8.3 percent); the median district holds 4,149.
- Median closure time barely varies by district: every district's median is 0, 1, or 2 days. The variation sits in the tail and the same-day share. Same-day closure runs from 25.7 percent in District 24 (6,674 closed) to 67.9 percent in District 10 (1,659 closed). The highest district 90th percentile is District 21 at 36 days (5,666 closed).
- ZIP code shows the same completeness pattern as district (blank on 79,642 records, 32.1 percent). Among ZIP-recorded requests, 37013 holds the most at 17,540, then 37211 at 15,589 and 37203 at 14,537.
- No exposure denominator is published with this layer (the layer carries no population, household, or parcel base by district), so this brief reports district counts, shares of the district-recorded population, and closure timing - not per-capita request rates - and draws no conclusion about which district "uses" 311 most.

## What the ledger does not record

Three recording gaps bound what this dataset can answer, and each is stated here rather than worked around:

- **Request origin is blank on all 248,066 records.** The layer carries a Request_Origin field; in the 2025 population it is empty on every record, so channel questions (phone vs web vs app) cannot be answered from the public data.
- **Two spellings split one work-order family.** The type field records both "Public Works WO" (4,069 requests, 3,407 closed) and "Public_Works_WO" (2,686 requests, 95 closed). As recorded, the underscore spelling's requests almost never carry a closed date (2,591 of its 2,686 records, and 2,591 of the 7,669 unclosed records in the whole population). The brief reports the two spellings as recorded and does not merge them; whether they are one population in Metro's source system is a question the public layer does not answer.
- **Type labels are as recorded.** The 17 type values include near-duplicate pairs beyond the work-order family ("Parks" at 150 requests beside "Parks and Environment" at 1,760; "Planning and Zoning" at 63 beside "Planning & Zoning" at 13). All type figures use the recorded strings.

## The full-series context

The full series on the pull date holds 2,120,937 records. Opened counts by Chicago calendar year, counted server-side, are: 30,196 in 2017, 82,991 in 2018, 155,426 in 2019, 239,784 in 2020, 317,027 in 2021, 260,797 in 2022, 272,959 in 2023, 277,019 in 2024, 248,066 in 2025, and 236,672 in 2026 through the pull date. The yearly counts sum exactly to the full-series total, which is the pull's internal control. The brief does not interpret the year-to-year movement: the series' early years coincide with the hubNashville system's own ramp-up, and the layer publishes no definition history that would let a reader separate changed recording from changed demand.

For series context only: the Denver 311 brief in this series reported 84 percent of its cases closing the same day, counted over all Denver cases in its three-year population, a basis that does not separate first-contact resolutions into their own type the way Nashville's ledger does. The two same-day figures are printed on their own bases and are not a like-for-like comparison.

## What this might mean

One possible reading is that hubNashville operates as two systems sharing one ledger: a high-volume contact system that ends most of what it touches on the first call or the same day (the first-call type at 100.0 percent same-day, Public Safety at 86.2 percent), and a field-work system whose waits concentrate in a few lanes, with property violations the largest of the slow lanes by volume and by over-30-day share (22,622 opened; median 6 days; 21.1 percent of closed requests over 30 days). On that reading, a single citywide closure average describes neither system. The strongest alternative explanation is that the type field mixes unlike things by design: a resolution category (first call) sits in the same field as topic categories, and property-violation cases may remain open in the system while inspections, notices, and compliance steps proceed elsewhere, so a long recorded gap can measure case workflow rather than waiting time for a resident-visible result. The data in this layer cannot separate those two readings, because the layer carries no milestone or outcome field between opened and closed.

## Who can act

- **hubNashville / Metro Information Technology Services (ledger completeness).** The lever is the public layer's own fields: recording a council district (or a stated reason it is not recorded) on first-call resolutions, and populating Request_Origin, would make district and channel questions answerable. Cost class: low-cost operational change. Outcome measure: the district-recorded share and the origin-populated share of opened requests in a future snapshot of this same service, against the 68.0 percent and 0 percent recorded here.
- **Metro Department of Codes Administration (property-violation lane).** The lever is the case workflow behind the lane with the highest over-30-day share at scale: publishing the milestone steps inside a property-violation request (inspection, notice, compliance, closure), or a type-level median and 90th-percentile closure table, would show whether the 6-day median and the 21.1 percent over-30-day share move, and where inside the case they sit. Cost class: low-cost operational change. Outcome measure: the property-violation median gap and over-30-day share in this service on a future snapshot, computed the same way as the type panel in this brief's data folder.
- **Metro Council (service reporting ahead of its November 17, 2026 meeting).** The lever is a standing type-level report rather than a single citywide average: the two-clock split in this brief (first-call resolutions separated from topic types) is computable from the public layer today. Cost class: low-cost operational change. Outcome measure: a published council or hubNashville report that states closure timing by request type on the separated basis, checkable against this brief's type panel.

## Methods in brief

Snapshot of the hubNashville 311 full-series service on November 8, 2026, filtered server-side to requests opened in calendar 2025 (America/Chicago); the pull's 248,066 rows match the server's own count for the same window exactly. All date arithmetic uses America/Chicago local dates. Closure gaps are computed only over records carrying a closed date (240,397); no record carries a closed date before its opened date. Status and closed-date agree closely but not exactly: 240,390 records carry the status "Closed," and the 7 additional dated records carry the statuses Accept (2), Canceled (2), and Regret (3) as recorded. The layer's public metadata describes each field but does not define its status values, so statuses are reported as recorded. The pre-flight audit, the join and missingness record, and the independent verification are documented in verification.md.

Data, code, charts, and the full audit: https://github.com/adowlen/nashville-311-data-brief

*Machine Readable is a public-good civic data project. Figures are drawn from the sources in the repository's sources.md; corrections are welcome and will be recorded in the repository.*
