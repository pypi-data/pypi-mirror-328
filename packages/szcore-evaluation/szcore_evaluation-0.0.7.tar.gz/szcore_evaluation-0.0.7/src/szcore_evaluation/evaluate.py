import json
from pathlib import Path

from epilepsy2bids.annotations import Annotations
import numpy as np
from timescoring import scoring
from timescoring.annotations import Annotation


class Result(scoring._Scoring):
    """Helper class built on top of scoring._Scoring that implements the sum
    operator between two scoring objects. The sum corresponds to the
    concatenation of both objects.
    Args:
        scoring (scoring._Scoring): initialized as None (all zeros) or from a
                                    scoring._Scoring object.
    """

    def __init__(self, score: scoring._Scoring = None):
        if score is None:
            self.fs = 0
            self.duration = 0
            self.numSamples = 0
            self.tp = 0
            self.fp = 0
            self.refTrue = 0
        else:
            self.fs = score.ref.fs
            self.duration = len(score.ref.mask) / score.ref.fs
            self.numSamples = score.numSamples
            self.tp = score.tp
            self.fp = score.fp
            self.refTrue = score.refTrue

    def __add__(self, other_result: scoring._Scoring):
        new_result = Result()
        new_result.fs = other_result.fs
        new_result.duration = self.duration + other_result.duration
        new_result.numSamples = self.numSamples + other_result.numSamples
        new_result.tp = self.tp + other_result.tp
        new_result.fp = self.fp + other_result.fp
        new_result.refTrue = self.refTrue + other_result.refTrue

        return new_result

    def __iadd__(self, other_result: scoring._Scoring):
        self.fs = other_result.fs
        self.duration += other_result.duration
        self.numSamples += other_result.numSamples
        self.tp += other_result.tp
        self.fp += other_result.fp
        self.refTrue += other_result.refTrue

        return self


def evaluate_dataset(
    reference: Path, hypothesis: Path, outFile: Path, avg_per_subject=True
) -> dict:
    """
    Compares two sets of seizure annotations accross a full dataset.

    Parameters:
    reference (Path): The path to the folder containing the reference TSV files.
    hypothesis (Path): The path to the folder containing the hypothesis TSV files.
    outFile (Path): The path to the output JSON file where the results are saved.
    avg_per_subject (bool): Whether to compute average scores per subject or
                            average across the full dataset.

    Returns:
    dict. return the evaluation result. The dictionary contains the following
          keys: {'sample_results': {'sensitivity', 'precision', 'f1', 'fpRate',
                    'sensitivity_std', 'precision_std', 'f1_std', 'fpRate_std'},
                 'event_results':{...}
                 }
    """

    FS = 1

    sample_results = dict()
    event_results = dict()
    for subject in Path(reference).glob("sub-*"):
        sample_results[subject.name] = Result()
        event_results[subject.name] = Result()

        for ref_tsv in subject.glob("**/*.tsv"):
            # Load reference
            ref = Annotations.loadTsv(ref_tsv)
            ref = Annotation(ref.getMask(FS), FS)

            # Load hypothesis
            hyp_tsv = Path(hypothesis) / ref_tsv.relative_to(reference)
            if hyp_tsv.exists():
                hyp = Annotations.loadTsv(hyp_tsv)
                try: 
                    hyp = Annotation(hyp.getMask(FS), FS)
                except IndexError as e:
                    print(f"Error in {hyp_tsv}: {e}")
                    hyp = Annotation(np.zeros_like(ref.mask), ref.fs)
            else:
                hyp = Annotation(np.zeros_like(ref.mask), ref.fs)

            # Compute evaluation
            try:
                sample_score = scoring.SampleScoring(ref, hyp)
                event_score = scoring.EventScoring(ref, hyp)
            except ValueError as e:
                print(f"Error in {ref_tsv}: {e}")
                hyp = Annotation(np.zeros_like(ref.mask), ref.fs)
                sample_score = scoring.SampleScoring(ref, hyp)
                event_score = scoring.EventScoring(ref, hyp)

            # Store results
            sample_results[subject.name] += Result(sample_score)
            event_results[subject.name] += Result(event_score)

        # Compute scores
        sample_results[subject.name].computeScores()
        event_results[subject.name].computeScores()

    aggregated_sample_results = dict()
    aggregated_event_results = dict()
    if avg_per_subject:
        for result_builder, aggregated_result in zip(
            (sample_results, event_results),
            (aggregated_sample_results, aggregated_event_results),
        ):
            for metric in ["sensitivity", "precision", "f1", "fpRate"]:
                aggregated_result[metric] = np.nanmean(
                    [getattr(x, metric) for x in result_builder.values()]
                )
                aggregated_result[f"{metric}_std"] = np.nanstd(
                    [getattr(x, metric) for x in result_builder.values()]
                )
    else:
        for result_builder, aggregated_result in zip(
            (sample_results, event_results),
            (aggregated_sample_results, aggregated_event_results),
        ):
            result_builder["cumulated"] = Result()
            for result in result_builder.values():
                result_builder["cumulated"] += result
            result_builder["cumulated"].computeScores()
            for metric in ["sensitivity", "precision", "f1", "fpRate"]:
                aggregated_result[metric] = getattr(result_builder["cumulated"], metric)

    output = {
        "sample_results": aggregated_sample_results,
        "event_results": aggregated_event_results,
    }
    with open(outFile, "w") as file:
        json.dump(output, file, indent=2, sort_keys=False)

    return output
