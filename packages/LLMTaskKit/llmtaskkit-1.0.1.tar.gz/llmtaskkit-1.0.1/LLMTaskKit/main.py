# main.py
import logging
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from LLMTaskKit.core.task import Task, load_raw_tasks_from_yaml
from LLMTaskKit.core.llm import LLMConfig
from LLMTaskKit.prompt_chain import TaskChainExecutor
from LLMTaskKit.example.meeting_summary import MeetingSummary
from LLMTaskKit.example.prompt_finetuner import PromptFintuner

class Summary(BaseModel):
    summary: str
class Response(BaseModel):
    response: str

def chain_test():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    load_dotenv()
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    llm = LLMConfig(api_key=gemini_api_key, model="gemini/gemini-exp-1206")

    # Chargement des tâches brutes depuis le YAML
    raw_tasks = load_raw_tasks_from_yaml("./LLMTaskKit/tasks.yaml")

    # Création des tâches en surchargeant éventuellement output_format et llm
    task_demo = Task.from_raw(raw_tasks["TacheDemo"], output_pydantic=Response, assistant_prefill="<brainstorm>\n")
    task_suivante = Task.from_raw(raw_tasks["TacheSuivante"], output_pydantic=Summary, forced_output_format="json")

    tasks_finales = [task_demo, task_suivante]

    # Contexte initial (exemple)
    initial_context = {
        "name": "john",
        "familly": {
            "wife": "Elisabeth",
            "children": ["Esmee", "Eddy"]
        }
    }

    # Création de l'executor avec verbose activé pour voir les détails
    executor = TaskChainExecutor(llm, verbose=True, step_by_step=True)
    executor.execute(tasks_finales, initial_context)


    initial_context = {**executor.context}
    print(f'initial_context : {initial_context}')
    print(f'initial_context : {initial_context["TASK_RESULT"]["TacheDemo"]}')

    logging.info("Contexte final :")
    logging.info(executor.context)
    logging.info("Résultat de la dernière tâche :")
    logging.info(executor.result)
    input('Wait')

def meeting_summary():
    MeetingSummary().exec()


def pimpt_prompt():
    # créé une annotation en java, l'ecosystem c'est quarkus et j'aimerai que l'annontation permette de catch les exception, et d'envoyer un mail via MailService.send au mail défini dans la properties alert.mail
    PromptFintuner().exec()


if __name__ == "__main__":
    #chain_test()
    pimpt_prompt()
    #meeting_summary()

# TODO : 
# https://github.com/anthropics/courses/blob/master/real_world_prompting/01_prompting_recap.ipynb