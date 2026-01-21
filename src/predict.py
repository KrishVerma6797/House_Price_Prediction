import pandas as pd

def predict_price(model):
    area = int(input("Enter area (sqft): "))
    bedrooms = int(input("Enter bedrooms: "))
    bathrooms = int(input("Enter bathrooms: "))
    stories = int(input("Enter stories: "))
    parking = int(input("Enter parking spaces: "))

    mainroad = input("Main road (yes/no): ")
    guestroom = input("Guest room (yes/no): ")
    basement = input("Basement (yes/no): ")
    hotwaterheating = input("Hot water heating (yes/no): ")
    airconditioning = input("Air conditioning (yes/no): ")
    prefarea = input("Preferred area (yes/no): ")
    furnishingstatus = input("Furnishing (furnished/semi-furnished/unfurnished): ")

    input_df = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "parking": parking,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus
    }])

    prediction = model.predict(input_df)
    print(f"Predicted House Price: ₹{int(prediction[0])}")
