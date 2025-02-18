print("Welcome to Python Pizza Deliveries!")
prices = {
    "S": {
        "Y":{
            "Y": 15+2+1,
            "N": 15+2,
        },
        "N":{
            "Y": 15+1,
            "N": 15,
        },
    },
    "M": {
        "Y":{
            "Y": 20+3+1,
            "N": 20+3,
        },
        "N":{
            "Y": 20+1,
            "N": 20,
        },
    },
    "L": {
        "Y": {
            "Y": 25+3+1,
            "N": 25+3,
        },
        "N": {
            "Y": 25+1,
            "N": 25,
        },
    },
}

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

print(f"Your final bill is: ${prices[size][pepperoni][extra_cheese]}.")