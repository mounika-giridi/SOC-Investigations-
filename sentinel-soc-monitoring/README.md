# Microsoft Sentinel SOC Monitoring Lab

A Microsoft Sentinel security monitoring lab focused on authentication detections, KQL threat hunting, alert triage, and investigation documentation.

> **Project status:** Lab implementation with synthetic test events. Live Sentinel validation, production deployment, and detection performance measurements are not included.

## What it does

- Detects bursts of failed Microsoft Entra ID sign-ins by user and IP.
- Hunts for a successful sign-in after repeated failures from the same user/IP.
- Detects Windows failed logon bursts using `SecurityEvent` when that connector is configured.
- Provides a repeatable analyst triage and rule-tuning process.
- Includes local fixture checks (Python standard library only).

## Architecture

```text
Entra ID Sign-in Logs ──> Log Analytics / Sentinel ──> KQL analytics ──> Incident triage
Windows Security Events ─┘                                  │
                                                            └──> Investigation notes + tuning feedback
```

## Prerequisites

1. An Azure subscription with a Log Analytics workspace and Microsoft Sentinel enabled (charges may apply).
2. Microsoft Entra ID sign-in log ingestion for the `SigninLogs` rules.
3. Optional: Windows Security Events connector/AMA for the `SecurityEvent` rule.
4. Appropriate access to view logs and create analytics rules.

**Schema check:** In **Logs**, run `SigninLogs | take 5` and `SecurityEvent | take 5` separately. If a table is missing, configure its data connector before proceeding. `SigninLogs` data is not the same as Windows event 4625.

## Quick start

1. Review `docs/setup.md` and enable the appropriate connectors.
2. Open **Microsoft Sentinel > Logs** and paste a query from `detections/`.
3. Set a suitable time range (e.g., last 24 hours). Queries use explicit time filters.
4. Confirm expected rows and tune thresholds using known benign activity and approved test accounts.
5. Create a **Scheduled query** analytics rule using the query. See `docs/rule-deployment.md` for scheduling, grouping and entity-mapping guidance.
6. Investigate results using `docs/triage-playbook.md` and record decisions with `docs/incident-template.md`.
7. Run `python3 -m unittest discover -s tests -v` locally to validate the synthetic reference cases.

## Detection catalog

| File | Data source | Purpose | Caveat |
|---|---|---|---|
| `detections/entra_failed_signin_burst.kql` | `SigninLogs` | Many failed sign-ins for one user/IP | Password retries and stale credentials can look similar |
| `detections/entra_success_after_failures.kql` | `SigninLogs` | Success after repeated failures | Not proof of account compromise |
| `detections/windows_failed_logon_burst.kql` | `SecurityEvent` | Burst of Windows 4625 failures | Requires Windows Security Events ingestion |
| `hunting/entra_account_timeline.kql` | `SigninLogs` | Investigate sign-in context | Edit placeholder UPN before running |

## Limitations and safety

- These are **starting-point detections**, not validated production-ready rules.
- A successful sign-in after failures is a signal for investigation, not a confirmed compromise.
- Source IPs may be shared (NAT, VPN, proxies); geographic and reputation signals can be misleading.
- Service accounts, automation, time synchronization, log ingestion latency and connector coverage affect results.
- Avoid permanent broad allowlists. Record the reason, owner and expiry for narrowly scoped exclusions.
- Sample data is fabricated. No real credentials, tokens, personal records, or production logs are committed.
- Analytics-rule configuration and incident automation are intentionally manual; nothing in this repo automatically blocks users.

## Repository structure

```text
detections/     KQL detection queries
hunting/        Investigation query
docs/           Setup, triage, deployment, and incident notes
sample-data/    Synthetic authentication events
tests/          Offline logic checks for reference scenarios
.github/        CI for local tests
```

## License

MIT. See `LICENSE`.
