from __future__ import annotations

from mteb.abstasks import AbsTask
from mteb.abstasks.aggregated_task import AbsTaskAggregate, AggregateTaskMetadata
from mteb.tasks.Retrieval import (
    CQADupstackAndroidNLRetrieval,
    CQADupstackEnglishNLRetrieval,
    CQADupstackGamingNLRetrieval,
    CQADupstackGisNLRetrieval,
    CQADupstackMathematicaNLRetrieval,
    CQADupstackPhysicsNLRetrieval,
    CQADupstackProgrammersNLRetrieval,
    CQADupstackStatsNLRetrieval,
    CQADupstackTexNLRetrieval,
    CQADupstackUnixNLRetrieval,
    CQADupstackWebmastersNLRetrieval,
    CQADupstackWordpressNLRetrieval,
)

task_list_cqa: list[AbsTask] = [
    CQADupstackAndroidNLRetrieval(),
    CQADupstackEnglishNLRetrieval(),
    CQADupstackGamingNLRetrieval(),
    CQADupstackGisNLRetrieval(),
    CQADupstackMathematicaNLRetrieval(),
    CQADupstackPhysicsNLRetrieval(),
    CQADupstackProgrammersNLRetrieval(),
    CQADupstackStatsNLRetrieval(),
    CQADupstackTexNLRetrieval(),
    CQADupstackUnixNLRetrieval(),
    CQADupstackWebmastersNLRetrieval(),
    CQADupstackWordpressNLRetrieval(),
]


class CQADupstackNLRetrieval(AbsTaskAggregate):
    metadata = AggregateTaskMetadata(
        name="CQADupstack-NL",
        description="CQADupStack: A Benchmark Data Set for Community Question-Answering Research. This a "
        "Dutch-translated version.",
        reference="https://huggingface.co/datasets/clips/beir-nl-cqadupstack",
        tasks=task_list_cqa,
        main_score="ndcg_at_10",
        type="Retrieval",  # since everything is retrieval - otherwise it would be "Aggregated"
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["nld-Latn"],
        date=("2024-10-01", "2024-10-01"),
        domains=["Written"],
        task_subtypes=[],
        license="apache-2.0",
        annotations_creators="LM-generated and reviewed",
        dialect=[""],
        sample_creation="machine-translated and verified",
        bibtex_citation="""@misc{banar2024beirnlzeroshotinformationretrieval,
    title={BEIR-NL: Zero-shot Information Retrieval Benchmark for the Dutch Language}, 
     author={Nikolay Banar and Ehsan Lotfi and Walter Daelemans},
     year={2024},
     eprint={2412.08329},
     archivePrefix={arXiv},
     primaryClass={cs.CL},
     url={https://arxiv.org/abs/2412.08329}, 
}""",
    )
