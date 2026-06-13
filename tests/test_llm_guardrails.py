from llm_guardrails import LLMGuardrails, Request, Guardrail, Error
import json

def test_apply_guardrails_success():
    llm_guardrails = LLMGuardrails()
    request = Request({}, 'response')
    guardrail_ids = []
    result = llm_guardrails.apply_guardrails(request, guardrail_ids)
    assert result == request

def test_apply_guardrails_block():
    llm_guardrails = LLMGuardrails()
    llm_guardrails.add_guardrail('guardrail1', 'block')
    request = Request({}, 'response')
    guardrail_ids = ['guardrail1']
    result = llm_guardrails.apply_guardrails(request, guardrail_ids)
    assert isinstance(result, Error)
    assert result.message == "Request blocked by guardrail guardrail1"
    assert result.rule_details == 'block'

def test_apply_guardrails_fallback():
    llm_guardrails = LLMGuardrails()
    llm_guardrails.add_guardrail('guardrail1', 'allow')
    request = Request({}, 'response')
    guardrail_ids = ['guardrail1', 'guardrail2']
    result = llm_guardrails.apply_guardrails(request, guardrail_ids)
    assert result == request

def test_process_request_success():
    llm_guardrails = LLMGuardrails()
    request = Request({}, 'response')
    guardrail_ids = []
    result = llm_guardrails.process_request(request, guardrail_ids)
    assert json.loads(result) == {'response': 'response'}

def test_process_request_block():
    llm_guardrails = LLMGuardrails()
    llm_guardrails.add_guardrail('guardrail1', 'block')
    request = Request({}, 'response')
    guardrail_ids = ['guardrail1']
    result = llm_guardrails.process_request(request, guardrail_ids)
    assert json.loads(result) == {'error': "Request blocked by guardrail guardrail1", 'rule_details': 'block'}
