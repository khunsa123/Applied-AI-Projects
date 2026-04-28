from src.parser import load_tickets

def main():
    tickets = load_tickets("data/sample_tickets.json")
    print("Sample Support Tickets:")
    for t in tickets:
        print(f"- {t['id']}: {t['title']} [{t['status']}]\n  Category: {t['category']}\n  Description: {t['description']}")

if __name__ == "__main__":
    main()
