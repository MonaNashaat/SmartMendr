from __future__ import absolute_import

from smartmendr.ensemble_learner.models.meta import smartmendrBase, smartmendrSession, smartmendr_engine, smartmendr_postgres
from smartmendr.ensemble_learner.models.context import Context, Document, Sentence, TemporarySpan, Span
from smartmendr.ensemble_learner.models.context import construct_stable_id, split_stable_id
from smartmendr.ensemble_learner.models.candidate import Candidate, candidate_subclass, Marginal
from smartmendr.ensemble_learner.models.annotation import (
    Feature, FeatureKey, Label, LabelKey, GoldLabel, GoldLabelKey, StableLabel,
    Prediction, PredictionKey
)


smartmendrBase.metadata.create_all(smartmendr_engine)
