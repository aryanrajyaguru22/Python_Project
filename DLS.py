def calculate_dls_target(overs_total, wickets_lost, current_score, overs_remaining, resources_table):
    """Calculate target score using DLS method"""
    initial_resources = resources_table[overs_total][0]  # Resources at start
    remaining_resources = resources_table[overs_remaining][wickets_lost]
    used_resources = initial_resources - remaining_resources
    
    target = round((current_score / used_resources) * initial_resources)
    return target

def create_resources_table():
    """Create a simplified resources table"""
    # This is a simplified version of the DLS resources table
    # Format: {overs: [resources percentage for 0,1,2,3,4,5,6,7,8,9 wickets]}
    resources = {
        50: [100.0, 93.4, 85.1, 74.9, 62.7, 49.0, 34.9, 22.0, 11.9, 4.7],
        45: [95.0, 89.1, 81.5, 72.1, 60.7, 47.6, 34.1, 21.6, 11.7, 4.6],
        40: [89.3, 84.2, 77.3, 68.7, 58.2, 45.8, 32.9, 20.9, 11.4, 4.5],
        35: [82.7, 78.2, 72.2, 64.6, 55.0, 43.6, 31.5, 20.1, 11.0, 4.4],
        30: [75.1, 71.3, 66.1, 59.5, 51.0, 40.8, 29.8, 19.1, 10.5, 4.2],
        25: [66.5, 63.3, 58.9, 53.4, 46.1, 37.3, 27.5, 17.8, 9.8, 4.0],
        20: [56.6, 54.2, 50.7, 46.3, 40.3, 32.9, 24.6, 16.1, 9.0, 3.7],
        15: [45.2, 43.4, 40.9, 37.7, 33.2, 27.5, 20.9, 13.9, 7.9, 3.3],
        10: [32.1, 31.0, 29.4, 27.3, 24.4, 20.6, 15.9, 10.8, 6.3, 2.7],
        5: [17.2, 16.8, 16.1, 15.1, 13.7, 11.9, 9.4, 6.6, 4.1, 1.9]
    }
    return resources

def main():
    print("Cricket DLS Calculator")
    print("=====================")
    
    try:
        # Get match details from user
        total_overs = int(input("Enter total overs in the match: "))
        if total_overs not in [20, 25, 30, 35, 40, 45, 50]:
            print("Please enter valid overs (20, 25, 30, 35, 40, 45, or 50)")
            return
        
        team1_score = int(input("Enter Team 1's score: "))
        
        # Get interruption details
        overs_completed = float(input("Enter overs completed when rain interrupted: "))
        wickets_lost = int(input("Enter wickets lost at interruption: "))
        if wickets_lost > 9:
            print("Wickets lost cannot be more than 9")
            return
        
        overs_possible = float(input("Enter overs possible after interruption: "))
        if overs_possible > total_overs:
            print("Overs possible cannot be more than total overs")
            return
        
        # Calculate overs remaining
        overs_remaining = total_overs - overs_completed
        if overs_remaining < 0:
            print("Invalid overs calculation")
            return
        
        # Get resources table
        resources_table = create_resources_table()
        
        # Calculate target
        new_target = calculate_dls_target(
            total_overs,
            wickets_lost,
            team1_score,
            round(overs_possible),
            resources_table
        )
        
        # Display results
        print("\nDLS Calculation Results:")
        print("========================")
        print(f"Original Target: {team1_score + 1}")
        print(f"Revised Target: {new_target + 1}")
        print(f"Target in {overs_possible} overs: {new_target + 1} runs")
        
        required_rate = (new_target + 1) / overs_possible
        print(f"Required Run Rate: {required_rate:.2f}")

    except ValueError as e:
        print("Please enter valid numerical values")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()