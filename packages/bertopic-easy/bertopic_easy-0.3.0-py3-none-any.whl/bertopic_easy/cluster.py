from __future__ import annotations

import asyncio
import json
from collections import defaultdict
from pathlib import Path
from typing import Literal, Optional, Union

from loguru import logger

logger.debug(
    "Importing BERTopic takes a while... see the BERTopic library's FAQ for more info"
)
from bertopic import BERTopic
from loguru import logger
from openai import AsyncAzureOpenAI, AzureOpenAI
from pydantic import BaseModel, Field
from rich import print
from rich.console import Console
from rich.theme import Theme

from bertopic_easy.embedding import embed
from bertopic_easy.models import Clusters, LabeledDoc

custom_theme = Theme({"info": "dim cyan", "warning": "magenta", "danger": "bold red"})
console = Console(theme=custom_theme)


def cluster(
    *,
    bertopic_kwargs: dict,
    docs: list[str],
    openai: Union[AzureOpenAI, OpenAI],
    embed_llm_name: str,
    with_disk_cache: bool,
) -> Clusters:
    topic_model = BERTopic(**bertopic_kwargs)
    embeddings = embed(
        texts=docs,
        openai=openai,
        llm_model_name=embed_llm_name,
        with_disk_cache=with_disk_cache,
    )
    topics, probs = topic_model.fit_transform(docs, embeddings=embeddings)
    if topics is None or probs is None:
        raise ValueError("No topics or probs found")
    labeled_docs = [
        LabeledDoc(doc=doc, label=label, prob=prob)
        for doc, label, prob in zip(docs, topics, probs)
    ]
    clusters = defaultdict(list)
    for labeled_doc in labeled_docs:
        clusters[int(labeled_doc.label)].append(labeled_doc)
    clusters = Clusters(
        clusters=clusters,
        bertopic_kwargs=bertopic_kwargs,
        embedding_llm_name=embed_llm_name,
    )
    return clusters
