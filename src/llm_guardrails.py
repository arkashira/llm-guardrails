from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Guardrail:
    id: str
    rule: str

@dataclass
class Request:
    metadata: Dict[str, str]
    response: str

class LLMGuardrails:
    def __init__(self):
        self.guardrails = {}

    def add_guardrail(self, guardrail_id: str, rule: str):
        self.guardrails[guardrail_id] = Guardrail(guardrail_id, rule)

    def apply_guardrails(self, request: Request, guardrail_ids: List[str]):
        for guardrail_id in guardrail_ids:
            if guardrail_id in self.guardrails:
                guardrail = self.guardrails[guardrail_id]
                if self._check_rule(guardrail.rule, request.response):
                    request.metadata['guardrail_id'] = guardrail_id
                else:
                    raise Exception(f"Guardrail {guardrail_id} blocked the response: {guardrail.rule}")
        return request

    def _check_rule(self, rule: str, response: str):
        # For simplicity, let's assume the rule is a substring of the response
        return rule not in response

    def get_error(self, guardrail_id: str, rule: str):
        return {
            'error': 'Guardrail blocked the response',
            'guardrail_id': guardrail_id,
            'rule': rule
        }
