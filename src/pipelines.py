from modelscope.pipelines import pipeline

pipelineK = pipeline('text-generation', model='./models/k')

k = lambda v: pipelineK(v)['text']