# This program was written for fun. Basic, simple baseball game written in Python

import random

strikes = 0 
balls = 0
outs = 0
runner_on_first = False
runner_on_second = False
runner_on_third = False
homes_runs = 0
visitor_runs = 0
innings = 1.0
team_name = "XXX"
pitch_count = 0
pitcher_names = ["Marcus Fundango", "Douglas Smartcar", "Spanky Alfalfa", "Rodriguez Cantadora", "Juan Carlos", "Mike Hunt"]
dinger_names = ["Spunchess Fruitbasket", "Ringo Planet", "Jorge Elefante", "Dylan Forscythe", "Greg Limbo", "Mike Oxlong"]

def end_game():
    global homes_runs
    global visitor_runs
    global team_name
    if homes_runs > visitor_runs:
        print("\n\n{} are the winners!! Great ball game!!".format(team_name))
        print("The final score: %a: %a         Bots: %a" %(team_name,homes_runs, visitor_runs))
    elif homes_runs < visitor_runs:
        print("\n\nThe Bots are the winners!! Terrible ball game by {}".format(team_name))
        print("The final score: %a: %a         Bots: %a" %(team_name,homes_runs, visitor_runs))
    else:
        print("\n\nIts a tie!! No winner is good!!")
        print("The final score: %a: %a         Bots: %a" %(team_name,homes_runs, visitor_runs))

def pitcher():
    global innings
    global end_of_inning
    global balls
    global strikes
    global pitch_count
    global outs
    strike_zone_chance = [0,1]
    while outs < 3:
        print("\nInning %a" %(innings))
        print("\n%a - %a" %(balls,strikes))
        print("Which pitch would you like to throw?: ")
        print("a. Fastball")
        print("b. Curveball")
        print("c. Knuckleball")
        pitch = input()
        if pitch == "a":
            ball_or_strike = random.choice(strike_zone_chance)
            # print(ball_or_strike)
            if ball_or_strike == 0:
                # print("Ball")
                pitch_count += 1
                bot_batter(ball_or_strike)
            elif ball_or_strike == 1:
                # print("Strike")
                pitch_count += 1
                bot_batter(ball_or_strike)
        elif pitch == "b":
            ball_or_strike = random.choice(strike_zone_chance)
            # print(ball_or_strike)
            if ball_or_strike == 0:
                # print("Ball")
                pitch_count += 1
                bot_batter(ball_or_strike)
            elif ball_or_strike == 1:
                # print("Strike")
                pitch_count += 1
                bot_batter(ball_or_strike)
        elif pitch == "c":
            ball_or_strike = random.choice(strike_zone_chance)
            # print(ball_or_strike)
            if ball_or_strike == 0:
                # print("Ball")
                pitch_count += 1
                bot_batter(ball_or_strike)
            elif ball_or_strike == 1:
                # print("Strike")
                pitch_count += 1
                bot_batter(ball_or_strike)

def batter():
    global innings
    global end_of_inning
    global balls
    global strikes
    global pitch_count
    global outs
    strike_zone_chance = [0,1]
    while outs < 3:
        print("\nInning %a" %(innings))
        print("\n%a - %a" %(balls,strikes))
        print("a. Swing")
        print("b. Bunt")
        print("c. Take pitch")
        bat = input()
        if bat == "a":
            ball_or_strike = random.choice(strike_zone_chance)
            if ball_or_strike == 0:
                pitch_count += 1
                bot_pitcher(bat)
            elif ball_or_strike == 1:
                pitch_count += 1
                bot_pitcher(bat)
        elif bat == "b":
            ball_or_strike = random.choice(strike_zone_chance)
            if ball_or_strike == 0:
                pitch_count += 1
                bot_pitcher(bat)
            elif ball_or_strike == 1:
                pitch_count += 1
                bot_pitcher(bat)
        elif bat == "c":
            ball_or_strike = random.choice(strike_zone_chance)
            if ball_or_strike == 0:
                pitch_count += 1
                bot_pitcher(bat)
            elif ball_or_strike == 1:
                pitch_count += 1
                bot_pitcher(bat)

def bot_pitcher(y):
    global strikes
    global balls
    global outs
    global runner_on_first
    global runner_on_second
    global runner_on_third
    global visitor_runs
    global homes_runs
    global team_name
    global pitch_count
    global innings 
    global dinger_names
    bot_pitcher = [0,1]
    player_hit = [0,1,0,1,0,1,0,1,2]
    which_base = [2,3]
    if y == "a":
        hit = random.choice(player_hit)
        pitch = random.choice(bot_pitcher)
        if hit == 0 and pitch == 0:
            strikes += 1
            print("        Strike %a\n" %(strikes))
        elif hit == 1 and pitch == 0:
            strikes += 1
            print("         Strike %a\n" %(strikes))
        elif hit == 2 and pitch == 0:
            strikes += 1
            print("         Strike %a\n" %(strikes))
        elif hit == 0 and pitch == 1:
            print("Ouch! Batter hit by pitch!")
            if runner_on_first == False and runner_on_second == False and runner_on_third == False:
                print("Batter takes first base")
                runner_on_first == True
            elif runner_on_first == True and runner_on_second == False and runner_on_third == False:
                print("Runner from first advances to second, batter takes first base")
                runner_on_first == True
                runner_on_second == True
            elif runner_on_first == True and runner_on_second == True and runner_on_third == False:
                print("Runner from second advances to third, runner from first advances to second and batter takes first base. BASES LOADED")
                runner_on_first == True
                runner_on_second == True
                runner_on_third == True
            balls = 0
            strikes = 0
        elif hit == 1 and pitch == 1:
            base = random.choice(which_base)
            if runner_on_first == False and runner_on_second == False and runner_on_third == False:
                print("Base hit over the %a basemen, runner on first!" %(base))
                runner_on_first = True
                balls = 0
                strikes = 0
            elif runner_on_first == True and runner_on_second == False and runner_on_third == False:
                print("Base hit over the %a basemen, runners on second and first" %(base))
                runner_on_first = True
                runner_on_second = True
                balls = 0
                strikes = 0
            elif runner_on_first == True and runner_on_second == True and runner_on_third == False:
                print("Base hit over the %a basemen, runners on third, second and first. BASES LOADED" %(base))
                runner_on_first = True
                runner_on_second = True
                runner_on_third =  True
                balls = 0
                strikes = 0
            elif runner_on_first == True and runner_on_second == True and runner_on_third == True:
                print("Base hit over the %a basemen, runner from third comes home! Bases still loaded" %(base))
                homes_runs += 1
                print("%a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
                balls = 0
                strikes = 0
        elif hit == 2 and pitch == 1:
            ding = random.choice(dinger_names)
            if runner_on_first == False and runner_on_second == False and runner_on_third == False:
                print("DINGER! Home run hit by %a from the %a"%(ding, team_name))
                homes_runs += 1
                print("%a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
                balls = 0
                strikes = 0
            elif runner_on_first == True and runner_on_second == False and runner_on_third == False:
                print("DINGER! A 2 run home run hit by %a from the %a"%(ding, team_name))
                homes_runs += 2
                print("%a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
                runner_on_first = False
                balls = 0
                strikes = 0
            elif runner_on_first == True and runner_on_second == True and runner_on_third == False:
                print("DINGER! A 3 run home run hit by %a from the %a"%(ding, team_name))
                homes_runs += 3
                print("%a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
                runner_on_first = False
                runner_on_second = False
                balls = 0
                strikes = 0
            elif runner_on_first == True and runner_on_second == True and runner_on_third == True:
                print("DINGER! A GRAND SLAM run home run hit by %a from the %a"%(ding, team_name))
                homes_runs += 4
                print("%a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
                runner_on_first = False
                runner_on_second = False
                runner_on_third = False
                balls = 0
                strikes = 0
    elif y == "b":
        print("Bunting is an automatic out")
        outs += 1
        print("             Outs: %a\n"%(outs))
        balls = 0
        strikes = 0
    elif y == "c":
        pitch = random.choice(bot_pitcher)
        if pitch == 0:
            balls += 1
            print("         Ball %a" %(balls))
        elif pitch == 1:
            strikes += 1
            print("Strike %a" %(strikes))
    if strikes == 3:
        print("Batter is out!!")
        outs += 1
        print("             Outs: %a\n" %(outs))
        balls = 0
        strikes = 0
    elif balls == 4:
        if runner_on_first == False and runner_on_second == False and runner_on_third == False:
            print("Batter walks to first")
            runner_on_first = True
            balls = 0
            strikes = 0
        elif runner_on_first == True and runner_on_second == False and runner_on_third == False:
            print("Batter walks to first, runner on first advances to second")
            runner_on_first = True
            runner_on_second = True
            balls = 0
            strikes = 0
        elif runner_on_first == True and runner_on_second == True and runner_on_third == False:
            print("Batter walks to first, runner on first advances to second, runner on second advances to third. BASES LOADED")
            runner_on_first = True
            runner_on_second = True
            runner_on_third = True
            balls = 0
            strikes = 0
    if outs == 3:
        print("The side is retired! **switching sides**")
        print("The inning ended with a total of %a pitches thrown" %(pitch_count))
        print("Score    %a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
        outs = 0
        pitch_count = 0
        runner_on_first = False
        runner_on_second = False
        runner_on_third = False
        innings += 0.5
        if innings == 10.0:
            end_game()
        else:
            pitcher()
        
    
def bot_batter(x):
    global strikes
    global balls
    global outs
    global runner_on_first
    global runner_on_second
    global runner_on_third
    global visitor_runs
    global homes_runs
    global team_name
    global pitch_count
    global innings
    global pitcher_names
    bot_batter_swing = [0,1,0,1,0,1,0,1,2]
    bot_hit = [0,1]
    which_base = [2,3]
    if x == 0:
        bot_swing = random.choice(bot_batter_swing)
        if bot_swing == 0:
            balls += 1
            print("           Ball %a" %(balls))
        elif bot_swing == 1:
            strikes += 1
            print("           Strike %a" %(strikes))
        elif bot_swing == 2:
            print("Ouch! Batter hit by pitch!")
            if runner_on_first == False and runner_on_second == False and runner_on_third == False:
                print("Batter takes first base")
                runner_on_first == True
            elif runner_on_first == True and runner_on_second == False and runner_on_third == False:
                print("Runner from first advances to second, batter takes first base")
                runner_on_first == True
                runner_on_second == True
            elif runner_on_first == True and runner_on_second == True and runner_on_third == False:
                print("Runner from second advances to third, runner from first advances to second and batter takes first base. BASES LOADED")
                runner_on_first == True
                runner_on_second == True
                runner_on_third == True
            balls = 0
            strikes = 0
    elif x == 1:
        bot_swing = random.choice(bot_batter_swing)
        if bot_swing == 0:
            strikes += 1
            print("          Strike %a" %(strikes))
        elif bot_swing == 1:
            contact = random.choice(bot_hit)
            base = random.choice(which_base)
            if contact == 0:
                print("Ground out to the %a basemen, out at 1st!" %(base))
                outs += 1
                print("          Outs: %a" %(outs))
                balls = 0
                strikes = 0
            elif contact == 1:
                if runner_on_first == False and runner_on_second == False and runner_on_third == False:
                    print("Base hit over the %a basemen, runner on first!" %(base))
                    runner_on_first = True
                    balls = 0
                    strikes = 0
                elif runner_on_first == True and runner_on_second == False and runner_on_third == False:
                    print("Base hit over the %a basemen, runners on second and first" %(base))
                    runner_on_first = True
                    runner_on_second = True
                    balls = 0
                    strikes = 0
                elif runner_on_first == True and runner_on_second == True and runner_on_third == False:
                    print("Base hit over the %a basemen, runners on third, second and first. BASES LOADED" %(base))
                    runner_on_first = True
                    runner_on_second = True
                    runner_on_third =  True
                    balls = 0
                    strikes = 0
                elif runner_on_first == True and runner_on_second == True and runner_on_third == True:
                    print("Base hit over the %a basemen, runner from third comes home! Bases still loaded" %(base))
                    visitor_runs += 1
                    print("%a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
                    balls = 0
                    strikes = 0
        elif bot_swing == 2:
            if runner_on_first == False and runner_on_second == False and runner_on_third == False:
                print("DINGER! Home run hit by the Bot Team")
                visitor_runs += 1
                print("%a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
                balls = 0
                strikes = 0
            elif runner_on_first == True and runner_on_second == False and runner_on_third == False:
                print("DINGER! A 2 run home run hit by the Bot Team")
                visitor_runs += 2
                print("%a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
                runner_on_first = False
                balls = 0
                strikes = 0
            elif runner_on_first == True and runner_on_second == True and runner_on_third == False:
                print("DINGER! A 3 run home run hit by the Bot Team")
                visitor_runs += 3
                print("%a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
                runner_on_first = False
                runner_on_second = False
                balls = 0
                strikes = 0
            elif runner_on_first == True and runner_on_second == True and runner_on_third == True:
                print("DINGER! A GRAND SLAM run home run hit by the Bot Team")
                visitor_runs += 4
                print("%a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
                runner_on_first = False
                runner_on_second = False
                runner_on_third = False
                balls = 0
                strikes = 0
    if strikes == 3:
        print("Batter is out!!")
        outs += 1
        print("             Outs: %a" %(outs))
        balls = 0
        strikes = 0
    elif balls == 4:
        if runner_on_first == False and runner_on_second == False and runner_on_third == False:
            print("Batter walks to first")
            runner_on_first = True
            balls = 0
            strikes = 0
        elif runner_on_first == True and runner_on_second == False and runner_on_third == False:
            print("Batter walks to first, runner on first advances to second")
            runner_on_first = True
            runner_on_second = True
            balls = 0
            strikes = 0
        elif runner_on_first == True and runner_on_second == True and runner_on_third == False:
            print("Batter walks to first, runner on first advances to second, runner on second advances to third. BASES LOADED")
            runner_on_first = True
            runner_on_second = True
            runner_on_third = True
            balls = 0
            strikes = 0
    if outs == 3:
        pit = random.choice(pitcher_names)
        print("The side is retired! **switching sides**")
        print("The inning ended with a total of %a pitches thrown from pitcher %a" %(pitch_count, pit))
        print("Score    %a: %a    Away Team: %a" %(team_name, homes_runs, visitor_runs))
        pitch_count = 0
        runner_on_first = False
        runner_on_second = False
        runner_on_third = False
        outs = 0
        innings += 0.5     
        if innings == 10.0:
            end_game()
        else:
            batter()
  
def main():
    global team_name
    name = input("What is your team name?: ")
    team_name = name
    print("{} vs The Bots!!".format(team_name))
    print("\nWould you like to be the pitcher or the batter?: ")
    choice = input()
    if choice == "pitcher":
        pitcher()
    else:
        batter()

main()
