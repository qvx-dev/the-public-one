import math

def laminate_cost(length, width, plank_length, plank_width, price_per_m2):
    room_area = length * width
    total_cost = round(room_area * price_per_m2, 2)
    return total_cost

if __name__ == "__main__":
    length = float(input("Enter the length of the room (m): "))
    width = float(input("Enter the width of the room (m): "))
    plank_length = float(input("Enter the length of the laminate board (m): "))
    plank_width = float(input("Enter the width of the laminate board (m): "))
    price = float(input("Enter the price of laminate per 1 square meter (€): "))

    cost = laminate_cost(length, width, plank_length, plank_width, price)
    print(f"Laminate flooring installation costs: {cost} €")

