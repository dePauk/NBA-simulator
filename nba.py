import random
import numpy as np
import math

Hou_wins = Dal_wins = 0
quiet_sim = False

# SIMULATOR BASIC 1


# Home team default (HOUSTON)

hatt_3p = 0.5
hatt_2p = 0.38
hatt_3ft = 0.02
hatt_2ft = 0.1

h3ptacc = 0.343
h2ptacc = 0.558
hftacc = 0.795

havg_poss = 108.2
hsigma = 4

hturnov = 0.141

# Away team default (DALLAS)

aatt_3p = 0.38
aatt_2p = 0.5
aatt_3ft = 0.02
aatt_2ft = 0.1

a3ptacc = 0.362
a2ptacc = 0.551
aftacc = 0.780

aavg_poss = 103.6
asigma = 4

aturnov = 0.122

def sim(home_name='HOU', away_name='DAL'):
    global Home_pts, Away_pts, Home_numb_poss
    global OT_no, is_draw
    
    # Basic result variables
    Home_pts = Away_pts = 0
    Home_action = Away_action = 0
    Home_turnovers = Away_turnovers = 0
    OT_no = is_draw = 0

    # Stats variables
    Home_3pt_scored = Home_3pt_attempted = Home_2pt_scored = Home_2pt_attempted = 0
    Home_ft_scored = Home_ft_attempted = 0

    Away_3pt_scored = Away_3pt_attempted = Away_2pt_scored = Away_2pt_attempted = 0
    Away_ft_scored = Away_ft_attempted = 0

    Home_numb_poss = math.floor(int(np.random.normal(havg_poss,hsigma)))-1
    Away_numb_poss = math.floor(int(np.random.normal(aavg_poss,asigma)))-1
    
    for i in range(Home_numb_poss):
        homeAction_tb = random.random()
        if homeAction_tb < hatt_3p*(1-hturnov):
            Home_action = 1 #3pt attempt
        elif homeAction_tb < (hatt_3p + hatt_2p)*(1-hturnov):
            Home_action = 2 #2pt attempt
        elif homeAction_tb < (hatt_3p + hatt_2p + hatt_3ft)*(1-hturnov):
            Home_action = 3 #3 free throws
        elif homeAction_tb < (1-hturnov):
            Home_action = 4 #2 free throws
        else:
            Home_action = 5 #turnover
            
        if Home_action == 1:
            Home_3pt_attempted += 1
            Succ = random.random()
            if Succ < h3ptacc:                                      #ZUCC
                Home_pts += 3
                Home_3pt_scored += 1
            pass
        elif Home_action == 2:
            Home_2pt_attempted += 1
            Succ = random.random()
            if Succ < h2ptacc:
                Home_pts += 2
                Home_2pt_scored += 1
            pass
        elif Home_action == 3:
            Home_ft_attempted += 3
            for free_throw in range(3):
                Succ = random.random()
                if Succ < hftacc:
                    Home_pts += 1
                    Home_ft_scored += 1
        elif Home_action == 4:
            Home_ft_attempted += 2
            for free_throw in range(2):
                Succ = random.random()
                if Succ < hftacc:
                    Home_pts += 1
                    Home_ft_scored += 1

        elif Home_action == 5:
            Home_turnovers += 1

    for i in range(Away_numb_poss):   
        awayAction_tb = random.random()
        if awayAction_tb < aatt_3p*(1-aturnov):
            Away_action = 1 #3pt attempt
        elif awayAction_tb < (aatt_3p + aatt_2p)*(1-aturnov):
            Away_action = 2 #2pt attempt
        elif awayAction_tb < (aatt_3p + aatt_2p + aatt_3ft)*(1-aturnov):
            Away_action = 3 #3 free throws
        elif awayAction_tb < (1-aturnov):
            Away_action = 4 #2 free throws
        else:
            Away_action = 5 #turnover
            
        if Away_action == 1:
            Away_3pt_attempted +=1
            Succ = random.random()
            if Succ < a3ptacc:
                Away_pts += 3
                Away_3pt_scored +=1
            pass
        elif Away_action == 2:
            Away_2pt_attempted +=1
            Succ = random.random()
            if Succ < a2ptacc:
                Away_pts += 2
                Away_2pt_scored += 1
            pass
        elif Away_action == 3:
            Away_ft_attempted += 3
            for free_throw in range(3):
                Succ = random.random()
                if Succ < aftacc:
                    Away_pts += 1
                    Away_ft_scored += 1
                
        elif Away_action == 4:
            Away_ft_attempted += 2
            for free_throw in range(2):
                Succ = random.random()
                if Succ < aftacc:
                    Away_pts += 1
                    Away_ft_scored += 1

        elif Away_action == 5:
            Away_turnovers += 1
            

        #print (Home_pts, Away_pts)
    global Hou_wins, Dal_wins, Draws
    global quiet_sim
    global max_numb_OT
    global most_OT_home, most_OT_away
    
    if Home_pts > Away_pts:
        Hou_wins += 1
    elif Home_pts == Away_pts:
        Draws += 1
        is_draw = 1
    elif Away_pts > Home_pts:
        Dal_wins += 1

    if is_draw == 1:   
        while is_draw == 1:
            OT_Home_numb_poss = math.floor(int(0.104*np.random.normal(havg_poss,hsigma)))-1
            OT_Away_numb_poss = math.floor(int(0.104*np.random.normal(aavg_poss,asigma)))-1
            OT_no += 1
            if OT_no > max_numb_OT:
                max_numb_OT = OT_no
            
            for i in range(OT_Home_numb_poss):
                homeAction_tb = random.random()
                if homeAction_tb < hatt_3p*(1-hturnov):
                    Home_action = 1 #3pt attempt
                elif homeAction_tb < (hatt_3p + hatt_2p)*(1-hturnov):
                    Home_action = 2 #2pt attempt
                elif homeAction_tb < (hatt_3p + hatt_2p + hatt_3ft)*(1-hturnov):
                    Home_action = 3 #3 free throws
                elif homeAction_tb < (1-hturnov):
                    Home_action = 4 #2 free throws
                else:
                    Home_action = 5 #turnover
                    
                if Home_action == 1:
                    Home_3pt_attempted += 1
                    Succ = random.random()
                    if Succ < h3ptacc:                                      #ZUCC
                        Home_pts += 3
                        Home_3pt_scored += 1
                    pass
                elif Home_action == 2:
                    Home_2pt_attempted += 1
                    Succ = random.random()
                    if Succ < h2ptacc:
                        Home_pts += 2
                        Home_2pt_scored += 1
                    pass
                elif Home_action == 3:
                    Home_ft_attempted += 3
                    for free_throw in range(3):
                        Succ = random.random()
                        if Succ < hftacc:
                            Home_pts += 1
                            Home_ft_scored += 1
                elif Home_action == 4:
                    Home_ft_attempted += 2
                    for free_throw in range(2):
                        Succ = random.random()
                        if Succ < hftacc:
                            Home_pts += 1
                            Home_ft_scored += 1

                elif Home_action == 5:
                    Home_turnovers += 1

            for i in range(OT_Away_numb_poss):   
                awayAction_tb = random.random()
                if awayAction_tb < aatt_3p*(1-aturnov):
                    Away_action = 1 #3pt attempt
                elif awayAction_tb < (aatt_3p + aatt_2p)*(1-aturnov):
                    Away_action = 2 #2pt attempt
                elif awayAction_tb < (aatt_3p + aatt_2p + aatt_3ft)*(1-aturnov):
                    Away_action = 3 #3 free throws
                elif awayAction_tb < (1-aturnov):
                    Away_action = 4 #2 free throws
                else:
                    Away_action = 5 #turnover
                    
                if Away_action == 1:
                    Away_3pt_attempted +=1
                    Succ = random.random()
                    if Succ < a3ptacc:
                        Away_pts += 3
                        Away_3pt_scored +=1
                    pass
                elif Away_action == 2:
                    Away_2pt_attempted +=1
                    Succ = random.random()
                    if Succ < a2ptacc:
                        Away_pts += 2
                        Away_2pt_scored += 1
                    pass
                elif Away_action == 3:
                    Away_ft_attempted += 3
                    for free_throw in range(3):
                        Succ = random.random()
                        if Succ < aftacc:
                            Away_pts += 1
                            Away_ft_scored += 1
                        
                elif Away_action == 4:
                    Away_ft_attempted += 2
                    for free_throw in range(2):
                        Succ = random.random()
                        if Succ < aftacc:
                            Away_pts += 1
                            Away_ft_scored += 1

                elif Away_action == 5:
                    Away_turnovers += 1
                    
            if Home_pts != Away_pts:
                is_draw = 0
                Draws -= 1
                if max_numb_OT == OT_no:
                    most_OT_home = Home_pts
                    most_OT_away = Away_pts
           
    
    if quiet_sim == False:
        print ('')
        print ('%s %s : %s %s' %(home_name, Home_pts, Away_pts, away_name))
        print ('')
        print ('%s %s/%s 3pt, %s/%s 2pt, %s/%s ft, %s turnovers' %
               (home_name, Home_3pt_scored, Home_3pt_attempted, Home_2pt_scored, Home_2pt_attempted,
               Home_ft_scored, Home_ft_attempted, Home_turnovers))
        print ('%s %s/%s 3pt, %s/%s 2pt, %s/%s ft, %s turnovers' %
               (away_name, Away_3pt_scored, Away_3pt_attempted, Away_2pt_scored, Away_2pt_attempted,
               Away_ft_scored, Away_ft_attempted, Away_turnovers))
    pass


def multisim(number):
    global Hou_wins, Dal_wins, Draws
    global Hou_max, Dal_max, Hou_min, Dal_min
    global max_numb_OT, most_OT_home, most_OT_away
    Hou_wins = Dal_wins = Draws = 0
    Hou_max = Dal_max = 0
    Hou_min = Dal_min = 200
    max_numb_OT = 0
    for i in range(number):
        global Home_pts, Away_pts
        
        global quiet_sim
        quiet_sim = True
        sim()
        
        if Home_pts > Hou_max:
            Hou_max = Home_pts
        if Away_pts > Dal_max:
            Dal_max = Away_pts
        if Home_pts < Hou_min:
            Hou_min = Home_pts
        if Away_pts < Dal_min:
            Dal_min = Away_pts
            
    print ('')
    print ('HOU %s, DAL %s, draw %s' % (Hou_wins, Dal_wins, Draws))
    print ('')
    print ('HOU max: %s, HOU min: %s' % (Hou_max, Hou_min))
    print ('DAL max: %s, DAL min: %s' % (Dal_max, Dal_min))
    print ('Most OTs: %s while the end score was %s : %s' % (max_numb_OT, most_OT_home, most_OT_away))
    quiet_sim = False
    
    
def multi_sim2(number):
    for i in range(number):
        sim()
    print (Hou_wins)


        

        

        
        
      
        
        
