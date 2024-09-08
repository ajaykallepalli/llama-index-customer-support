# test_ai.py

from support_ai import SupportAI

def test_ai():
    ai = SupportAI()
    
    test_queries = [
        "How do I reset my password?",
        "What are your shipping options?",
        "Can you explain your return policy?",
        "How do I upgrade to a premium account?",
        "What should I do if I receive a damaged item?",
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        response = ai.get_response(query)
        print(f"Response: {response}")
        print("-" * 50)

if __name__ == "__main__":
    test_ai()