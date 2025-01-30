from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class FEVERNL(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="FEVER-NL",
        dataset={
            "path": "clips/beir-nl-fever",
            "revision": "ee0f58854a2555a8e666a3b248a8f9e856568785",
        },
        description=(
            "FEVER (Fact Extraction and VERification) consists of 185,445 claims generated by altering sentences"
            + " extracted from Wikipedia and subsequently verified without knowledge of the sentence they were"
            + " derived from. FEVER-NL is a Dutch translation."
        ),
        reference="https://huggingface.co/datasets/clips/beir-nl-fever",
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["nld-Latn"],
        main_score="ndcg_at_10",
        date=("2024-10-01", "2024-10-01"),
        domains=["Encyclopaedic"],
        task_subtypes=[],
        license="cc-by-4.0",
        annotations_creators="LM-generated and reviewed",
        dialect=[],
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
