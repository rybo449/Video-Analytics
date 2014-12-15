import time

import random

import operator

import numpy as np

import matplotlib.cm as cm

import scipy.ndimage as nd

import matplotlib.pyplot as plt


img = nd.imread('images/digits.png')

nums = img.reshape(50,20,100,20).transpose(0,2,1,3).reshape(5000,20,20)

nums_avg = np.array([nums[i*500:(i+1)*500].mean(0) for i in range(10)])

PT = nums_avg.reshape(10,400)

P  = PT.transpose()

PTPinv = np.linalg.inv(np.dot(PT,P))


failures_n_guesses = []

for nmrl in xrange(10):
    
    total_incorrect_count = 0
    
    incorrect_count_dict = dict([(dgt,0) for dgt in xrange(10)])
    
    myLst = []
    
    for idx_o_nmrl in xrange(500):
        
        index = nmrl * 500 + idx_o_nmrl
    
        samp = nums[index]
        
        PTyy = np.dot(PT,samp.flatten())

        avec = np.dot(PTPinv,PTyy)
    
        myLst.append(avec)
        
        if np.argmax(avec) != nmrl:
            
            failures_n_guesses.append((index, np.argmax(avec)))
        
            total_incorrect_count += 1
            
            incorrect_count_dict[np.argmax(avec)] += 1

    myLst = np.vstack(myLst)
    
    lst_o_lst_o_coefs = myLst.T
    
    fig_i, axes_i = plt.subplots(10,1, sharex=True)
    
    for idx in range(len(axes_i)):
            
        axes_i[idx].hist(lst_o_lst_o_coefs[idx], bins = 100)
        
        axes_i[idx].set_yticklabels('')

        axes_i[idx].set_title(str(nmrl) + '\'s' + ' regressed against ' + str(idx) + '\'s', fontsize=10)
        
        axes_i[idx].set_xlim(-1.75,1.75)

    fig_i.subplots_adjust(hspace = 2)
            
    fig_i.canvas.draw()
    
    sorted_incorrect_count_lst_o_tups = sorted(incorrect_count_dict.items(), key=operator.itemgetter(1), reverse = True)
    
    print "%s%% of %s's were incorrectly identified, the most common guess for those failures was %s's" % ((total_incorrect_count/500.0) * 100, nmrl, sorted_incorrect_count_lst_o_tups[0][0])
        
    fig_i.show()


fig, ax = plt.subplots()

fig.subplots_adjust(0,0,1,1)

ax.axis('off')

img_dgt = ax.imshow(nums[0], cmap="Greys_r")

t0 = time.time()

dt = 0.0


while dt < 30. :
    
    rndInt = random.randint(0, len(failures_n_guesses))
    
    failure = failures_n_guesses[rndInt][0]
    
    guess = failures_n_guesses[rndInt][1]

    if dt == 0.0:
        
        img_dgt.set_data(nums[failure])
        
        txt = fig.suptitle('Guess: ' + str(guess), color = 'w')
        
    
    else:
    
        
        img_dgt.set_data(nums[failure])

        txt.set_text('Guess: ' + str(guess))

    fig.canvas.draw()
    
    fig.show()
    
    time.sleep(1.0)
    
    dt = time.time() - t0



plt.clf()

print "\n"

print "Removing zero point offset:\n"

PT1 = nums_avg.reshape(10,400)

PT = np.vstack((PT1, np.ones(400)))

P  = PT.transpose()

PTPinv = np.linalg.inv(np.dot(PT,P))


failures_n_guesses = []

for nmrl in xrange(10):
    
    total_incorrect_count = 0
    
    incorrect_count_dict = dict([(dgt,0) for dgt in xrange(10)])
    
    myLst = []
    
    for idx_o_nmrl in xrange(500):
        
        index = nmrl * 500 + idx_o_nmrl
    
        samp = nums[index]
        
        PTyy = np.dot(PT,samp.flatten())

        avec = np.dot(PTPinv,PTyy)

        avec = avec[0:10]
    
        myLst.append(avec[0:10])
        
        if np.argmax(avec) != nmrl:
            
            failures_n_guesses.append((index, np.argmax(avec)))
        
            total_incorrect_count += 1
            
            incorrect_count_dict[np.argmax(avec)] += 1

    myLst = np.vstack(myLst)
    
    lst_o_lst_o_coefs = myLst.T
    
    fig_i, axes_i = plt.subplots(10,1, sharex=True)
    
    for idx in range(len(axes_i)):
            
        axes_i[idx].hist(lst_o_lst_o_coefs[idx], bins = 100)
        
        axes_i[idx].set_yticklabels('')

        axes_i[idx].set_title(str(nmrl) + '\'s' + ' regressed against ' + str(idx) + '\'s', fontsize=10)
        
        axes_i[idx].set_xlim(-1.75,1.75)
            
    fig_i.subplots_adjust(hspace = 2)

    fig_i.canvas.draw()
    
    sorted_incorrect_count_lst_o_tups = sorted(incorrect_count_dict.items(), key=operator.itemgetter(1), reverse = True)
    
    print "%s%% of %s's were incorrectly identified, the most common guess for those failures was %s's" % ((total_incorrect_count/500.0) * 100, nmrl, sorted_incorrect_count_lst_o_tups[0][0])
        
    fig_i.show()



