# PnR-Final
The final project for my Programming and Robotics class.  My job was to move my robot from one side of an obstacle course to the other.  Using what I have learned in Mr. Adiletta's Programming and Robotics class I
have programmed my robot to do just that.

#Some Things To Know
Mr. Adiletta has created a parent class,`pigo.py, that had the basic code to get us started.  In the pigo.py file Mr. Adiletta will also update it with handy new methods to help us out.  We worked in the student.py file.
The first method that I made was the dance method.  At the very top of my code I have put some instance variables that remain constant throughout all my code.  Some of the variables include my midpoint, the point at which my robots
head is facing forward, and my left and right speed.

##About Some of My Methods
`self.backwards()`
The lazy method that I created is  kind of self explanatory, and slightly stupid.  When I was calibrating my robot I got _very_* of having to get up every time and pick up my robot and bring it back.
I thought to myself, "Wow I wish my robot could magically just come bcak to me".  Then I realized that I could.  Basically, I just made a method to move backwards a little bit and added it to my menu.

`self.testDrive()`
The cruise method is very important to my code because it makes going through the obstacle course **much** more quick and efficient.
 Basically if the robot detects that it is clear straight ahead, it will cruise at a constant speed until it detects something is in its way.

`self.tooClose()`
While tinkering with my robot and running it through the course many times I realized that when it was just too close to an object the robot would get sort of confused and get stuck in a loop going back and forth.
That is when I decided to create the back up method so that if it is ever too close the robot will back up.

`self.chooseBetter()`
This method is key for my robot to getting through the obstacle course because it is how it determines its turns.  The robot scans from negative 60 degrees to positive 60 degrees and averages the distances.
After it averages the distances it turns to the side that has the larger average.

`self.calibrate()`
Calibrate is a method in the pigo.py file that Mr. Adiletta made and it is something that I use nearly ever class.  Calibrate helps me make sure my robots head is facing forward.
It also helps me ensure that when the robot uses the test drive that is drives straight forward.

`self.encR()`, `self.encL()`, `self.encB()`, `self.encF()`
These methods make my robot go right, left, forward, and backwards.  I have used these methods within other methods, such as `self.backwards()` and `self.dance()`.
You can set the exact value at which it turns or moves forward/backwards.

`self.dance()`
The dance method is a method that the whole class has tinkered with before we went into programming our robot to maneuver through obstacles.  This method uses `self.encR()`, `self.encL()`, `self.encB()`, amd self.encF()` a lot.
This method was basically created so that when my robot makes it through the course it can have a victory dance.

##
