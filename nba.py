import random
import numpy as np
import math
import time

#SIMULATOR BASIC 1.5.2
        #new 1.5.2: Indents in display 
        #new 1.5.1: On/off dramatic score display
        #new 1.5: More realistic results

        #to do: OT betting, AH, all teams, player betting


print('''ODDS:

To win (incl. OT):

    HOU 1.93
    DAL 1.97

Match Total (incl. OT):

    179,5 U 25.00 | O 1.02
    189,5 U 12.00 | O 1.05
    199,5 U 6.00 | O 1.15
    204,5 U 4.00 | O 1.27
    209,5 U 2.90 | O 1.45
    214,5 U 2.20 | O 1.70
    219,5 U 1.80 | O 2.10
    229,5 U 1.30 | O 3.75
    239,5 U 1.10 | O 8.00
    249,5 U 1.04 | O 18.00

Player Points (incl. OT):

    Luka Doncic 34,5
    U 1.90 | O 1.90

Input 'drama' to switch between ON/OFF dramatic result display

''')



Hou_wins = Dal_wins = Draws = max_numb_OT = 0
quiet_sim = False
odd_gen = False
dramatic = False


# Home team default (HOUSTON)

hatt_3p = 0.5
hatt_2p = 0.38
hatt_3ft = 0.02
hatt_2ft = 0.1

#h3ptacc = np.random.normal(0.343,0.069)
#h2ptacc = np.random.normal(0.558,0.112)
#hftacc = np.random.normal(0.795,0.159)

havg_poss = 108.2
hsigma = 0.01*havg_poss

hturnov = 0.141

# Away team default (DALLAS)

aatt_3p = 0.38
aatt_2p = 0.5
aatt_3ft = 0.02
aatt_2ft = 0.1

#a3ptacc = np.random.normal(0.362,0.072)
#a2ptacc = np.random.normal(0.551,0.110)
#aftacc = np.random.normal(0.780,0.156)

aavg_poss = 103.6
asigma = 0.01*aavg_poss

aturnov = 0.122


Hou_ez = Dal_ez = -100
diff = Hou_ez_Hou = Hou_ez_Dal = Dal_ez_Hou = Dal_ez_Dal = 0

doncic_avg = 0.32
doncic_sigma = 0.05

doncic_max_pts = 0

Home_dram_poss = Away_dram_poss = 0


def sim(home_name='HOU', away_name='DAL'):
    global Home_pts, Away_pts, Home_numb_poss
    global OT_no, is_draw
    global Hou_ez, Dal_ez, Hou_ez_Hou, Hou_ez_Dal, Dal_ez_Hou, Dal_ez_Dal, diff
    global doncic_pts, doncic_max_pts


##    h3ptacc = np.random.normal(0.343,0.069)
##    h2ptacc = np.random.normal(0.558,0.112)
##    hftacc = np.random.normal(0.795,0.159)
##
##    a3ptacc = np.random.normal(0.362,0.072)
##    a2ptacc = np.random.normal(0.551,0.110)
##    aftacc = np.random.normal(0.780,0.156)
    
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

    Home_numb_poss = math.floor(int(np.random.normal(havg_poss,hsigma)))
    Away_numb_poss = math.floor(int(np.random.normal(aavg_poss,asigma)))
    
    for i in range(Home_numb_poss):

        
        homeAction_tb = random.random()
        if homeAction_tb < hatt_3p*(1-hturnov):
            Home_action = 1 #3pt attempt (+possible FT)
        elif homeAction_tb < (hatt_3p + hatt_2p)*(1-hturnov):
            Home_action = 2 #2pt attempt (+possible FT)
        elif homeAction_tb < (hatt_3p + hatt_2p + hatt_3ft)*(1-hturnov):
            Home_action = 3 #3 free throws
        elif homeAction_tb < (1-hturnov):
            Home_action = 4 #2 free throws
        else:
            Home_action = 5 #turnover
            
        if Home_action == 1:
            h3ptacc = np.random.normal(0.343,0.069)
            Home_3pt_attempted += 1
            Succ = random.random()
            if Succ < h3ptacc:                                      #ZUCC
                Home_pts += 3
                Home_3pt_scored += 1
                bonus_ft = random.random()
                if bonus_ft > 0.9:
                    Home_ft_attempted += 1
                    hftacc = np.random.normal(0.795,0.5*0.159)
                    Succ = random.random()
                    if Succ < hftacc:
                        Home_pts += 1
                        Home_ft_scored += 1
        
        elif Home_action == 2:
            h2ptacc = np.random.normal(0.558,0.112)
            Home_2pt_attempted += 1
            Succ = random.random()
            if Succ < h2ptacc:
                Home_pts += 2
                Home_2pt_scored += 1
                bonus_ft = random.random()
                if bonus_ft > 0.9:
                    Home_ft_attempted += 1
                    hftacc = np.random.normal(0.795,0.5*0.159)
                    Succ = random.random()
                    if Succ < hftacc:
                        Home_pts += 1
                        Home_ft_scored += 1

        elif Home_action == 3:
            Home_ft_attempted += 3
            for free_throw in range(3):
                hftacc = np.random.normal(0.795,0.5*0.159)
                Succ = random.random()
                if Succ < hftacc:
                    Home_pts += 1
                    Home_ft_scored += 1
                    
        elif Home_action == 4:
            Home_ft_attempted += 2
            for free_throw in range(2):
                hftacc = np.random.normal(0.795,0.5*0.159)
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
            a3ptacc = np.random.normal(0.362,0.072)
            Away_3pt_attempted +=1
            Succ = random.random()
            if Succ < a3ptacc:
                Away_pts += 3
                Away_3pt_scored +=1
                bonus_ft = random.random()
                if bonus_ft > 0.9:
                    Away_ft_attempted += 1
                    aftacc = np.random.normal(0.780,0.5*0.156)
                    Succ = random.random()
                    if Succ < aftacc:
                        Away_pts += 1
                        Away_ft_scored += 1

        elif Away_action == 2:
            a2ptacc = np.random.normal(0.551,0.110)
            Away_2pt_attempted +=1
            Succ = random.random()
            if Succ < a2ptacc:
                Away_pts += 2
                Away_2pt_scored += 1
                bonus_ft = random.random()
                if bonus_ft > 0.9:
                    Away_ft_attempted += 1
                    aftacc = np.random.normal(0.780,0.5*0.156)
                    Succ = random.random()
                    if Succ < aftacc:
                        Away_pts += 1
                        Away_ft_scored += 1

        elif Away_action == 3:
            Away_ft_attempted += 3
            for free_throw in range(3):
                aftacc = np.random.normal(0.780,0.5*0.156)
                Succ = random.random()
                if Succ < aftacc:
                    Away_pts += 1
                    Away_ft_scored += 1
                
        elif Away_action == 4:
            Away_ft_attempted += 2
            for free_throw in range(2):
                aftacc = np.random.normal(0.780,0.5*0.156)
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
        diff = Home_pts - Away_pts
        if diff > Hou_ez:
            Hou_ez = diff
            Hou_ez_Hou = Home_pts
            Hou_ez_Dal = Away_pts
    elif Home_pts == Away_pts:
        Draws += 1
        is_draw = 1
    elif Away_pts > Home_pts:
        Dal_wins += 1
        diff = Away_pts - Home_pts
        if diff > Dal_ez:
            Dal_ez = diff
            Dal_ez_Dal = Away_pts
            Dal_ez_Hou = Home_pts

    if is_draw == 1:   
        while is_draw == 1:
            OT_Home_numb_poss = math.floor(int(0.104*np.random.normal(havg_poss,hsigma)))
            OT_Away_numb_poss = math.floor(int(0.104*np.random.normal(aavg_poss,asigma)))
            OT_no += 1
            if OT_no > max_numb_OT:
                max_numb_OT = OT_no
            
            for i in range(OT_Home_numb_poss):
                homeAction_tb = random.random()
                if homeAction_tb < hatt_3p*(1-hturnov):
                    Home_action = 1 #3pt attempt (+possible FT)
                elif homeAction_tb < (hatt_3p + hatt_2p)*(1-hturnov):
                    Home_action = 2 #2pt attempt (+possible FT)
                elif homeAction_tb < (hatt_3p + hatt_2p + hatt_3ft)*(1-hturnov):
                    Home_action = 3 #3 free throws
                elif homeAction_tb < (1-hturnov):
                    Home_action = 4 #2 free throws
                else:
                    Home_action = 5 #turnover
                    
                if Home_action == 1:
                    h3ptacc = np.random.normal(0.343,0.069)
                    Home_3pt_attempted += 1
                    Succ = random.random()
                    if Succ < h3ptacc:                                      #ZUCC
                        Home_pts += 3
                        Home_3pt_scored += 1
                        bonus_ft = random.random()
                        if bonus_ft > 0.9:
                            Home_ft_attempted += 1
                            hftacc = np.random.normal(0.795,0.5*0.159)
                            Succ = random.random()
                            if Succ < hftacc:
                                Home_pts += 1
                                Home_ft_scored += 1

                elif Home_action == 2:
                    h2ptacc = np.random.normal(0.558,0.112)
                    Home_2pt_attempted +=1
                    Succ = random.random()
                    if Succ < h2ptacc:
                        Home_pts += 2
                        Home_2pt_scored += 1
                        bonus_ft = random.random()
                        if bonus_ft > 0.9:
                            Home_ft_attempted += 1
                            hftacc = np.random.normal(0.795,0.5*0.159)
                            Succ = random.random()
                            if Succ < hftacc:
                                Home_pts += 1
                                Home_ft_scored += 1

                elif Home_action == 3:
                    Home_ft_attempted += 3
                    for free_throw in range(3):
                        hftacc = np.random.normal(0.795,0.5*0.159)
                        Succ = random.random()
                        if Succ < hftacc:
                            Home_pts += 1
                            Home_ft_scored += 1
                            
                elif Home_action == 4:
                    Home_ft_attempted += 2
                    for free_throw in range(2):
                        hftacc = np.random.normal(0.795,0.5*0.159)
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
                    a3ptacc = np.random.normal(0.362,0.072)
                    Away_3pt_attempted +=1
                    Succ = random.random()
                    if Succ < a3ptacc:
                        Away_pts += 3
                        Away_3pt_scored +=1
                        bonus_ft = random.random()
                        if bonus_ft > 0.9:
                            Away_ft_attempted += 1
                            aftacc = np.random.normal(0.780,0.5*0.156)
                            Succ = random.random()
                            if Succ < aftacc:
                                Away_pts += 1
                                Away_ft_scored += 1

                elif Away_action == 2:
                    a2ptacc = np.random.normal(0.551,0.110)
                    Away_2pt_attempted +=1
                    Succ = random.random()
                    if Succ < a2ptacc:
                        Away_pts += 2
                        Away_2pt_scored += 1
                        bonus_ft = random.random()
                        if bonus_ft > 0.9:
                            Away_ft_attempted += 1
                            aftacc = np.random.normal(0.780,0.5*0.156)
                            Succ = random.random()
                            if Succ < aftacc:
                                Away_pts += 1
                                Away_ft_scored += 1

                
                elif Away_action == 3:
                    Away_ft_attempted += 3
                    for free_throw in range(3):
                        aftacc = np.random.normal(0.780,0.5*0.156)
                        Succ = random.random()
                        if Succ < aftacc:
                            Away_pts += 1
                            Away_ft_scored += 1
                        
                elif Away_action == 4:
                    Away_ft_attempted += 2
                    for free_throw in range(2):
                        aftacc = np.random.normal(0.780,0.5*0.156)
                        Succ = random.random()
                        if Succ < aftacc:
                            Away_pts += 1
                            Away_ft_scored += 1

                elif Away_action == 5:
                    Away_turnovers += 1
                    
            if Home_pts != Away_pts:
                if Home_pts > Away_pts:
                    Hou_wins += 1
                    diff = Home_pts - Away_pts
                    if diff > Hou_ez:
                        Hou_ez = diff
                        Hou_ez_Hou = Home_pts
                        Hou_ez_Dal = Away_pts
                else:
                    Dal_wins += 1
                    diff = Away_pts - Home_pts
                    if diff > Dal_ez:
                        Dal_ez = diff
                        Dal_ez_Dal = Away_pts
                        Dal_ez_Hou = Home_pts
                
                is_draw = 0
                Draws -= 1
                if max_numb_OT == OT_no:
                    most_OT_home = Home_pts
                    most_OT_away = Away_pts

    doncic_pts = math.floor((np.random.normal(doncic_avg, doncic_sigma))*Away_pts)
    if doncic_pts < 0:
        doncic_pts = 0

    if doncic_pts > doncic_max_pts:
        doncic_max_pts = doncic_pts
           
    
    if quiet_sim == False:
        if dramatic == False:
            print('')
            print ('%s %s : %s %s' %(home_name, Home_pts, Away_pts, away_name))
            if OT_no > 0:
                print (' '*4 + 'after %s overtime(s)' % OT_no)
            print ('')
            print (' '*4 + '%s %s/%s 3pt, %s/%s 2pt, %s/%s ft, %s turnovers' %
               (home_name, Home_3pt_scored, Home_3pt_attempted, Home_2pt_scored, Home_2pt_attempted,
               Home_ft_scored, Home_ft_attempted, Home_turnovers))
            print (' '*4 + '%s %s/%s 3pt, %s/%s 2pt, %s/%s ft, %s turnovers' %
               (away_name, Away_3pt_scored, Away_3pt_attempted, Away_2pt_scored, Away_2pt_attempted,
               Away_ft_scored, Away_ft_attempted, Away_turnovers))
            print (' '*4 + 'Doncic %s pts' % (doncic_pts))
        
        elif dramatic == True:
            print ('''Dramatic score enabled
                                                ''')
            time.sleep(2)
            print ('%s %s/%s 3pt, %s/%s 2pt, %s/%s ft, %s turnovers' %
               (home_name, Home_3pt_scored, Home_3pt_attempted, Home_2pt_scored, Home_2pt_attempted,
               Home_ft_scored, Home_ft_attempted, Home_turnovers))
            time.sleep(1)
            print (' '*4 + '%s %s/%s 3pt, %s/%s 2pt, %s/%s ft, %s turnovers' %
               (away_name, Away_3pt_scored, Away_3pt_attempted, Away_2pt_scored, Away_2pt_attempted,
               Away_ft_scored, Away_ft_attempted, Away_turnovers))
            time.sleep(1)
            print (' '*4 + 'Doncic %s pts' % (doncic_pts))
            time.sleep(1)
            print ('')
            print (' '*4 + '%s: %s' %(home_name, Home_pts))
            time.sleep(3)
            print ('%s: %s' %(away_name, Away_pts))
            if OT_no > 0:
                print (' '*4 + 'after %s overtime(s)' % OT_no)

            
most_OT_home = most_OT_away = max_numb_OT = 0



def multisim(number):
    global Hou_wins, Dal_wins, Draws
    global Hou_max, Dal_max, Hou_min, Dal_min
    global max_numb_OT, most_OT_home, most_OT_away
    global Hou_ez, Dal_ez, diff, Hou_ez_Hou, Hou_ez_Dal, Dal_ez_Hou, Dal_ez_Dal
    global doncic_pts, doncic_max_pts
    Hou_wins = Dal_wins = Draws = 0
    Hou_max = Dal_max = 0
    Hou_min = Dal_min = 200
    max_numb_OT = 0
    doncic_max_pts = 0

    Hou_ez = Dal_ez = -100
    diff = Hou_ez_Hou = Hou_ez_Dal = Dal_ez_Hou = Dal_ez_Dal = 0

    sum_pts = 0
    o209 = o179 = o189 = o199 = o204 = o214 = o219 = o229 = o239 = o249 = 0
    
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

        pts_this_game = Home_pts + Away_pts
        sum_pts += pts_this_game

        if pts_this_game >= 180:
            o179 += 1
        if pts_this_game >= 190:
            o189 += 1
        if pts_this_game >= 200:
            o199 += 1
        if pts_this_game >= 205:
            o204 += 1
        if pts_this_game >= 210:
            o209 += 1
        if pts_this_game >= 215:
            o214 += 1
        if pts_this_game >= 220:
            o219 += 1
        if pts_this_game >= 230:
            o229 += 1
        if pts_this_game >= 240:
            o239 += 1
        if pts_this_game >= 250:
            o249 += 1

            
    avg_pts = sum_pts/number
    if odd_gen == True:
        perc_o179 = (o179 /number)*100
        perc_o189 = (o189 /number)*100
        perc_o199 = (o199 /number)*100
        perc_o204 = (o204 /number)*100
        perc_o209 = (o209 /number)*100
        perc_o214 = (o214 /number)*100
        perc_o219 = (o219 /number)*100
        perc_o229 = (o229 /number)*100
        perc_o239 = (o239 /number)*100
        perc_o249 = (o249 /number)*100

        odd_o179 = round(1+(0.95*((100/perc_o179)-1)),2)
        odd_o189 = round(1+(0.95*((100/perc_o189)-1)),2)
        odd_o199 = round(1+(0.95*((100/perc_o199)-1)),2)
        odd_o204 = round(1+(0.95*((100/perc_o204)-1)),2)
        odd_o209 = round(1+(0.95*((100/perc_o209)-1)),2)
        odd_o214 = round(1+(0.95*((100/perc_o214)-1)),2)
        odd_o219 = round(1+(0.95*((100/perc_o219)-1)),2)
        odd_o229 = round(1+(0.95*((100/perc_o229)-1)),2)
        odd_o239 = round(1+(0.95*((100/perc_o239)-1)),2)
        odd_o249 = round(1+(0.95*((100/perc_o249)-1)),2)

        dd_u180 = (100/(100-perc_o179))
        dd_u190 = round((100/(100-perc_o189)),2)
        dd_u200 = round((100/(100-perc_o199)),2)
        dd_u205 = round((100/(100-perc_o204)),2)
        dd_u210 = round((100/(100-perc_o209)),2)
        dd_u215 = round((100/(100-perc_o214)),2)
        dd_u220 = round((100/(100-perc_o219)),2)
        dd_u230 = round((100/(100-perc_o229)),2)
        dd_u240 = round((100/(100-perc_o239)),2)
        dd_u250 = round((100/(100-perc_o249)),2)

        odd_u180 = round(1+(0.95*(dd_u180-1)),2)
        odd_u190 = round(1+(0.95*(dd_u190-1)),2)
        odd_u200 = round(1+(0.95*(dd_u200-1)),2)
        odd_u205 = round(1+(0.95*(dd_u205-1)),2)
        odd_u210 = round(1+(0.95*(dd_u210-1)),2)
        odd_u215 = round(1+(0.95*(dd_u215-1)),2)
        odd_u220 = round(1+(0.95*(dd_u220-1)),2)
        odd_u230 = round(1+(0.95*(dd_u230-1)),2)
        odd_u240 = round(1+(0.95*(dd_u240-1)),2)
        odd_u250 = round(1+(0.95*(dd_u250-1)),2)
   
        
            
    print ('')
    print ('HOU %s, DAL %s, draw %s' % (Hou_wins, Dal_wins, Draws))
    print ('')
    print (' '*4 + 'HOU max: %s, HOU min: %s' % (Hou_max, Hou_min))
    print (' '*4 + 'DAL max: %s, DAL min: %s' % (Dal_max, Dal_min))
    print (' ')
    print (' '*4 + 'HOU biggest win: +%s  (%s : %s)' % (Hou_ez,Hou_ez_Hou, Hou_ez_Dal))
    print (' '*4 + 'DAL biggest win: +%s  (%s : %s)' % (Dal_ez, Dal_ez_Hou, Dal_ez_Dal))
    print (' '*4 + 'Doncic max %s pts' % (doncic_max_pts))
    print (' ')
    
    if max_numb_OT > 0:
        print (' '*4 + 'Most OTs: %s, while the end score was %s : %s' % (max_numb_OT, most_OT_home, most_OT_away))
    #print ('Avg points pg: %s' % avg_pts)
    if odd_gen == True:
        print ('179,5 u%s  o%s   189,5 u%s o%s   199,5 u%s o%s   204,5 u%s o%s   209,5 u%s o%s   214,5 u%s o%s   219,5 u%s o%s   229,5 u%s o%s   239,5 u%s o%s   249,5 u%s o%s' %
               (odd_u180,odd_o179,odd_u190,odd_o189,odd_u200,odd_o199,odd_u205,odd_o204,odd_u210,odd_o209,odd_u215,odd_o214,odd_u220,odd_o219,odd_u230,odd_o229,odd_u240,odd_o239,odd_u250,odd_o249))
    print (' ')
    
    quiet_sim = False
    

    
continue_sim = True

while continue_sim == True:
    #print(' ')
    g1 = input('How many simulations do you want to generate (or use command)?')
    if g1 == 'drama' and dramatic == True:
        dramatic = False
        print ('Dramatic display OFF')
    elif g1 == 'drama' and dramatic == False:
        dramatic = True
        print ('Dramatic display ON')      
    else:
        g = int(g1)
        print(' ')
        if g != 1 and dramatic == True:
            dramatic = False
            print ('''Dramatic only available for 1 match
Dramatic display OFF
                   ''')
            
    

        if g < 10:
            for i in range(g):
                sim()
                print(' ')
                print(' ')

        else:
            multisim(g)
            

          
         
            
