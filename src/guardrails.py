import json
from dataclasses import dataclass, field
from typing import List

@dataclass
class Guardrail:
    name: str
    description: str
    source: str = "template"
    fields: List[str] = field(default_factory=list)

class GuardrailLibrary:
    def __init__(self):
        self.guardrails = []

    def add_guardrail(self, guardrail):
        self.guardrails.append(guardrail)

    def import_template(self, template_name):
        templates = {
            "gdpr_pii_redaction": Guardrail("GDPR PII Redaction", "Redact personally identifiable information"),
            "profanity_filter": Guardrail("Profanity Filter", "Filter out profanity"),
            "data_retention": Guardrail("Data Retention", "Retain data for a specified period"),
            "access_control": Guardrail("Access Control", "Control access to sensitive data"),
            "encryption": Guardrail("Encryption", "Encrypt sensitive data"),
        }
        if template_name in templates:
            return templates[template_name]
        else:
            raise ValueError("Template not found")

    def list_guardrails(self):
        return self.guardrails

def main():
    library = GuardrailLibrary()
    library.add_guardrail(library.import_template("gdpr_pii_redaction"))
    library.add_guardrail(library.import_template("profanity_filter"))
    print(json.dumps([g.__dict__ for g in library.list_guardrails()], indent=4))

if __name__ == "__main__":
    main()
