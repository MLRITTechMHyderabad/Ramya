customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

eligible_customers = filter(
    lambda cust: 18 <= cust["age"] <= 40,
    customers
)
discounted_customers = map(
    lambda cust: {
        "name": cust["name"],
        "age": cust["age"],
        "total_purchase": round(
            cust["total_purchase"] * (0.90 if cust["age"] <= 25 else 0.95), 2
        )
    },
    eligible_customers
)
result = list(discounted_customers)
print(result)
