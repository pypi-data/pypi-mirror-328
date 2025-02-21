#  Copyright (c) Prior Labs GmbH 2025.
#  Licensed under the Apache License, Version 2.0

from __future__ import annotations

import copy
import random
from sklearn.ensemble import StackingClassifier, BaggingClassifier, VotingClassifier

from . import configs
from tabpfn_extensions.rf_pfn import (
    RandomForestTabPFNClassifier,
    RandomForestTabPFNRegressor,
)
from .weighted_ensemble import WeightedAverageEnsemble


class TabPFNEnsemble(VotingClassifier):
    def set_categorical_features(self, categorical_features):
        for model_name, model in self.estimators:
            model.set_categorical_features(categorical_features)


def get_tabpfn_outer_ensemble(config: configs.TabPFNConfig, **kwargs):
    """
    This will create a model very similar to our standard TabPFN estimators,
    but it uses multiple model weights to generate predictions.
    Thus the `configs.TabPFNModelPathsConfig` can contain multiple paths which are all used.

    A product of the preprocessor_trasnforms and paths is created to yield interesting ensemble members.

    This only supports multiclass for now. If you want to add regression, you probably want to add
    the y_transforms to the relevant_config_product.
    :param config: TabPFNConfig
    :param kwargs: kwargs are passed to get_single_tabpfn, e.g. device
    :return: A TabPFNEnsemble, which is a soft voting classifier that mixes multiple standard TabPFN estimators.
    """
    assert config.task_type == "multiclass", "Only multiclass is supported for now."
    if config.model_type_config is not None:
        pass  # assert config.model_type_config.multiclass_decoder == "shuffle"

    relevant_config_product = list(
        utils.product_dict(
            {
                "paths_config": [
                    configs.TabPFNModelPathsConfig([p])
                    for p in config.paths_config.paths
                ],
                "preprocess_transforms": [
                    (pp_transform,) for pp_transform in config.preprocess_transforms
                ],
            }
        )
    )
    # shuffle with fixed seed
    relevant_config_product = sorted(
        relevant_config_product, key=lambda x: hash(str(x))
    )

    # if we have more ensemble configurations than models, we can have multiple configurations per model
    n_estimators_per_model = max(config.n_estimators // len(relevant_config_product), 1)

    single_tabpfns = []
    for ensemble_member_index, sub_config in zip(
        range(config.n_estimators), relevant_config_product
    ):
        member_config = copy.deepcopy(config)
        for k, v in sub_config.items():
            setattr(member_config, k, v)
        member_config.model_type = "single"
        member_config.n_estimators = n_estimators_per_model
        print(member_config)
        tabpfn = get_single_tabpfn(member_config, **kwargs)
        tabpfn.seed = ensemble_member_index + 120412 + random.randint(0, 100_000)
        single_tabpfns.append(tabpfn)

    ensemble_tabpfn = TabPFNEnsemble(
        estimators=[(f"model_{i}", clf) for i, clf in enumerate(single_tabpfns)],
        voting="soft",
        n_jobs=1,
    )
    print("oour tabpfn ensemble is: ", ensemble_tabpfn)
    return ensemble_tabpfn


def get_tabpfn_rf(config, random_state=0, **kwargs):
    tabpfn = get_single_tabpfn(config, **kwargs)
    show_progress = tabpfn.show_progress
    tabpfn.show_progress = False
    if config.task_type == "multiclass":
        return RandomForestTabPFNClassifier(
            tabpfn=tabpfn,
            min_samples_leaf=config.model_type_config.min_samples_leaf,
            min_samples_split=config.model_type_config.min_samples_split,
            n_estimators=config.model_type_config.n_estimators,
            max_features=config.model_type_config.max_features,
            show_progress=show_progress,
            preprocess_X_once=config.model_type_config.preprocess_X_once,
            bootstrap=config.model_type_config.bootstrap,
            criterion=config.model_type_config.criterion,
            adaptive_tree=config.model_type_config.adaptive_tree,
            adaptive_tree_overwrite_metric=config.model_type_config.adaptive_tree_overwrite_metric,
            adaptive_tree_test_size=config.model_type_config.adaptive_tree_test_size,
            adaptive_tree_min_train_samples=config.model_type_config.adaptive_tree_min_train_samples,
            adaptive_tree_min_valid_samples_fraction_of_train=config.model_type_config.adaptive_tree_min_valid_samples_fraction_of_train,
            adaptive_tree_max_train_samples=config.model_type_config.adaptive_tree_max_train_samples,
            adaptive_tree_skip_class_missing=config.model_type_config.adaptive_tree_skip_class_missing,
            dt_average_logits=config.model_type_config.dt_average_logits,
            random_state=random_state,
            rf_average_logits=config.model_type_config.rf_average_logits,
            max_predict_time=config.model_type_config.max_predict_time,
        )
    elif config.task_type == "regression":
        return RandomForestTabPFNRegressor(
            tabpfn=tabpfn,
            min_samples_leaf=config.model_type_config.min_samples_leaf,
            min_samples_split=config.model_type_config.min_samples_split,
            n_estimators=config.model_type_config.n_estimators,
            max_features=config.model_type_config.max_features,
            show_progress=show_progress,
            preprocess_X_once=config.model_type_config.preprocess_X_once,
            bootstrap=config.model_type_config.bootstrap,
            criterion=config.model_type_config.criterion,
            adaptive_tree=config.model_type_config.adaptive_tree,
            adaptive_tree_overwrite_metric=config.model_type_config.adaptive_tree_overwrite_metric,
            adaptive_tree_test_size=config.model_type_config.adaptive_tree_test_size,
            adaptive_tree_min_train_samples=config.model_type_config.adaptive_tree_min_train_samples,
            adaptive_tree_min_valid_samples_fraction_of_train=config.model_type_config.adaptive_tree_min_valid_samples_fraction_of_train,
            adaptive_tree_max_train_samples=config.model_type_config.adaptive_tree_max_train_samples,
            random_state=random_state,
            rf_average_logits=config.model_type_config.rf_average_logits,
            max_predict_time=config.model_type_config.max_predict_time,
        )
    else:
        raise ValueError(f"Unknown task type for RF PFN {config.task_type}")


class TabPFNWeightedAverageEnsemble(WeightedAverageEnsemble):
    def set_categorical_features(self, categorical_features):
        self.categorical_features = categorical_features
        for _, estimator in self.estimators:
            if estimator.__class__.__name__ == "TabPFNClassifier":
                estimator.set_categorical_features(categorical_features)

    def meta_init_seed(self):
        for i, (_, estimator) in enumerate(self.estimators):
            if estimator.__class__.__name__ == "TabPFNClassifier":
                estimator.seed = i
                estimator._init_rnd()

    def fit(self, X, y):
        self.meta_init_seed()
        return super().fit(X, y)

    def predict_proba(self, X):
        self.meta_init_seed()
        return super().predict_proba(X)

    def predict(self, X):
        self.meta_init_seed()
        return super().predict(X)


class TabPFNStackingClassifier(StackingClassifier):
    def set_categorical_features(self, categorical_features):
        self.categorical_features = categorical_features
        for _, estimator in self.estimators:
            if estimator.__class__.__name__ == "TabPFNClassifier":
                estimator.set_categorical_features(categorical_features)

    def meta_init_seed(self):
        for i, (_, estimator) in enumerate(self.estimators):
            if estimator.__class__.__name__ == "TabPFNClassifier":
                estimator.seed = i
                estimator._init_rnd()

    def fit(self, X, y, sample_weight=None):
        self.meta_init_seed()
        return super().fit(X, y, sample_weight=sample_weight)

    def predict_proba(self, X):
        self.meta_init_seed()
        return super().predict_proba(X)

    def predict(self, X, **predict_params):
        self.meta_init_seed()
        return super().predict(X, **predict_params)

    # TODO: Adapt scoring function, needs to overwrite the scoring function of the
    #  _BaseStacking or in BaseTabPFNClassifier
    # def score(self, X, y=None):
    #    if self.optimize_metric == "roc":
    #        from sklearn.metrics import roc_auc_score

    #        return roc_auc_score(X, y)


class TabPFNBaggingClassifier(BaggingClassifier):
    def set_categorical_features(self, categorical_features):
        self.categorical_features = categorical_features
        self.estimator.set_categorical_features(categorical_features)

    def _fit(
        self,
        X,
        y,
        max_samples=None,
        max_depth=None,
        sample_weight=None,
        check_input=True,
    ):
        self.estimator.seed = None  # Make sure that TabPFN is not seeded
        max_samples = min(
            X.shape[0], max_samples
        )  # Breaks in sklearn if max_samples is larger than X.shape[0]
        super()._fit(
            X,
            y,
            max_samples=max_samples,
            max_depth=max_depth,
            sample_weight=sample_weight,
            check_input=check_input,
        )

    def __init_rnd(self):
        self.estimator._init_rnd()

    # TODO: Adapt scoring function, needs to overwrite the scoring function of the
    #  _BaseStacking or in BaseTabPFNClassifier


def get_bagging_ensemble(config, **kwargs):
    tabpfn = get_single_tabpfn(config, **kwargs)
    tabpfn.show_progress = False
    tabpfn.seed = None
    return TabPFNBaggingClassifier(
        estimator=tabpfn,
        n_estimators=config.model_type_config.n_estimators,
        max_samples=config.model_type_config.max_samples,
        max_features=config.model_type_config.max_features,
        random_state=0,
        bootstrap_features=config.model_type_config.bootstrap_features,
        bootstrap=config.model_type_config.bootstrap,
        # Replacement does not work with TabPFN since repeated samples are ignored
    )


def get_stacking_ensemble(config, **kwargs):
    # TODO: Overwrite StackingClassifier score method to use the same metric that should be optimized
    #   Make this easily adaptable to different metrics
    # TODO: Adapt final_estimator
    estimators = []
    for seed, stacking_config in enumerate(config.model_type_config.params_stacked):
        config_ = copy.deepcopy(config)
        for k, v in stacking_config.items():  # Overwrite configs with stacking settings
            setattr(config_, k, v)
        tabpfn = get_single_tabpfn(config_, **kwargs)
        tabpfn.show_progress = False
        tabpfn.seed = seed
        estimators.append(
            (
                str(stacking_config),
                tabpfn,
            )
        )

    if config.model_type_config.append_other_model_types:
        from xgboost import XGBClassifier

        estimators.append(("rf", XGBClassifier()))

    return TabPFNStackingClassifier(
        estimators=estimators,
        final_estimator=config.model_type_config.final_estimator,
        cv=config.model_type_config.cv,
    )


def get_weighted_average_ensemble(config, **kwargs):
    estimators = []
    for seed, stacking_config in enumerate(config.model_type_config.params_stacked):
        config_ = copy.deepcopy(config)
        for k, v in stacking_config.items():  # Overwrite configs with stacking settings
            setattr(config_, k, v)
        tabpfn = get_single_tabpfn(config_, **kwargs)
        tabpfn.show_progress = False
        tabpfn.seed = seed
        estimators.append(
            (
                str(stacking_config),
                tabpfn,
            )
        )

    return TabPFNWeightedAverageEnsemble(
        estimators=estimators,
        cv=config.model_type_config.cv,
        n_max=config.model_type_config.n_max,
    )
