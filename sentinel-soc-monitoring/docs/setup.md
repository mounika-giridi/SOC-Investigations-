# Setup checklist

1. Create/select a Log Analytics workspace and enable Microsoft Sentinel.
2. In Sentinel **Content management / Data connectors**, locate the Microsoft Entra ID connector and configure sign-in log collection. Check current Azure prerequisites and licensing in your tenant.
3. Optionally ingest Windows Security Events through Azure Monitor Agent (AMA) and a data collection rule.
4. In **Logs**, check `SigninLogs | take 5` and `SecurityEvent | take 5`. Missing tables mean the corresponding query cannot run yet.
5. Use a limited test account and approved lab activity; never generate authentication attacks against systems without permission.
6. Run each detection as a query before enabling an analytics rule. Validate field names, data freshness, volumes, and noise.
7. Set alert thresholds and exclusion policies only after observing your environment.

**Cost:** Azure log ingestion, retention and Sentinel services may incur charges. Review pricing and set budget alerts before enabling ingestion.
