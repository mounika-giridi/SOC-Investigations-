# Authentication alert triage playbook

1. **Confirm telemetry:** table, connector, ingestion delay, timestamps, time zone, account and source IP.
2. **Establish timeline:** count failures, distinct users/IPs, and successes before/after the alert.
3. **Check context:** expected user activity, approved service accounts, password resets, device identity, application, conditional access and MFA outcomes (where available).
4. **Correlate:** related endpoint/identity events, suspicious changes, new devices or applications, and any credible threat intelligence.
5. **Decide:**
   - **Escalate** if there is credible evidence of unauthorized success, account abuse, persistence, or material uncertainty with high potential impact.
   - **Close as benign** only with corroborated explanation and no contradictory evidence in available telemetry.
   - **Keep investigating** if evidence is insufficient; do not call unknown activity a false positive.
6. **Document:** evidence, timestamps, queries, uncertainty, decision, owner, and follow-up actions.
7. **Tune:** identify repetitive benign patterns; prefer narrowly scoped, time-bound exclusions; replay known malicious and benign scenarios before/after changes.

**Do not** treat a known IP as automatically safe or an unfamiliar IP as automatically malicious.
