def show_football_stats():
  stats = {
    'Team' : 'Kansas City Chiefs',
    'Wins' : 13,
    'Losses' : 4,
    'Passing Yards' : 4100,
    'Rushing Yards' : 1900,
<<<<<<< HEAD
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
=======
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
>>>>>>> 1a3e86faffa3bd98d3303463e8fe0d4495932923
    print("1. View Football Stats")
    print("2. View Basketball Stats")
    print("3. View Baseball Stats")
    print("4. Exit")
<<<<<<< HEAD
    choice = input("Enter your choice (1-4): ")
=======
    choice = input("Enter your choice (1-4):")
>>>>>>> 1a3e86faffa3bd98d3303463e8fe0d4495932923
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
<<<<<<< HEAD
  main()
=======
  main()
>>>>>>> 1a3e86faffa3bd98d3303463e8fe0d4495932923
