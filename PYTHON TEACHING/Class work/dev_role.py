


# --- Constants (ALL CAPS by convention: don't change these) ---
CARD_WIDTH = 40
COMPANY = "HackathonAfrica"
HOURS_PER_DAY = 8

# --- The raw details ---
first_name = "Ada"
last_name = "Lovelace"
role = "Backend Developer"
city = "London"
location = "United Kingdom"
experience = 5
rate = 50.0
cv_file = "ada_cv.pdf"

def print_card():
    """Print a card with the details of the person."""
    print("-" * CARD_WIDTH)
    print(f"{COMPANY:^40}")
    print("-" * CARD_WIDTH)
    print(f"Name: {first_name} {last_name}")
    print(f"Role: {role}")
    print(f"Location: {city}, {location}")
    print(f"Experience: {experience} years")
    print(f"Hourly Rate: ${rate:,.2f}")
    print(f"CV File: {cv_file}")
    print("-" * CARD_WIDTH)

print_card()