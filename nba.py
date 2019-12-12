import random

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

# Away team default (DALLAS)

aatt_3p = 0.38
aatt_2p = 0.5
aatt_3ft = 0.02
aatt_2ft = 0.1

a3ptacc = 0.362
a2ptacc = 0.551
aftacc = 0.780

def sim(home_name='HOU', away_name='DAL'):
    global Home_pts, Away_pts
    # Basic result variables
    Home_pts = 0
    Away_pts = 0
    Home_action = 0
    Away_action = 0

    # Stats variables
    Home_3pt_scored = Home_3pt_attempted = Home_2pt_scored = Home_2pt_attempted = 0
    Home_ft_scored = Home_ft_attempted = 0

    Away_3pt_scored = Away_3pt_attempted = Away_2pt_scored = Away_2pt_attempted = 0
    Away_ft_scored = Away_ft_attempted = 0
    
    for i in range(92):
        homeAction_tb = random.random()
        if homeAction_tb < hatt_3p:
            Home_action = 1 #3pt attempt
        elif homeAction_tb < hatt_3p + hatt_2p:
            Home_action = 2 #2pt attempt
        elif homeAction_tb < hatt_3p + hatt_2p + hatt_3ft:
            Home_action = 3 #3 free throws
        else:
            Home_action = 4 #2 free throws
            
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


        awayAction_tb = random.random()
        if awayAction_tb < aatt_3p:
            Away_action = 1 #3pt attempt
        elif awayAction_tb < aatt_3p + aatt_2p:
            Away_action = 2 #2pt attempt
        elif awayAction_tb < aatt_3p + aatt_2p + aatt_3ft:
            Away_action = 3 #3 free throws
        else:
            Away_action = 4 #2 free throws
            
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

        #print (Home_pts, Away_pts)
    global Hou_wins, Dal_wins, Draws
    global quiet_sim
    if Home_pts > Away_pts:
        Hou_wins += 1
    elif Home_pts == Away_pts:
        Draws += 1
    else:
        Dal_wins += 1
    if quiet_sim == False:
        print ('')
        print ('%s %s : %s %s' %(home_name, Home_pts, Away_pts, away_name))
        print ('')
        print ('%s %s/%s 3pt, %s/%s 2pt, %s/%s ft' %
               (home_name, Home_3pt_scored, Home_3pt_attempted, Home_2pt_scored, Home_2pt_attempted,
               Home_ft_scored, Home_ft_attempted))
        print ('%s %s/%s 3pt, %s/%s 2pt, %s/%s ft' %
               (away_name, Away_3pt_scored, Away_3pt_attempted, Away_2pt_scored, Away_2pt_attempted,
               Away_ft_scored, Away_ft_attempted))
    pass

Dal_wins = 0
Hou_wins = 0
Draws = 0
Hou_max = 0
Dal_max = 0
Hou_min = 200
Dal_min = 200

def multisim(number):
    for i in range(number):
        global Home_pts, Away_pts, Hou_wins, Dal_wins, Draws
        global Hou_max, Hou_min, Dal_max, Dal_min
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
    quiet_sim = False
    
    
def multi_sim2(number):
    for i in range(number):
        sim()
    print (Hou_wins)


        

        

        
        
      
        
        
