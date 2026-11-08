"""Offline reference logic checks. These do NOT execute KQL or validate Sentinel behavior."""
import csv
import unittest
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / 'sample-data' / 'auth_events.csv'


def load_events():
    with DATA.open(newline='', encoding='utf-8') as handle:
        events = list(csv.DictReader(handle))
    for event in events:
        event['dt'] = datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
    return events


def successes_after_failures(events, min_failures=5, window_minutes=30):
    findings = []
    for event in events:
        if event['result'] != 'success':
            continue
        failures = [other for other in events
                    if other['result'] == 'failure'
                    and other['user'] == event['user']
                    and other['ip'] == event['ip']
                    and event['dt'] - timedelta(minutes=window_minutes) <= other['dt'] < event['dt']]
        if len(failures) >= min_failures:
            findings.append((event['user'], event['ip'], len(failures)))
    return findings


class DetectionScenarioTests(unittest.TestCase):
    def test_flags_attack_like_pattern(self):
        self.assertIn(('bob@example.test', '198.51.100.20', 5), successes_after_failures(load_events()))

    def test_does_not_flag_short_benign_retry(self):
        self.assertNotIn('alice@example.test', [x[0] for x in successes_after_failures(load_events())])

    def test_excludes_failures_outside_window(self):
        events = load_events()
        bob_success = next(x for x in events if x['user'] == 'bob@example.test' and x['result'] == 'success')
        for event in events:
            if event['user'] == 'bob@example.test' and event['result'] == 'failure':
                event['dt'] = bob_success['dt'] - timedelta(minutes=31)
        self.assertEqual(successes_after_failures(events), [])


if __name__ == '__main__':
    unittest.main()
