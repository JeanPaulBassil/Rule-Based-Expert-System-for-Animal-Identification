from knowledge_base import KnowledgeBase
from rules_definition import rules

def main():
    kb = KnowledgeBase(rules)
    result = kb.get('animal')
    print("Result:", result)

if __name__ == "__main__":
    main()
