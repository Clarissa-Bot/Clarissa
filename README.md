# Clarissa

Clarissa is a python-based bot for PCs & Mobile phones.

# How to run?

If it's your first time, run 'python setup.py [SETUP_PATH]'. Example: 'python setup.py pwd'.

#  Q&A

Q: What is the end goal? A: The end goal is to allow commercial use of a mockup of IBM's Watson.

Q: Can I use this for my own app? A: Sure! We've got it open source for a reason!

Q: Is this a finished product? A: No. Much like Minecraft, this project is and will always be in beta mode.

Q: What is the project's goal? A: The goal is to add machine learning to a python bot. This has never been done before. We plan on having it be able to determine the next president by 2020. That feature will be deactivated by default until voting time.

# Current version
We are on version 1.2.1.6-PROD

# What's new?
Nothing really, just patched some errors in setup file, and added forwards compatibility to newer pip versions.

# How do I make an app for this?
To make a new app, run:
cpk make APP_NAME
But you need the developer_edition, so clone that instead. Run git clone https://github.com/Clarissa-Bot/Clarissa.git -b developer_edition

To package the app, run:
cpk compile LOCATION_OF_APP CPK_NAME
But again, must have developer edition

To install an app, run:
cpk install LOCATION_OF_APP

To run an app, run:
cpk run APP_NAME

# What will be in the next version?
We added optional updating of commands database by setup file. Be sure to try it out, if you understand modifications of corpi.