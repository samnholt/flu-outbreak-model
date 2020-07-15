# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:13:06 2020

@author: HP
"""
import numpy as np



np.random.seed(0)
nums = 1000     #noumber of students
fract = 0.01    #fraction initially immune
recovr = 0.2    #chance of recovering per day
num_infect = 1  #number of infected per day
numd = 40       #number of days
reps = 40       #number of repetitions
data = []   
sdata = []
data = np.zeros(numd)                #array for infected 
sdata = np.zeros(numd)               #array for susceptible ##     

remov = 0                            #number removed

for k in range(reps) :                   #loop for repeat calc
    
    # 0=immune 1= suscep 2= infcted
    P = np.zeros(nums)                #student array to zero
    for i in range(nums) :            #choose susceptibles
        P[i] = 1                         #all susceptible
    fn = int(fract*nums)              #fn = amount initially immune
    n = 0
    while n < fn :                    #while the amount initialliy immune is more than zero exact frac * nums immune
        rr = np.random.randint(1, nums)   #random number in students
        ra = rr                #not sure
        if P[rr] != 0 :         #find random person in array P then change them to immune?
            P[rr] = 0
            n = n+1                     #turn everyone in fract immune
    n = 0
    while n < 1 :                                   #patie zero?
        rr = np.random.randint(1, nums)       
        ra = rr
        if P[rr] == 1 :
            P[rr] = 2
            n = 1
    
    # main part of calculation follows
    for j in range(numd) : #loop over days
        for i in range(nums) : #loop over students
            if P[i] == 2 : #spread infection
                for ii in num_infect : #for everyone who is infected
                    ra = rr       #infect new student
                    if P[rr] == 2 :
                        P[rr] = 2
                        remov = remov + 1      #number removed
            if np.random.random_sample() < recovr :     #chance of recovery
                ra = rr
                if P[rr] == 2 :
                    P[rr] = 0
        
        c = 0
        s = 0
        for i in range(nums):       #find no. infected
            if P[i] == 2:
                c = c+1
            if P[i] == 1:
                s = s+1
        data[j] = data[j] + c
        sdata[j] = sdata[j] + s
    num_fected = remov*1.0/reps
    print(num_fected)

                
                
                
             
            
        
        
        
    
    
