import datetime
import pytest
from guardrails import Guardrails, Violation

def test_export_violations_csv():
    guardrails = Guardrails('org_scope')
    violation = Violation(datetime.datetime(2022, 1, 1), 'req_id', 'rule_id', 'action_taken')
    guardrails.add_violation(violation)

    csv_data = guardrails.export_violations()
    assert csv_data == 'timestamp,request_id,rule_id,action_taken\n2022-01-01 00:00:00,req_id,rule_id,action_taken\n'

def test_export_violations_invalid_format():
    guardrails = Guardrails('org_scope')
    with pytest.raises(ValueError):
        guardrails.export_violations('json')

def test_filter_violations():
    guardrails = Guardrails('org_scope')
    violation1 = Violation(datetime.datetime(2022, 1, 1), 'req_id1', 'rule_id1', 'action_taken1')
    violation2 = Violation(datetime.datetime(2022, 1, 15), 'req_id2', 'rule_id2', 'action_taken2')
    violation3 = Violation(datetime.datetime(2022, 2, 1), 'req_id3', 'rule_id3', 'action_taken3')
    guardrails.add_violation(violation1)
    guardrails.add_violation(violation2)
    guardrails.add_violation(violation3)

    start_date = datetime.datetime(2022, 1, 1)
    end_date = datetime.datetime(2022, 1, 31)
    filtered_violations = guardrails.filter_violations(start_date, end_date)
    assert len(filtered_violations) == 2
    assert filtered_violations[0].request_id == 'req_id1'
    assert filtered_violations[1].request_id == 'req_id2'
