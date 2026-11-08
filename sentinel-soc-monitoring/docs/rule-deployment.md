# Deploying scheduled analytics rules

1. Run and validate the KQL in Sentinel Logs against your connected data.
2. Go to **Analytics** and create a **Scheduled query rule** (menu names may change).
3. Paste the query and set the query frequency/lookback consistently. For the 15-minute burst query, consider a 15-minute frequency with a lookback of at least 15 minutes; account for ingestion delays and duplicate windows.
4. Trigger on result count greater than zero. Choose severity based on environment and contextual evidence, not the query name alone.
5. Map entities where the wizard supports them: `UserPrincipalName` as account and `IPAddress` as IP; Windows rules can additionally map `Computer` as host.
6. Decide whether to group results into one incident or separate incidents per account; avoid uncontrolled incident floods.
7. Test in a lab, inspect generated alerts, and document changes before promoting to production.

**Important:** Queries containing `ago()` run relative to execution time. Scheduled rules may evaluate overlapping time windows; deduplication and suppression need explicit design. No automatic containment is included.
