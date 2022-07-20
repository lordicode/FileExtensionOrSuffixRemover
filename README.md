# FileExtensionOrSuffixRemover
Sometimes our AWS servers will act up when we or client will try to upload multi hundreds of gigabytes archives to it. 
Adding a random extension to volumes that AWS is having troubles with helps solve all issues.
However, we end up with a large quantity of renamed volumes, which is a chore to rename by hand.

This is a little excercise in Python, plus a program that actually solves an issue - you input the directory and the suffix that you want to remove, and in a second all the volumes are named how you want them to.
