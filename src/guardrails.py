import csv
import dataclasses
import datetime
from typing import List

@dataclasses.dataclass
class Violation:
    timestamp: datetime.datetime
    request_id: str
    rule_id: str
    action_taken: str

class Guardrails:
    def __init__(self, organization_scope: str):
        self.organization_scope = organization_scope
        self.violations = []

    def add_violation(self, violation: Violation):
        self.violations.append(violation)

    def export_violations(self, format: str = 'csv') -> str:
        if format != 'csv':
            raise ValueError('Only CSV format is supported')

        csv_data = 'timestamp,request_id,rule_id,action_taken\n'
        for violation in self.violations:
            csv_data += f'{violation.timestamp},{violation.request_id},{violation.rule_id},{violation.action_taken}\n'

        return csv_data

    def filter_violations(self, start_date: datetime.datetime, end_date: datetime.datetime) -> List[Violation]:
        return [v for v in self.violations if start_date <= v.timestamp <= end_date]
