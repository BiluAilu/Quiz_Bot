### Telegram Bot Project ###
## Overview ##
The Quiz Bot is a Telegram bot designed to provide users with an interactive quiz-taking experience. Users can explore a variety of quizzes based on different categories and difficulty levels, evaluate their knowledge, and challenge themselves to improve their scores. The bot also introduces a collaborative element, allowing users to contribute new quiz questions and share them with the community after approval by administrators.

## Key Features ##
* Quiz Taking: Users can choose quizzes based on their preferred category and difficulty level, answering questions to evaluate their knowledge and receive instant feedback on their performance.

* Question Contribution: The bot empowers users to create and submit new quiz questions. These questions undergo an approval process by administrators before becoming part of the quiz pool.

* Score Tracking: Users can track their quiz scores over time, providing a competitive and motivational element to encourage continuous learning.

* Community Engagement: The bot fosters a sense of community by allowing users to share their favorite quizzes and challenge others to beat their scores.

* Administrative Approval: To maintain quiz quality, administrators have the authority to review and approve submitted questions before they are made available to the wider audience.


## Target Audience ##
The Quiz Bot is ideal for individuals who enjoy testing their knowledge, learning new facts, and engaging in friendly competition with others. Whether users are looking for a quick brain teaser or a comprehensive quiz on a specific topic, the bot offers a diverse range of quizzes to cater to different interests and proficiency levels.

## Technology Stack ##
The Quiz Bot is built using Python and leverages the Aiogram library for Telegram bot development. It utilizes a state machine to manage user interactions and MongoDB for data storage. MongoDB serves as the database to store persistent user information, quiz data, and user-submitted questions.

## Goals ##
Provide an engaging and educational experience for users interested in quizzes.
Foster a collaborative community where users can contribute and share quiz questions.
Maintain a high standard of quiz quality through an approval process.
Encourage continuous learning and friendly competition among users.

## Prerequisites ##
* Python 3.11
* Packages that are inside **requirement.txt** file

## Installation ##
1. Clone the repository:
```
git clone https://github.com/BiluAilu/Quiz_Bot.git
```
2. Navigate to the project directory
```
cd Quiz_Bot
```
3. Install dependencies
```
pip install -r requirements.txt
```


## Configuration ##
1. Obtain a Telegram Bot API Token from the BotFather on Telegram.


2. Create a .env file in the project root and add your telegram API token and your Mongodb database url
```
TOKEN="You telegram bot token"
MONGO_URL="you mongodb url"
```

## Usage ##
Run the bot using the following command:

```
python main.py

```





## Contributing
We welcome contributions to improve the functionality and features of this bot. If you would like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request.


