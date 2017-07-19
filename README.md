# What is Machine Learning, *really*?
### By Adam Raveret

The terms “Artificial Intelligence” and “Machine Learning” were coined way back in the 1950s, but recent increases in processing power have made the terms more relevant now than ever. Computers have beaten the best humans in the world at complex games like Chess and Go, cars are on the verge of driving themselves, and it all seems to be due to the magic of “Machine Learning.” Senior research scientist at Google, Greg Corrado, says “It’s not magic. It’s just a really important tool” that will soon permeate most aspects of society. But as nice as it would be to doze off during our morning commutes, others warn against the threats that come with AI. President Obama released a report in October of 2016 discussing the potential impact it could have on our labor force, and Elon Musk continually makes known his opinion that AI poses an “existential threat” to civilization. But before we judge its efficacy, what exactly do these terms mean?

To answer that, let’s start with their earliest definitions:
- At the first academic conference on the subject in 1956, John McCarthy offered the farsighted, yet vague definition of Artificial Intelligence as the “science and engineering of making intelligent machines.” 
- In 1959, Arthur Samuel defined Machine Learning as “a field of study that gives computers the ability to learn without being explicitly programmed.” 

The second is a little more explicitly stated, but both men define each term using words within the terms itself. What exactly does it mean for a computer to “learn” or be “intelligent”? None refute a computer’s ability to process logic, but those terms seem to imply *thinking*, which is another ballgame. In 1950, Alan Turing famously developed a test of machine “intelligence”, which hypothesized that an appropriately programmed computer with enough inputs and outputs would be able to imitate a human (through written correspondence) without detection. Now-a-days, this seems like a low bar to set for “intelligence.” Twitter bots, using terabytes of human crafted responses as inputs, can mimic human reaction simply enough. John Searle, whose 1980s Chinese room thought experiment refutes the idea that mimicry passes for “intelligence,” calls this “Weak AI.” In his thought experiment, Searle hypothesizes a machine that could pass the Turing test in Chinese and posits that by following the same processes as the machine, he (a non-Chinese speaker) would also pass the Turing test without any understanding of the exchange. His point is to say that while a computer can simulate intelligence, it lacks a conscious understanding (for now!). Before we get too philosophical with this (what is our mind other than a collection of data inputs collected through experience?), let’s recap: We know Artificial Intelligence and Machine Learning are not actual *thinking*, so then what are they? 

They both center around the idea of computers simulating “smart” actions, but differ in scope. While Artificial Intelligence broadly represents a machine’s ability to perform human task (including process automation as well as cognitive automation). Machine Learning is one application of AI that focuses on providing parameters and data (or the ability to create data), allowing the computer to discover patterns without explicit programming. How you ask? Let’s illustrate through an example ([code here](https://github.com/araveret/tic_tac_toe_sim/blob/master/tic_tac_toe_sim.py) if you want to follow along):

Suppose we want to develop a program to play tic-tac-toe optimally. Because of the simplicity of the game, we could likely hard code the optimal response to each combination of moves, but it would be a painstaking process. Alternatively, we could use Machine Learning to create the ultimate player. First we would first import the parameters of the game: create the board, the win scenarios, the alternating turns, and method of selecting a space. Later we will use data to inform our selections, but since I have thrown out all those cocktail napkins, we’ll have to start with random selections. 

**Step 1.** Below is an example of each turn of play and an example of how you might store that game’s data (lines 8 – 114 in the code). Notice in the data that a winning result is recorded as a 1 for each move after the game is completed. 

![alt text](https://github.com/araveret/tic_tac_toe_sim/blob/master/images/step_1.png "Step 1 Image")

**Step 2.** Now we’ll simulate 1000 games using random selections and store the data as our training set for future simulations. Below is the distribution of results and the means of the result across each of the first selections (lines 115 – 216). Notice that when randomizing selections, a win occurs twice as often as as a loss and 6 times as often as a draw. Also notice that all first selections average above 0.5, meaning they are most likely to result in a win, with the middle spot resulting in a win most often. 

![alt text](https://github.com/araveret/tic_tac_toe_sim/blob/master/images/step_2.png "Step 2 Image")

**Step 3.** We’ll simulate another 1000 games, but this time instead of randomizing the selections, we’ll use the data from our previous simulations to inform the selections. Situations that resulted in a win in the past will be prioritized, while situations that resulted in a loss will be avoided. Below is again the distribution of results and the mean of the results across each first selection (lines 217 – 327). The top results are for this 1000 games, the bottom results are for the cumulative 2000 games. Notice how different these results are from the randomized selections. Also notice that the majority of games are ending in a draw.

![alt text](https://github.com/araveret/tic_tac_toe_sim/blob/master/images/step_3.png "Step 3 Image")

**Step 4.** We’ll simulate another 1000 games using our cumulative training set to inform our selections, and again display the results below (lines 328 - 438). Notice how the most recent simulations as well as the cumulative set both converge to 0.5. 

![alt text](https://github.com/araveret/tic_tac_toe_sim/blob/master/images/step_4.png "Step 4 Image")

We just created a program to play tic-tac-toe optimally using "Machine Learning"… **BAM!**

