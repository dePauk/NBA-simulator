import random
import numpy as np
import math
import tkinter as tk

#SIMULATOR BASIC 1.3
        #new: biggest wins
        #to do: OT betting, AH




'''

ODDS:

To win (incl. OT):

HOU 1.93
DAL 1.97



Match Total (incl. OT):

179,5 U 8.00 | O 1.10
189,5 U 4.30 | O 1.25
199,5 U 2.75 | O 1.50
204,5 U 2.25 | O 1.70
209,5 U 1.93 | O 1.97
214,5 U 1.70 | O 2.25
219,5 U 1.50 | O 2.75
229,5 U 1.25 | O 4.30
239,5 U 1.11 | O 7.75
249,5 U 1.05 | O 14.00

'''



print('ODDS:')
print('')
print('To win (incl. OT): ')
print('')
print('HOU 1.93')
print('DAL 1.97')
print('')
print('Match Total (incl. OT):')
print('')
print('179,5 U 8.00 | O 1.10')
print('189,5 U 4.30 | O 1.25')
print('199,5 U 2.75 | O 1.50')
print('204,5 U 2.25 | O 1.70')
print('209,5 U 1.93 | O 1.97')
print('214,5 U 1.70 | O 2.25')
print('219,5 U 1.50 | O 2.75')
print('229,5 U 1.25 | O 4.30')
print('239,5 U 1.11 | O 7.75')
print('249,5 U 1.05 | O 14.00')




Hou_wins = Dal_wins = Draws = max_numb_OT = 0
quiet_sim = False
odd_gen = False

# SIMULATOR BASIC 1


# Home team default (HOUSTON)

hatt_3p = 0.5
hatt_2p = 0.38
hatt_3ft = 0.02
hatt_2ft = 0.1

#h3ptacc = np.random.normal(0.343,0.069)
#h2ptacc = np.random.normal(0.558,0.112)
#hftacc = np.random.normal(0.795,0.159)

havg_poss = 108.2
hsigma = 4

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
asigma = 4

aturnov = 0.122


Hou_ez = Dal_ez = -100
diff = Hou_ez_Hou = Hou_ez_Dal = Dal_ez_Hou = Dal_ez_Dal = 0

global home_name, away_name

def sim(home_name='HOU', away_name='DAL'):

    global Home_pts, Away_pts, Home_numb_poss
    global OT_no, is_draw
    global Hou_ez, Dal_ez, Hou_ez_Hou, Hou_ez_Dal, Dal_ez_Hou, Dal_ez_Dal, diff

    h3ptacc = np.random.normal(0.343,0.069)
    h2ptacc = np.random.normal(0.558,0.112)
    hftacc = np.random.normal(0.795,0.159)

    a3ptacc = np.random.normal(0.362,0.072)
    a2ptacc = np.random.normal(0.551,0.110)
    aftacc = np.random.normal(0.780,0.156)
    
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
           
    
    if quiet_sim == False:
        print ('')
        print ('%s %s : %s %s' %(home_name, Home_pts, Away_pts, away_name))
        if OT_no > 0:
            print ('after %s overtime(s)' % OT_no)
        print ('')
        print ('%s %s/%s 3pt, %s/%s 2pt, %s/%s ft, %s turnovers' %
               (home_name, Home_3pt_scored, Home_3pt_attempted, Home_2pt_scored, Home_2pt_attempted,
               Home_ft_scored, Home_ft_attempted, Home_turnovers))
        print ('%s %s/%s 3pt, %s/%s 2pt, %s/%s ft, %s turnovers' %
               (away_name, Away_3pt_scored, Away_3pt_attempted, Away_2pt_scored, Away_2pt_attempted,
               Away_ft_scored, Away_ft_attempted, Away_turnovers))
    pass

most_OT_home = most_OT_away = max_numb_OT = 0






def multisim(number):
    global Hou_wins, Dal_wins, Draws
    global Hou_max, Dal_max, Hou_min, Dal_min
    global max_numb_OT, most_OT_home, most_OT_away
    global Hou_ez, Dal_ez, diff, Hou_ez_Hou, Hou_ez_Dal, Dal_ez_Hou, Dal_ez_Dal
    Hou_wins = Dal_wins = Draws = 0
    Hou_max = Dal_max = 0
    Hou_min = Dal_min = 200
    max_numb_OT = 0

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
    print (' ')
    print ('HOU max: %s, HOU min: %s' % (Hou_max, Hou_min))
    print ('DAL max: %s, DAL min: %s' % (Dal_max, Dal_min))
    print (' ')
    print ('HOU biggest win: +%s  (%s : %s)' % (Hou_ez,Hou_ez_Hou, Hou_ez_Dal))
    print ('DAL biggest win: +%s  (%s : %s)' % (Dal_ez, Dal_ez_Hou, Dal_ez_Dal))
    print (' ')
    
    if max_numb_OT > 0:
        print ('Most OTs: %s, while the end score was %s : %s' % (max_numb_OT, most_OT_home, most_OT_away))
    #print ('Avg points pg: %s' % avg_pts)
    if odd_gen == True:
        print ('179,5 u%s  o%s   189,5 u%s o%s   199,5 u%s o%s   204,5 u%s o%s   209,5 u%s o%s   214,5 u%s o%s   219,5 u%s o%s   229,5 u%s o%s   239,5 u%s o%s   249,5 u%s o%s' %
               (odd_u180,odd_o179,odd_u190,odd_o189,odd_u200,odd_o199,odd_u205,odd_o204,odd_u210,odd_o209,odd_u215,odd_o214,odd_u220,odd_o219,odd_u230,odd_o229,odd_u240,odd_o239,odd_u250,odd_o249))
    print (' ')
    
    quiet_sim = False
    
    

#Monte Carlo 1m:
    
    #Avg points pg: 209.485996
    
    #HOU 505414, DAL 494586, draw 0
    
    #HOU max: 198, HOU min: 29
    #DAL max: 201, DAL min: 31

#Monte Carlo 10m @0.05 margin:
    
    #Avg points pg: 209.5538546

    #HOU 5047863, DAL 4952137, draw 0

    #HOU max: 209, HOU min: 25
    #DAL max: 200, DAL min: 22

    #Most OTs: 5 while the end score was 144 : 143
        
#179,5 u7.99  o1.13   189,5 u4.39 o1.27   199,5 u2.75 o1.52
#204,5 u2.27 o1.71   209,5 u1.93 o1.97   214,5 u1.68 o2.32
#219,5 u1.5 o2.8   229,5 u1.27 o4.43   239,5 u1.13 o7.83   249,5 u1.07 o15.52




current_gen_no = 1
all_the_stats = "Currently only console output"

def visual_refresh():
    visual_number['text'] = str(current_gen_no)


def result_visual_refresh():
    global home_name, Home_pts, Away_pts, away_name
    show_result['text'] = str(all_the_stats)
                            

def sim_stats():
    all_the_stats = "%s " % Home_pts



##        print ('')
##        print ('%s %s : %s %s' %(home_name, Home_pts, Away_pts, away_name))
##        if OT_no > 0:
##            print ('after %s overtime(s)' % OT_no)
##        print ('')
##        print ('%s %s/%s 3pt, %s/%s 2pt, %s/%s ft, %s turnovers' %
##               (home_name, Home_3pt_scored, Home_3pt_attempted, Home_2pt_scored, Home_2pt_attempted,
##               Home_ft_scored, Home_ft_attempted, Home_turnovers))
##        print ('%s %s/%s 3pt, %s/%s 2pt, %s/%s ft, %s turnovers' %
##               (away_name, Away_3pt_scored, Away_3pt_attempted, Away_2pt_scored, Away_2pt_attempted,
##               Away_ft_scored, Away_ft_attempted, Away_turnovers))


    


def plus1gen():
    global current_gen_no
    current_gen_no += 1
    visual_refresh()

def plus10gen():
    global current_gen_no
    current_gen_no += 10
    visual_refresh()
    
def plus100gen():
    global current_gen_no
    current_gen_no += 100
    visual_refresh()

def plus1kgen():
    global current_gen_no
    current_gen_no += 1000
    visual_refresh()
    
def plus10kgen():
    global current_gen_no
    current_gen_no += 10000
    visual_refresh()

def plus100kgen():
    global current_gen_no
    current_gen_no += 100000
    visual_refresh()
    

def minus1gen():
    global current_gen_no
    if current_gen_no < 2:
        pass
    else:    
        current_gen_no -= 1
    visual_refresh()

def minus10gen():
    global current_gen_no
    if current_gen_no < 11:
        pass
    else:
        current_gen_no -= 10
    visual_refresh()

def minus100gen():
    global current_gen_no
    if current_gen_no < 101:
        pass
    else:       
        current_gen_no -= 100
    visual_refresh()

def minus1kgen():
    global current_gen_no
    if current_gen_no < 1001:
        pass
    else:
        current_gen_no -= 1000
    visual_refresh()

def minus10kgen():
    global current_gen_no
    if current_gen_no < 10001:
        pass
    else:
        current_gen_no -= 10000
    visual_refresh()

def minus100kgen():
    global current_gen_no
    if current_gen_no < 100001:
        pass
    else:
        current_gen_no -= 100000
    visual_refresh()
    
def simulate_tk():
    global home_name
    if current_gen_no <10:
        sim()
        all_the_stats = "cmon"
    else:
        multisim(current_gen_no)
    all_the_stats = "cmon"
    result_visual_refresh()



window = tk.Tk()

title = tk.Frame(window)
title.pack()


number_gen = tk.Frame(window)
number_gen.pack()

number_gen1 = tk.Frame(window)
number_gen1.pack()

visual_number = tk.Label(window)
visual_number.pack()
visual_refresh()

generator = tk.Frame(window)
generator.pack()

show_result = tk.Label(window)
show_result.pack()
result_visual_refresh()



title_text = tk.Label(title, text = 'How many matches do you want to generate?').pack()

current_gen = tk.Label(number_gen, text = 'No. of matches:  ').grid(row=0, column=0)

plus_1 = tk.Button(number_gen1, text = '+1', command=plus1gen).grid(row=0, column=0)
plus_10 = tk.Button(number_gen1, text = '+10', command=plus10gen).grid(row=0, column=1)
plus_100 = tk.Button(number_gen1, text = '+100', command=plus100gen).grid(row=0, column=2)
plus_1k = tk.Button(number_gen1, text = '+1k', command=plus1kgen).grid(row=0, column=3)
plus_10k = tk.Button(number_gen1, text = '+10k', command=plus10kgen).grid(row=0, column=4)
plus_100k = tk.Button(number_gen1, text = '+100k', command=plus100kgen).grid(row=0, column=5)

minus_1 = tk.Button(number_gen1, text = '-1', command=minus1gen).grid(row=1, column=0)
minus_10 = tk.Button(number_gen1, text = '-10', command=minus10gen).grid(row=1, column=1)
minus_100 = tk.Button(number_gen1, text = '-100', command=minus100gen).grid(row=1, column=2)
minus_1k = tk.Button(number_gen1, text = '-1k', command=minus1kgen).grid(row=1, column=3)
minus_10k = tk.Button(number_gen1, text = '-10k', command=minus10kgen).grid(row=1, column=4)
minus_100k = tk.Button(number_gen1, text = '-100k', command=minus100kgen).grid(row=1, column=5)

generate = tk.Button(generator, text = 'Generate!', command = simulate_tk).pack()


window.mainloop()


    
continue_sim = True

while continue_sim == True:
    print(' ')
    g = int(input('How many simulations do you want to generate? '))
    print(' ')

    if g < 10:
        for i in range(g):
            sim()
            print(' ')
            print(' ')

    else:
        multisim(g)

    continue_sim = False



###




            

          
         
            
