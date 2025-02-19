from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

from pydantic_ai.models.gemini import  GeminiModelName, LatestGeminiModelNames
from pydantic_ai.models.openai import  ChatModel
from pydantic_ai.models.groq import  GroqModelName
from pydantic_ai.models.anthropic import  LatestAnthropicModelNames

from ..groq_utils import list_models
from ..open_router import list_models as list_openrouter_models

import os

from ..conversation_models import LLMProvider, ListModelsResponse

def get_model(provider: str, model: str = None):
    if provider == 'openai':
        if model is None:
            model = 'o1-mini'
        return f'openai:{model}'
    elif provider == 'anthropic':
        if model is None:
            model = 'claude-3-5-haiku-latest'
        return f'anthropic:{model}'
    elif provider == 'groq':
        if model is None:
            model = 'gemma2-9b-it'
        return f'groq:{model}'
    elif provider == 'google':
        if model is None:
            model = 'models/gemini-1.5-flash'
        return f'google-gla:{model}'
    elif provider == 'openrouter':
        # TODO: check if this is the correct way to do it
        if model is None:
            model = 'gryphe/mythomax-l2-13b:free'
        return OpenAIModel( model, base_url='https://openrouter.ai/api/v1', api_key=os.getenv('OPENROUTER_API_KEY'))
    else:
        raise ValueError(f'Provider {provider} not supported')
    

def get_model_names(provider: LLMProvider) :
    if provider == LLMProvider.OpenAI:
        names = ChatModel.__args__
        return [ListModelsResponse(name=name, id=name) for name in names]
    elif provider == LLMProvider.Google:
        # models = genai.list_models()
        # gemini_models = [{**model.__dict__, 'id': model.name} for model in models if 'gemini' in model.name.lower()]
        # return  gemini_models
        names = LatestGeminiModelNames.__args__
        return [ListModelsResponse(name=name, id=name) for name in names]
    elif provider == LLMProvider.OpenRouter:
        models = list_openrouter_models()
        return models
    elif provider == LLMProvider.Groq:
        models = list_models()
        return [ListModelsResponse(name=name, id=name) for name in models]
    elif provider == LLMProvider.Anthropic:
        names = LatestAnthropicModelNames.__args__
        return [ListModelsResponse(name=name, id=name) for name in names]
    else:
        raise ValueError(f"Provider {provider} not supported")
