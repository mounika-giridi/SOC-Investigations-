# Command Injection Attack Analysis

## Objective
Detect and analyze a command injection attack using web server access logs.

## Log Source
HTTP access logs from a simulated vulnerable web application.

## Attack Overview
The attacker attempted to execute system commands via a vulnerable parameter in a web application.

## Key Indicators
- Presence of command separators: `;`
- Commands observed: `ls`, `whoami`, `pwd`
- Repeated requests from same IP

## Findings Summary
- Attacker IP: 192.168.31.156
- Attack Start Time: 01/Mar/2022 09:03:33
- Target Parameter: `q`
- Payload Example: `q=1.1.1.1;ls`

## Analysis
Multiple requests containing command injection payloads were observed. However, response size remained consistent across requests, suggesting no visible command output.

## Conclusion
- Attack detected: Yes
- Attack successful: No (no evidence of execution output)
