# import requests
# import random
# import time


# API_URL = "http://127.0.0.1:5000/predict"


# merchant_categories = {
#     "Food": 0,
#     "Travel": 1,
#     "Electronics": 2,
#     "Healthcare": 3,
#     "Luxury": 4
# }


# def generate_transaction():

#     amount = random.randint(100, 50000)

#     transaction_hour = random.randint(0, 23)

#     merchant_category = random.choice(
#         list(merchant_categories.values())
#     )

#     foreign_transaction = random.choice([0, 1])

#     location_mismatch = random.choice([0, 1])

#     device_trust_score = random.randint(1, 100)

#     velocity_last_24h = random.randint(1, 30)

#     cardholder_age = random.randint(18, 80)

#     return [
#         amount,
#         transaction_hour,
#         merchant_category,
#         foreign_transaction,
#         location_mismatch,
#         device_trust_score,
#         velocity_last_24h,
#         cardholder_age
#     ]


# while True:

#     transaction = generate_transaction()

#     response = requests.post(

#         API_URL,

#         json={
#             "features": transaction
#         }

#     )

#     result = response.json()
    


#     if "error" in result:

#         print("\nAPI ERROR")

#         print(result["error"])

#         continue



#     risk_score = result["risk_score"]

#     prediction = result["prediction"]

#     print("\nNEW TRANSACTION")

#     print("-------------------------")

#     print("Transaction:", transaction)

#     print(f"Risk Score: {risk_score:.2f}")

#     if prediction == 1:

#         if risk_score > 85:

#             print("ACTION: BLOCK TRANSACTION")

#         elif risk_score > 60:

#             print("ACTION: REQUIRE OTP")

#         else:

#             print("ACTION: FLAG FOR REVIEW")

#     else:

#         print("ACTION: APPROVE")

#     print("-------------------------")

#     time.sleep(3)



import requests
import random
import time


API_URL = "http://127.0.0.1:5000/predict"


merchant_categories = [
    "Food",
    "Travel",
    "Electronics",
    "Healthcare",
    "Luxury"
]


def generate_transaction():

    transaction = {

        "amount":
        random.randint(100, 50000),

        "transaction_hour":
        random.randint(0, 23),

        "merchant_category":
        random.choice(merchant_categories),

        "foreign_transaction":
        random.choice(["Yes", "No"]),

        "location_mismatch":
        random.choice(["Yes", "No"]),

        "device_trust_score":
        random.randint(1, 100),

        "velocity_last_24h":
        random.randint(1, 30),

        "cardholder_age":
        random.randint(18, 80)
    }

    return transaction


while True:

    transaction = generate_transaction()

    response = requests.post(

        API_URL,

        json=transaction

    )

    result = response.json()

    # Handle API errors
    if "error" in result:

        print("\nAPI ERROR")

        print(result["error"])

        continue

    risk_score = result["risk_score"]

    prediction = result["prediction"]

    print("\nNEW TRANSACTION")

    print("-------------------------")

    print(transaction)

    print(f"\nRisk Score: {risk_score:.2f}")

    if prediction == 1:

        if risk_score > 85:

            print("ACTION: BLOCK TRANSACTION")

        elif risk_score > 60:

            print("ACTION: REQUIRE OTP")

        else:

            print("ACTION: FLAG FOR REVIEW")

    else:

        print("ACTION: APPROVE")

    print("-------------------------")

    time.sleep(3)