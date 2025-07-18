# With __str__

'''

to know the content of an object we can use this instead of using the def info functiob


defines the "informal" or nicely printable string representation of an object. 
'''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - ${self.price}"

p = Product("Phone", 699)
print(p)  # Automatically uses __str__
# Also works in all these cases:
log_message = f"Processing {p}"
csv_line = str(p) + "\n"
gui_label.config(text=str(p))