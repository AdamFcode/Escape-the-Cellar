# Escape the Cellar
Escape the Cellar is a python-based text adventure that challenges the user to escape a cellar that they have been imprisoned in by a formless entity. This entity serves as the narrator and leads the user through a sequence of challenges that require choices to be made by the user. The game has several points at which the user can "fail" and be offered the chance to try again. There are only two means of escaping, each requiring the user to successfully navigate through the choices until they reach the end.

The deployed site can be accessed from here: [Escape the Cellar](https://escape-the-cellar-de7d0d9c5297.herokuapp.com/)

# Preparation
In preparation for this project, multiple websites and videos were consulted, as well as several "text-adventure" books, particularly from the "Goosebumps" series. These were studied to get an intuitive understanding of how such adventures are typically constructed.

The flow of the adventure was planned out using Lucid Chart, allowing for the two 'pathways' to be concisely illustrated. Provided in the relevant section below, this chart helped immensely in organising and visualising the flow of the project's functions and choices. 

Once the initial preparation was complete, potential "testers" were consulted in order to get an understanding of what they would expect from a text-adventure game.

## User Stories
* As a user, I want to play an interactive game that requires no downloads or installations
* As a user, I want to receive clear instructions and choices from the app
* As a user, I want my inputted data to be handled correctly and to return advancement in the "adventure"
* As a user, I want to be offered the chance to play again should I win or lose
* As a user, I want to replay the app and reasonably expect a varied experience

The above will be addressed under Testing below.

## Lucid Chart
Lucid Chart was selected to visualise the flow of the adventure and to provide a visual guide to reference when writing the code. The free version of Lucid Chart was used which limits the number of shapes the user has access to in any given document. As a result of this, some remaining shapes had to be manually placed later via MS Paint, which slightly upset the visual uniformity of the chart.

The chart is provided below; white shapes represent neutral choices. Green shapes represent correct pathways through the apps, whereas red shapes represent dead-ends where the user loses. Blue shapes represent "stun-conditions", where the user is bound to fail but presented with another narrative beat.

### Image of the Chart
![Lucid Chart](assets/readme-images/cellar-flowchart.webp)

# Features
## Txt Files
The narrative of the adventure is stored under assets in txt files. By doing so, a function to read the text could be declared and then called throughout the code in order to relay the narrative to the user without crowding the code itself. This also allowed for ASCII art to be implemented in order to provide visual flair for the title, "lose" screen and "win" screen.

## Narrative Framing
The narrative is presented to the user as the guiding comments of a nameless entity. Though showing clear enjoyment in the user’s "predicament", there are moments in which it seems that the narrator is rooting for the user. Text as provided by the narrator uses colorama in order to present it as purple. Red was considered but was ultimately decided against as it evoked the feeling of a "horror" story which, though similar, this story is not.

All text being read from the txt files is presented with time delays in order to provide the narrative line by line and avoid cluttering the terminal to the degree that the user is confused as to where the current text begins and the previous text ends. 

## Error Handling

The user’s choice selection is presented as standard white text. Visually, this not only provides narrative breaks for the user, but also distances the input request text from that of the narrator. All inputs except for the username input expect an integer, either 1 or 2, or 1, 2 or 3. In the event of the user inputting either an incorrect integer or a string of letters, an error message is printed to the console and the current function restarts. In this way, the narrative continues with all prior selections still marked and the provided username at the beginning of the app remains stored.

Below are examples of how input errors are handled.

### Image of Incorrect Integer Input
![Incorrect Integer](assets/readme-images/wrong-number-input.webp)

### Image of Letters Input
![Letters Input](assets/readme-images/word-input.webp)

## Name input
Upon initiation the app requests a username from the user. This username is stored and recalled upon a "win" or "loss" condition. Should the user fail or succeed and then decide to replay, the name input is skipped as the previously entered name remains stored. Only by refusing replay or restarting the app will the user be asked to re-enter a name.

Once given, a brief message confirms the name to the user and then proceeds with the adventure.

In terms of narration, the name is requested by the nameless entity, who then "steals" it and promises the user they can have it back if they succeed. The name is indeed returned upon success; in the event of failure, the nameless entity eats the name. This narrative feature was inspired by Hayao Miyazaki's film "Spirited Away", in which a young girls name is commandeered by a witch and held as collateral until she satisfies the conditions of a work contract in order to release her parents.

Below are images showing how username input is handled by the app.

### Image of Name Request
![Name Request](assets/readme-images/name-request.webp)

### Image of Name Inputted
![Name Input](assets/readme-images/name-documented.webp)

## Title and Intro
Next, the user is shown the title card for the app along with an introductory passage to inform them of the narrative framing. Here, the user is asked whether they wish to proceed with the game. If accepted, the narrator commends their bravery and the game continues. Upon refusal, the narrator sarcastically tells the user to enjoy remaining stationary in the cellar and the app is exited.

Below are images of the title card and how the app responds when the user does not wish to play the game.

### Image of Title and Intro
![Title and Intro](assets/readme-images/title-intro.webp)

### Image of Play Refusal
![Play Refused](assets/readme-images/refuse-play.webp)

## Path Selection
If the user agrees to play, they are provided with a selection of pathway. There are two to choose from; one which leads upstairs and another that leads downstairs. It is possible to succeed regardless of which pathway you select here. 

Below is an image of how the path selection is presented to the player.

### Image of Play Acceptance and Path Selection
![Play Accepted](assets/readme-images/accept-play-path.webp)

## Story Advancement
Throughout the game, selecting the correct option will advance the story and move the user through the cellar. When the user makes a decision, the narrator clearly informs the user whether they have been successful or not. This provided text remains aligned with the general narrative and how it has thus far been presented. The code provides gaps in order to segregate the narrative beats and provide a visual sense of progression.

Below is an example of the correct selection being made and the story advancing.

### Image of Story Advancing
![Story Advances](assets/readme-images/story-advance.webp)

## Stun conditions
On most floors of the cellar, the user is greeted by a monster and asked to react. Many of these have three options instead of two; the third option leads to a "stun condition". These are humorous developments that provide tongue-in-cheek text and a further binary choice for the user. In all stun conditions, the user’s selection leads to failure. They have been included in order to provide a bit of levity and also to instil hope in the already doomed player.

Below are images showing an example of a stun condition, how it is narratively handled and how it proceeds to failure.

### Image of Three Choice Selection
![Three Choices](assets/readme-images/three-choice.webp)

### Image of a Stun condition
![Stun Condition](assets/readme-images/stun-choice.webp)

### Image of Failure Following Stun Condition
![Stun Failure](assets/readme-images/stun-kill.webp)

## Fail Condition
In the event of failure, the user is greeted with another ASCII title, followed by a short piece of text in which the nameless entity permanently consumes the users name. They are then offered the option to replay the game, along with specific text that refers to the user’s failure in escaping. If they accept, the app returns to the title screen and begins the game again, with the previously entered username still stored. If the player refuses, the nameless entity accuses the user of cowardice and the app is exited.

Below are images of the fail title, the user being offered a replay and what is returns if users reject the replay option.

### Image of Fail Title
![Fail Title](assets/readme-images/lose-name.webp)

### Image of Replay on Failure
![Fail Replay](assets/readme-images/replay.webp)

### Image of Text on Replay Refused
![Replay Refused](assets/readme-images/replay-refuse.webp)

## Win Condition
In the event of success, the user is presented with another ASCII title, followed by a short piece of text in which the nameless entity returns the users name. They are then offered the option to replay the game, along with specific text that refers to the user’s success in escaping. If they accept, the app returns to the title screen and begins the game again, with the previously entered username still stored. If the player refuses, the nameless entity accuses the user of cowardice and the app is exited.

Below are images of the win title and how a replay request is presented to the user should they have succeeded in escaping the cellar.

### Image of Win Title
![Win Title](assets/readme-images/win-name.webp)

### Image of Replay on Success
![Success Replay](assets/readme-images/win-replay.webp)

# Abandoned Features
## Weapons
Early planning for the app included an inventory for the user which they could fill with weapons as the story progressed. Abandoned quite quickly, this feature was deemed unwieldy in the scope of this specific project as the included monsters tend to have universal lores that would require specific means of defeating them. It would also require that floors be inserted where the user merely selects a weapon as the intention was to have "dud" weapons that ensured failure. To avoid project bloat and to maintain a realistic scope, the feature was abandoned.

## Multiple Adventures
Multiple adventures were briefly considered, allowing the user to choose their storyline. Three stories were brainstormed and during this process it became clear that each story would be hindered due to the three different narratives. Instead, the preferred elements from each story were consolidated into one and the "Escape the Cellar" storyline was selected as the optimal framework to explore the ideas that emerged during the brainstorming process.

## Progress Tracker
The implementation of a tracker was considered to allow the user to keep track of their successes and failures throughout their attempts. However, fears that this would allow users to mentally plot the pathways of the game resulted in the feature being removed from considerations.
 
# Features Earmarked for Future Implementation
The following features are intended to be implemented at a future date.

## Expanded Narrative
More floors and pathways have been earmarked for future development in order to expand the scope of the app. Due to project deadlines, these could not be implemented sooner.

## Asymmetrical Plotting
As visible in the plotting chart above, the two pathways in the adventure are symmetrical with one another in how they proceed. This allowed for a seamless flow throughout the planning and implementation stages, though it has been noted that some users may be able to identify the pattern upon repeat plays and essentially "gamify" the experience. Though not entirely likely considering how the narrative is presented, it is a noted issue which could be addressed with asymmetrical design should the narrative be expanded.

## Further implementation of ASCII
The visual effect of ASCII art provides much needed flair to the narrative. Used sparingly in order to not clutter the terminal, means of implementing more ASCII art in a way which does not do this are under consideration and were earmarked for future implementation when the current workload was compared to the alotted time for completing the app.

## Multiple Adventures
As noted under abandoned features, the possibility of several adventures being offered to the user is one under serious consideration. Once the future implementations for Escape the Cellar have been put in place, the scope of the app can increase and allow for further adventures, perhaps ones that intertwine. First in line would perhaps be an Escape the Forest adventure, which would pick up from the moment the user escaped the cellar. However, it is noted that this may limit the user’s ability to select their adventure as one flows narratively from the other.

# Testing
## User Stories Testing
* As a user, I want to play an interactive game that requires no downloads or installations

The app runs as intended, providing an interactive experience that can be played in the user’s browser.

* As a user, I want to receive clear instructions and choices from the app

The narrative of the game provides clear guidance and options to the narrator.

* As a user, I want my inputted data to be handled correctly and to return advancement in the "adventure"

The app accepts user input and handles it appropriately, advancing, passing or failing the user where necessary and returning error messages that inform the user of any inaccuracy. In the event of an error, the user is able to continue the game without losing their prior progress.

* As a user, I want to be offered the chance to play again should I win or lose

Whether the user fails or succeeds, the app offers the option to replay the game and keeps the entered username stored.

* As a user, I want to replay the app and reasonably expect a varied experience

The app contains branching pathways that lead to different scenarios and provide the user with a varied experience on replay.

## Validator Testing
### Pylint
The Pylint score initially returned a rating of roughly seven (exact figure undocumented). Through code correction, it was possible to increase the score to 9.83. Two issues remained.

The first is for using the global statement. Worried that changing this would affect the storage and recall of the username later in the app, various articles were consulted on the nature of the issue. It was decided that within the scope of this project it was safe to leave it as is, though it has been noted as an issue for further builds.

Secondly, the "stun-condition" input choices would always evaluate to 2 as they led to the same narrative beat regardless of user selection. As those choices exist purely as "false-hope" scenarios and always result in a failure, it was decided to leave them as was and to figure out a way of sidestepping the issue in future builds.

Below is an image of the Pylint score.

#### Image of Pylint Score
![Pylint Score](assets/readme-images/pylint-score.webp)

### Code Institute Python Linter
The entirety of the code was run through the Code Institute Python Linter and returned a variety of issues. These included the following:
* Line length issues
*  Trailing lines
*  Missing or unnecessary spaces
*  The unnecessary usage of "return" in several functions
*  A suggestion to replace exit() with sys.exit()
*  An issue with the function that accessed, printed and closed txt files.

All of these issues were addressed, with consulted texts listed under credits. Below is an image of the final CI Python Linter score.

#### CI Python Linter Score
![CI Linter](assets/readme-images/ci-python-linter.webp)

## Bugs
Manual testing yielded few issues, as did reports from invited testers. All known bugs except for one were addressed and corrected throughout the coding process.

The unaddressed bug was detected by a tester. It is an issue during the "stun condition" portions of the narrative, where the user is giving a choice between two options that both lead to failure, as documented above. When the app requests the user’s choice, it does not return an error for putting in the wrong input. 

Whether the input was an incorrect integer or a string of letters, the app would automatically advance the user to the next narrative beat, which regardless of selection would always be failure. This issue was detected quite late in the process and various sources were consulted to identify the cause. It is presumed to be directly linked to the issue described under "Pylint" above.

Fortunately, as the user is "locked in" to a lose condition by the time the issue arises, it does not break the users experience, though there is worry that as it leads to failure as intended, it may be misinterpreted as a game-breaking bug by some users.

The issue could not be ironed out due to project deadlines. However, it has been noted as a major issue to be addressed in future builds.

# Deployment
Deployment required an Heroku account to host the app. Once an account was created, the following steps were followed:
* From the Heroku dashboard, select new in the upper right corner, followed by create new app.
* Enter an appropriate app name and select region, which was EU in this case.
* Select Create New App
* Under settings, select Reveal Config Vars. Enter PORT as a key with 8000 as the value and then add.
* Scroll to buildpacks and add Python then Node.js for dependencies. Ensure they are added in that order.
* Return to deployment and select deployment method which was GitHub in this case.
* Enter the relevant repository source and connect.
* Select deploy from branch which provided a landing page on Heroku for your app.
* In the top right, select "Open App" to launch in a new window

# Credits
## Written Reference Sources
The following forum posts were consulted in constructing the title_read and read_stroylines functions:
* https://stackoverflow.com/questions/24292806/how-can-i-pass-a-txt-file-as-a-function-parameter
* https://www.reddit.com/r/learnpython/comments/x1rt5n/i_have_pylint_errors_please_help/

The following websites were consulted throughout and proved invaluable:
* https://stackoverflow.com
* https://pieriantraining.com/
* https://www.shecodes.io/
* https://realpython.com/
* https://www.learnpython.org/

## Video Reference Sources
The following YouTube channels were consulted during the planning stages of the project:
* https://www.youtube.com/@Baober
* https://www.youtube.com/@TezFraser
* https://www.youtube.com/@TechWithTim

## Learning Materials
The learning materials, video tutorials and modules provided by Code Institute were consulted regularly during the project.

## Text Content
The riddles used in-game were sourced from the following article: 
* https://www.playosmo.com/kids-learning/riddles-for-kids/

The ASCII were generated using the following website:  
* https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

Colorama was used for styling the text in the terminal

All spellchecks for both text content and the readme were performed on Microsoft Word

All other text content written by AdamFcode

## Other
Microsoft Paint was used to expand/edit the Lucid Chart image.

The Code Institute Python Linter was used to verify Pep8 adherence.

Gitpod and GitHub were used in tandem to host the repository and write the code.

Heroku was used for deployment, as outlined above.

# Acknowledgement
With appreciation for aid lent by the project mentor and class CI provided by codeinstitue, as well as fellow students in the slack channel.
