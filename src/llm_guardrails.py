import json
from dataclasses import dataclass
from typing import List

@dataclass
class Guardrail:
    id: str
    rule: str

@dataclass
class Request:
    metadata: dict
    response: str

@dataclass
class Error:
    message: str
    rule_details: str

class LLMGuardrails:
    def __init__(self):
        self.guardrails = {}

    def add_guardrail(self, guardrail_id: str, rule: str):
        self.guardrails[guardrail_id] = Guardrail(guardrail_id, rule)

    def apply_guardrails(self, request: Request, guardrail_ids: List[str]):
        for guardrail_id in guardrail_ids:
            if guardrail_id in self.guardrails:
                request.metadata['guardrail_ids'] = request.metadata.get('guardrail_ids', []) + [guardrail_id]
                if self.guardrails[guardrail_id].rule == 'block':
                    return Error(f"Request blocked by guardrail {guardrail_id}", self.guardrails[guardrail_id].rule)
        return request

    def process_request(self, request: Request, guardrail_ids: List[str]):
        result = self.apply_guardrails(request, guardrail_ids)
        if isinstance(result, Error):
            return json.dumps({'error': result.message, 'rule_details': result.rule_details})
        else:
            return json.dumps({'response': result.response})
