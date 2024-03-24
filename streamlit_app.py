import streamlit as st
import pandas as pd

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyDGjSjvHDdDXARxMR3yOybRFll2SeQc4AI")

model = genai.GenerativeModel('gemini-pro')



prompt = "Given this list of ingredients,and allergens to avoid, can you generate 15 recipes for me? Can you give me steps to each recipie as well in one large block. Note: if there is an allergen involved, make sure none of the recipies you suggest involve it. Also, next to each recipe make a note of what allergens it avoids."
ingredients = "Ingredients: eggs, milk, cheese, butter, yogurt, lettuce, tomatoes, cucumber, carrots, onions, bell peppers, chicken, beef, pork, fish, shrimp, mayonnaise, ketchup, mustard, pickles, bread, pasta, rice, potatoes, garlic, ginger, lemon"
allergens = "Allergens: Peanuts, Vegan"


response = model.generate_content(
    prompt + allergens + ingredients
)
print(response.text)

# Display the current inventory
st.title('Receipes')
st.write(response)
