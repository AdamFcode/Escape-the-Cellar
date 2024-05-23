# Escape the Cellar
Escape the Cellar is a python-based text adventure that challenges the user to escape a cellar that they have been imprisoned in by a formless entity. This entity serves as the narrator and leads the user through a sequence of challenges that require choices to be made by the user. The game has several points at which the user can "fail" and be offered the chance to try again. There are only two means of escaping, each requiring the user to successfully navigate through the choices until they reach the end.

The deployed site can be accessed from here:[Escape the Cellar](https://escape-the-cellar-de7d0d9c5297.herokuapp.com/)

# Preparation
In preperation for this project, multiple websites and videos were consulted, as well as several "text-adventure" books, particularly from the "Goosebumps" series. These were studied to get an intuitive understanding of how such adventures are typically constructed.

The flow of the adventure was planned out using Lucidchart, allowing for the two 'pathways' to be concisely illustrated. Provided in the relevant section below, this chart helped immensely in organising and visualising the flow of the project's functions and choices. 

Once the initial preparation was complete, potential "testers" were consulted in order to get an understanding of what they would expect from a text-adventure game.

## User Stories
* As a user, I want to play an interactive game that requires no downloads or installations
* As a user, I want to receive clear instructions and choices from the app
* As a user, I want my inputted data to be handled correctly and to return advancement in the "adventure"
* As a user, I want to be offered the chance to play again should I win or lose
* As a user, I want to replay the app and reasonably expect a varied experience

The above will be adressed under Testing below.

## LucidChart
LucidChart was selected to visualise the flow of the adventure and to provide a visual guide to reference when writing the code. The free version of LucidChart was used which limits the number of shapes the user has access to in any given document. As a result of this, some remaining shapes had to be manually placed later via MS Paint, which slightly upset the visual uniformity of the chart.

### Image of the Chart
![LucidChart](assets/readme-images/cellar-flowchart.webp)

# Features
## Txt Files
The narrative of the adventure is stored under assets in txt files. By doing so, a function to read the text could be declared and then called throughout the code in order to relay the narrative to the user without crowding the code itself. This also allowed for ASCII art to be implemented in order to provide visual flair for the title, "lose" screen and "win" screen.

## Name input
Upon initiation the app requests a username from the user. This username is stored and recalled upon a "win" or "loss" condition. Should the user fail or succeed and then decide to replay, the name input is skipped as the previously entered name remains stored. Only by refusing replay or restarting the app will the user be asked to reenter a name.

In terms of narration, the name is requested by the nameless entity, who then "steals" it and promises the user they can have it back if they succeed. The name is indeed returned upon success; in the event of failure, the nameless entity eats the name. This narrative feature was inspired by Hayao Miyazaki's film "Spirited Away", in which a young girls name is comandeered by a witch and held as collateral until she satisfies the conditions of a work contract in order to release her parents.

### Image of Name Request
![Name Request](assets/readme-images/name-request.webp)

# Abandoned Features

 
# Features Earmarked for Future Implementation
The following features are intended to be implemented at a future date.



# Testing

## User Stories Testing

## Validator Testing

## Bugs

# Deployment

# Credits
## Written Reference Sources


## Video Reference Sources


## Learning Materials
The learning materials, video tutorials and modules provided by codeinstitute were consulted regularly during the project.

## Text Content

# Acknowledgement
With appreciation for aid lent by the project mentor and class CI provided by codeinstitue, as well as fellow students in the slack channel.
