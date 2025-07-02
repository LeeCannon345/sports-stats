def show_football_stats():
  stats = {
    'Team' : 'Kansas City Chiefs',
    'Wins' : 13,
    'Losses' : 4,
    'Passing Yards' : 4100,
    'Rushing Yards' : 1900,
    'Touchdowns' : 55 
  }
  print ("\n Football Stats:")
  for key, value in stats.items():
    print (f"{key}: {value}")

def show_basketball_stats():
  stats = {
    'Team' : 'Los Angeles Lakers',
    'Wins' : 50,
    'Losses' : 32,
    'Pionts Per Game' : 110,
    'Rebounds Per Game' : 45,
    'Assists Per Game' : 25
  }
  print ("\n Basketball Stats:")
  for key, value in stats.items():
   print (f"{key}: {value}")

def show_baseball_stats():
  stats = {
    'Team' : 'New York Yankees',
    'Wins' : 108,
    'Losses' : 54,
    'Home Runs' : 250,
    'Batting Average' : .285,  
    'ERA' : 123.91
  }
  print ("\n Baseball Stats:")
  for key, value in stats.items():
    print (f"{key}: {value}")

def main():
  while True:
    print("\nSporting Stats Menu ===")
    print("1. View Football Stats")
    print("2. View Basketball Stats")
    print("3. View Baseball Stats")
    print("4. Exit")
    choice = input("Enter your choice (1-4):")
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
