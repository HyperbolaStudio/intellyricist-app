from generationLogging import logger
from modelscope.pipelines import pipeline
from typing import Callable, Dict

pipelineK = pipeline('text-generation', model='./models/k')
pipelineP = pipeline('text-generation', model='./models/p')

def pipelineWrapper(pipelineFunction: Callable[[str], dict[str, str]]):
    def _(prompt: str):
        logger.info('[Prompt] %s', prompt)
        s = pipelineFunction(prompt)['text']
        logger.info('[Generation] %s', s)
        return s
    return _

k = pipelineWrapper(pipelineK)
p = pipelineWrapper(pipelineP)