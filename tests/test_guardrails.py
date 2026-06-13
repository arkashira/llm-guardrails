import pytest
from guardrails import Guardrail, GuardrailLibrary

def test_guardrail_library():
    library = GuardrailLibrary()
    assert len(library.list_guardrails()) == 0

def test_import_template():
    library = GuardrailLibrary()
    guardrail = library.import_template("gdpr_pii_redaction")
    assert guardrail.name == "GDPR PII Redaction"
    assert guardrail.source == "template"

def test_add_guardrail():
    library = GuardrailLibrary()
    guardrail = library.import_template("gdpr_pii_redaction")
    library.add_guardrail(guardrail)
    assert len(library.list_guardrails()) == 1

def test_list_guardrails():
    library = GuardrailLibrary()
    library.add_guardrail(library.import_template("gdpr_pii_redaction"))
    library.add_guardrail(library.import_template("profanity_filter"))
    assert len(library.list_guardrails()) == 2

def test_template_not_found():
    library = GuardrailLibrary()
    with pytest.raises(ValueError):
        library.import_template("non_existent_template")
