from json import load

def read_file():
    with open('loans.json', 'r') as json_file:
        data = load(json_file)
        return data

def calculate_unpaid_loans(data):
    loans = data["loans"]
    return sum(loan['amount'] for loan in loans if loan['status'] == 'unpaid')

def calculate_paid_loans(data):
    return sum(paid_loans(data))

def average_paid_loans(data):
    if len(paid_loans(data)) == 0:
        return
    return calculate_paid_loans(data) / len(paid_loans(data))

def paid_loans(data):
    loans = data["loans"]
    return [loan['amount'] for loan in loans if loan['status'] == 'paid']