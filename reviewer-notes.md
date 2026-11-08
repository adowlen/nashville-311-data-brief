# Reviewer notes - Nashville 311 Service Requests brief (2026-11-08)

## Thesis recorded before analysis (Standards Section 13.1)
"Nashville's 311 system in 2025 was dominated by a small set of request types, most requests closed quickly, but closure time varied sharply by request type and council district, so the citywide picture hides type and district lanes that wait much longer."

## Thesis revision (after the audit, before drafting; full record in verification.md)
The district clause failed in its strong form (district medians span only 0 to 2 days). Revised thesis: two clocks sharing one ledger - a third of requests resolved on the first call and closed the same day; the topic-type system at 44.0 percent same-day and a median of 1 day, with waits concentrating in a few lanes (property violations: median 6 days, 21.1 percent of closed requests over 30 days); district differences sit in the tail; a third of the ledger carries no district at all. The published brief matches the revised thesis, and the cold reader returned it in substance (gate PASS, verification.md).

## Claims most likely to be challenged
- The 62.3 percent citywide same-day figure vs the 44.0 percent excluding-first-call figure: both are printed with their populations wherever either appears, and the brief's spine leads with the split rather than the blended figure.
- "Closed" measures system closure, not field work: stated in the opening and in Methods in brief.
- Property violations as the headline slow lane: the basis is printed (highest over-30-day share among types with at least 1,000 closed requests); Parks and Environment's higher median (7 days, 1,528 closed) and Electric & Water General's higher over-30-day share (37.6 percent, 950 closed) are both disclosed in the same section.
- District figures rest on the 68.0 percent district-recorded population; the systematic missingness (87.1 percent of first-call records) is printed in the district section itself.
- The Denver 84 percent same-day contrast is printed with both bases and an explicit not-like-for-like note.

## Checks that could not be completed
- Channel analysis (phone vs web vs app): impossible from the public layer - Request_Origin is blank on all 248,066 records. Recorded as a finding and a Who-can-act item instead.
- Per-capita district rates: the layer carries no district exposure denominator, so no rate is published (stated in the brief).
- Definition history for the type/status vocabularies: the layer publishes field descriptions but no change history, so year-to-year series movement is reported as counts only, not interpreted.

## Findings that surprised us
- Request_Origin blank on every one of 248,066 records in a flagship open dataset.
- The "Public_Works_WO" spelling variant (2,686 records) almost never carries a closed date (95 closed), and it alone accounts for 2,591 of the 7,669 unclosed records in the whole 2025 population.
- District medians are nearly flat (0 to 2 days across all 35 districts) while same-day shares run from 25.7 to 67.9 percent - the district story is entirely in the distribution, not the center.

## Agency flag (Section 11.3)
The brief's findings describe hubNashville / Metro ITS recording practices (blank origin field, district missingness, spelling variants) and the Metro Codes property-violation lane. No named official is criticized; all statements are counts from the public layer with populations printed. Not a hold in the builder's judgment; flagged here for extra care per the standards.
