section_name = input("Class section: ")
coordinator_name = input("Coordinator name: ")
sports = ["Basketball", "Volleyball", "Badminton", "Chess", "Table Tennis"]
categories = ["Team", "Team", "Individual", "Individual", "Individual"]
print("\n==========================================")
print(" INTRAMURALS -- SPORTS EVENTS ")
print("==========================================")

for i in range(len(sports)):
    print(str(i + 1) + ". " + sports[i] + "\t[" + categories[i] + "]")
print("==========================================\n")
logged_games = []
total_points = 0
game_num = 1

while game_num <= 4:
    print("--- GAME " + str(game_num) + " ---")
    sport_choice = int(input("Sport number (0 to skip): "))

    if sport_choice == 0:
        print("Game skipped.\n")
        game_num = game_num + 1
    
    elif 1 <= sport_choice <= 5:
        opponent = input("Opposing section: ")
        result = input("Result (W/L): ").upper()

        if result == "W" or result == "L":
            points_earned = 0
            if result == "W":
                points_earned = 3
            total_points = total_points + points_earned
            sport_name = sports[sport_choice - 1]
            category_name = categories[sport_choice - 1]
            game_entry = [sport_name, category_name, opponent, result, points_earned]
            logged_games.append(game_entry)
            print("Successfully logged.\n")
            game_num = game_num + 1
        else:
            print("Invalid Result! Please enter W or L.\n")
            
    else:
        print("Invalid Sport Number! Please choose 1-5 or 0.\n")

if total_points >= 9:
    standing = "GOLD CONTENDER"
elif total_points >= 6:
    standing = "SILVER PUSH"
else:
    standing = "KEEP FIGHTING!"

print("\n" + "="*42)
print(" GAME RESULTS BOARD")
print("="*42)
print("Section : " + section_name)
print("Coordinator : " + coordinator_name)
print("-" * 42)

count = 1
for game in logged_games:
    log_text = str(count) + ". " + game[0] + " (" + game[1] + ") vs " + game[2]
    log_text = log_text + " | Result: " + game[3] + " | " + str(game[4]) + " pts"
    print(log_text)
    count = count + 1

print("-" * 42)
print("TOTAL POINTS: " + str(total_points))
print("STANDING : " + standing)
print("=" * 42)
