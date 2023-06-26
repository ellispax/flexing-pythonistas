#This is a simple project that will use a csv file
# read contents of the file 
#edit some contents 


import csv

def read_budget_file():
  """Reads the budget file and returns a list of budget items."""
  with open("budget.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    budget_items = []
    for row in reader:
      budget_items.append({
          "name": row[0],
          "amount": row[1],
      })
  return budget_items

def display_budget(budget_items):
  """Displays the budget items."""
  print("Budget:")
  for budget_item in budget_items:
    print(f"  {budget_item['name']}: ${budget_item['amount']}")

def add_budget_item(budget_items):
  """Adds a budget item to the list."""
  name = input("Enter the name of the budget item: ")
  amount = input("Enter the amount of the budget item: ")
  budget_items.append({
      "name": name,
      "amount": amount,
  })

def edit_budget_item(budget_items):
  """Edits a budget item in the list."""
  name = input("Enter the name of the budget item to edit: ")
  for budget_item in budget_items:
    if budget_item["name"] == name:
      new_name = input("Enter the new name of the budget item: ")
      new_amount = input("Enter the new amount of the budget item: ")
      budget_item["name"] = new_name
      budget_item["amount"] = new_amount
      break

def delete_budget_item(budget_items):
  """Deletes a budget item from the list."""
  name = input("Enter the name of the budget item to delete: ")
  for budget_item in budget_items:
    if budget_item["name"] == name:
      budget_items.remove(budget_item)
      break

def save_budget_file(budget_items):
  """Saves the budget items to the file."""
  with open("budget.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for budget_item in budget_items:
      writer.writerow([budget_item["name"], budget_item["amount"]])

def main():
  """The main function."""
  budget_items = read_budget_file()
  while True:
    print("1. Display budget")
    print("2. Add budget item")
    print("3. Edit budget item")
    print("4. Delete budget item")
    print("5. Save budget")
    print("6. Exit")
    option = input("Enter your option: ")
    if option == "1":
      display_budget(budget_items)
    elif option == "2":
      add_budget_item(budget_items)
    elif option == "3":
      edit_budget_item(budget_items)
    elif option == "4":
      delete_budget_item(budget_items)
    elif option == "5":
      save_budget_file(budget_items)
    elif option == "6":
      break

if __name__ == "__main__":
  main()
