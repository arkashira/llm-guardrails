from llm_guardrails import LLMGuardrails, Request
import pytest

def test_apply_guardrails_success():
    llm_guardrails = LLMGuardrails()
    llm_guardrails.add_guardrail('guardrail1', 'rule1')
    request = Request({}, 'response')
    result = llm_guardrails.apply_guardrails(request, ['guardrail1'])
    assert result.metadata == {'guardrail_id': 'guardrail1'}

def test_apply_guardrails_block():
    llm_guardrails = LLMGuardrails()
    llm_guardrails.add_guardrail('guardrail1', 'response')
    request = Request({}, 'response')
    with pytest.raises(Exception) as e:
        llm_guardrails.apply_guardrails(request, ['guardrail1'])
    assert str(e.value) == "Guardrail guardrail1 blocked the response: response"

def test_apply_guardrails_fallback():
    llm_guardrails = LLMGuardrails()
    llm_guardrails.add_guardrail('guardrail1', 'rule1')
    request = Request({}, 'response')
    result = llm_guardrails.apply_guardrails(request, ['guardrail1', 'guardrail2'])
    assert result.metadata == {'guardrail_id': 'guardrail1'}
