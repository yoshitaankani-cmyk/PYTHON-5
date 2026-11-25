          
n = int(input("Enter number of transactions: "))

ids = []
amounts = []

for i in range(n):
    transaction_id = input("Enter transaction ID: ")
    amount = float(input("Enter transaction amount: "))

    ids.append(transaction_id)
    amounts.append(amount)

print("\n----- TRANSACTION REPORT -----")

for i in range(n):
    count = 0

    for j in range(n):
        if ids[i] == ids[j]:
            count = count + 1

    if count > 1:
        if ids[i] not in ids[:i]:
            print("Duplicate transaction ID:", ids[i])

    if amounts[i] > 10000:
        print("High value transaction:", ids[i], amounts[i])

print("Transaction checking completed")
