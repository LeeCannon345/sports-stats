def show_football_stats():
  stats = {
    'Team' : 'Kansas City Chiefs',
    'Wins' : 13,
    'Losses' : 4,
    'Passing Yards' : 4100,
    'Rushing Yards' : 1900,
    'Touchdowns' : 55
  }
  print("\n Football Stats:")
  for key, value in stats.items():
    print(f"{key}: {value}")

def show_basketball_stats():
  stats = {
    'Team' : 'Golden State Warriors',
    'Wins' : 44,
    'Losses' : 38,
    'Points Per Game' : 118.9,
    'Rebounds' : 45.2,
    'Assists' : 28.8
  }
  print("\n Basketball Stats:")
  for key, value in stats.items():
    print(f"{key}: {value}")

def show_baseball_stats():
  stats = {
    'Team' : 'Los Angeles Dodgers',
    'Wins' : 93,
    'Losses' : 69,
    'Home Runs' : 200,
    'Batting Average' : .247,
    'ERA' : 3.91
  }
  print("\n Baseball Stats:")
  for key, value in stats.items():
    print(f"{key}: {value}")

def main():
  while True:
    print("\n Sporting Stats Menu ===")
    print("1. View Football Stats")
    print("2. View Basketball Stats")
    print("3. View Baseball Stats")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
      show_football_stats()
    elif choice == '2':
      show_basketball_stats()
    elif choice == '3':
      show_baseball_stats()
    elif choice == '4':
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()