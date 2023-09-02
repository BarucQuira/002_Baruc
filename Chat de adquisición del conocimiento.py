# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 11:50:02 2023

Módulo de adquisición del conocimiento

Baruc Gutiérrez Quirarte - 7F1 
Sistemas Expertos

@author: DELL
"""

from difflib import get_close_matches
import json

def get_best_match(user_question: str, questions: dict) -> str | None:
    """Compara la similitud del mensaje del usuario con los del diccionario"""

    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    # Devuelve la primera mejor coincidencia; en caso contrario, devuelve Ninguno
    if matches:
        return matches[0]

def chatbot(knowledge: dict, knowledge_file: str):
    """Chatbot"""

    while True:
        user_input: str = input('T\u00fa: ')

        # Encontrar la mejor coincidencia; de lo contrario, devuelve Ninguno
        best_match: str | None = get_best_match(user_input, knowledge)

        # Obtener la mejor coincidencia de la base de conocimientos
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: No se la respuesta a la pregunta... Podrias decirmela, para enseñarme a responderla?')
            new_answer = input('T\u00fa: ')

            if best_match:
                knowledge[best_match] = new_answer
            else:
                print('Bot: Perfecto, ya he aprendido a responder la frase anterior')
                original_question = user_input
                knowledge[original_question] = new_answer

            # Guardar la base de conocimientos actualizada en un archivo
            with open(knowledge_file, 'w') as file:
                json.dump(knowledge, file, indent=4)

if __name__ == "__main__":
    knowledge_file = 'knowledge_base.json'
    
    try:
        with open(knowledge_file, 'r') as file:
            brain = json.load(file)
    except FileNotFoundError:
        brain = {'hola': 'que rollo!',
                   'como estas?': 'Estoy bien, gracias!',
                   'que puedes hacer?': 'Puedo responder preguntas y aprender a contestarlas!, intentalo, de que quieres hablar? ',
                   'ok': 'genial.'}

    chatbot(knowledge=brain, knowledge_file=knowledge_file)
