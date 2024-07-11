from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_huggingface import HuggingFaceEndpoint

import os

huggingface_api = os.getenv('HUGGINGFACE_API_KEY')

# Define the Hugging Face model endpoint

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, temperature=0.6, token=huggingface_api, max_length=40)


def generate_restaurant_name(cuisine):
    # Template for generating restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="Suggest me  a restaurant name for a {cuisine} restaurant.Strictly only return the first name,no excess information "
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Generate restaurant name
    response = name_chain({'cuisine': cuisine})

    return response['restaurant_name']


def generate_restaurant_name_and_menu_items(cuisine):
    # Template for generating menu items
    restaurant_name = generate_restaurant_name(cuisine)
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest menu items for {restaurant_name}."
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Generate menu items
    response = food_items_chain({'restaurant_name': restaurant_name})

    return {'restaurant_name': restaurant_name
        , 'menu_items': response['menu_items']}


if __name__ == "__main__":
    cuisine = "italian"

    # Generate restaurant name
    restaurant_name = generate_restaurant_name(cuisine)
    print("Restaurant Name:", restaurant_name)

    # Generate menu items
    menu_items = generate_restaurant_name_and_menu_items(cuisine)
    print("Menu Items:", menu_items)
