from datetime import date, datetime
import csv
import os

def create_username(full_name: str) -> str:
    """
    Create a student username based on enrollment year, name, and surname initials.
    Format: a + last 2 digits of year + name + surname initials
    
    Args:
        full_name: Complete name (name + surnames)
        
    Returns:
        Username in lowercase
    """
    # Get current year and extract last 2 digits
    current_year = date.today().year
    year_suffix = str(current_year)[-2:]
    
    # Split the full name
    parts = full_name.lower().split()
    name = parts[0]
    
    # Get initials from surnames
    surname_initials = []
    for i in range(1, len(parts)):
        surname_initials.append(parts[i][0])
    
    # for part in parts[1:]:
    #     surname_initials.append(part[0])
    
    surname_initials = "".join(surname_initials)

    # Build username
    username = "a" + year_suffix + name + surname_initials
    return username

with open("registrations.csv") as ficheiro:
    persoas = csv.reader(ficheiro)
    for persoa in persoas:
        print(create_username(persoa[0] + " " + persoa[1]))
        
if not os.path.exists("processed"):
    os.mkdir("processed")

agora = datetime.now()
data_actual = agora.strftime("%Y%m%d_%H%M")
print(data_actual)

novo_nome = "registrations_" + data_actual + ".csv"

os.rename("registrations.csv", "processed/" + novo_nome)