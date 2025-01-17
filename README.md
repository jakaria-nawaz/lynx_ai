# AIKA (AI Kitchen Assistant)

Are you tired of the same old meal planning routine that leaves you feeling uninspired and frustrated? Do you find yourself throwing out food that has gone bad because you don't know what to do with it? Say goodbye to these kitchen woes and hello to **AIKA** - the ultimate kitchen management app!

**AIKA** is a game-changer for anyone who wants to eat healthy, delicious meals without the hassle of figuring out what to cook. It uses cutting-edge technology, such as **Redis** as its database and the powerful **OpenAI GPT-3** API, to generate personalized recipes based on your inventory and preferences. Plus, with the app's smart shopping list feature, you'll never have to worry about buying unnecessary groceries again.

Imagine being able to take a quick photo of your grocery receipt or inputting your inventory manually and having **AIKA** do the rest. The app learns your usage patterns and creates customized shopping lists and recipe suggestions that fit your lifestyle. And with the ability to save your favorite recipes in a beautifully-designed blog-style interface, you'll have access to meal ideas that are both tasty and visually appealing.

Whether you're a student on a budget, a busy professional, or a weekend commuter, **AIKA** is the kitchen management app you never knew you needed. It's the perfect solution for anyone who wants to simplify their meal planning routine, reduce food waste, and save time and money in the kitchen.

## Key Features

### Recipe Generation

- The system will leverage AI-powered algorithms (namely OpenAI GPT-3) to analyze the user's input and generate a dish to cook. 
- The application will also provide a list of required ingredients from the inventory and the cooking procedure.

### Inventory Management

- Add your grocery inventory either by taking a photo of cash memos or manually inputting your inventory. 
- The user will have the option to accept or reject the recipe suggestion. If the user selects and prepares a generated recipe, the inventory will be automatically be updated based on the amount of ingredients used.

### Smart Shopping Lists

- The application will utilize predictive analytics to track the user's grocery consumption patterns and notify the user when it is time to go shopping again. 
- The application can also generate a list of grocery items that are running low in the inventory, allowing the user to replenish their supplies proactively.

### Favorite Recipe Storage

- Users can save their favorite recipes generated, and they get saved in a separate page with beautiful images generated from OpenAI Dall-E in a blog-style interface, so the user can get back to them whenever they want.

## Deployment

The app is currently deployed using Streamlit [here](https://lynx-kitchen-inventory-recipe.streamlit.app/).

## Technologies Used

### [Redis](https://redis.io/)

Redis is an open-source, in-memory key-value data store that can be used as a database, cache, and message broker.

### [OpenAI API](https://platform.openai.com/docs/introduction)

OpenAI GPT-3 API is a cloud-based artificial intelligence platform that provides access to state-of-the-art language models, including GPT-3 and LLMs.

### [OpenAI Dall-E](https://openai.com/dall-e/)

OpenAI Dall-E is a neural network-based image generation API that can generate images from textual descriptions.

## Future Improvements

- We plan to create a mobile app version of AIKA for easier access on the go.
- We plan to integrate **OpenAI Whisper** to add voice commands to the app. 

## Hackathon Details

AIKA is being developed as part of the **OpenAI Stack Hack**, organized by [Lablab.ai](Lablab.ai), a hackathon that challenges participants to create innovative applications using generative AI. The hackathon took place from February 24th to March 3rd, 2023. You can learn more about the hackathon [here](https://lablab.ai/event/openai-hackathon).

For more information on our project, please refer to our pitch presentation using the link provided.

Feel free to reach out to us for any feedback or suggestions!
