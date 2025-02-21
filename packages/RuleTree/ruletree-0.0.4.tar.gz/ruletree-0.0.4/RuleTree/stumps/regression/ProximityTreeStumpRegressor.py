import copy
import random
import warnings

import numpy as np
import psutil
import tempfile312
from matplotlib import pyplot as plt
from numba import UnsupportedError

from RuleTree.stumps.classification import ProximityTreeStumpClassifier
from RuleTree.stumps.regression import DecisionTreeStumpRegressor
from RuleTree.utils.define import DATA_TYPE_TS
from RuleTree.utils.shapelet_transform.Shapelets import Shapelets


class ProximityTreeStumpRegressor(DecisionTreeStumpRegressor):
    def __init__(self,
                 n_shapelets=psutil.cpu_count(logical=False) * 2,
                 n_shapelets_for_selection=500,  # int, inf, or 'stratified'
                 n_ts_for_selection_per_class=100,  # int, inf
                 sliding_window=50,
                 selection='mi_clf',  # random, mi_clf, mi_reg, cluster
                 distance='euclidean',
                 mi_n_neighbors=100,
                 random_state=42, n_jobs=1,
                 **kwargs):
        self.n_shapelets = n_shapelets
        self.n_shapelets_for_selection = n_shapelets_for_selection
        self.n_ts_for_selection_per_class = n_ts_for_selection_per_class
        self.sliding_window = sliding_window
        self.selection = selection
        self.distance = distance
        self.mi_n_neighbors = mi_n_neighbors
        self.random_state = random_state
        self.n_jobs = n_jobs

        if "max_depth" in kwargs and kwargs["max_depth"] > 1:
            warnings.warn("max_depth must be 1")

        kwargs["max_depth"] = 1

        if selection not in ['random', 'mi_clf', 'cluster']:
            raise ValueError("'selection' must be 'random', 'mi_clf' or 'cluster'")

        super().__init__(**kwargs)

        kwargs |= {
            "n_shapelets": n_shapelets,
            "n_shapelets_for_selection": n_shapelets_for_selection,
            "n_ts_for_selection_per_class": n_ts_for_selection_per_class,
            "sliding_window": sliding_window,
            "selection": selection,
            "distance": distance,
            "mi_n_neighbors": mi_n_neighbors,
            "random_state": random_state,
            "n_jobs": n_jobs,
        }

    def fit(self, X, y, idx=None, context=None, sample_weight=None, check_input=True):
        if idx is None:
            idx = slice(None)
        X = X[idx]
        y = y[idx]

        self.y_lims = [X.min(), X.max()]

        random.seed(self.random_state)
        if sample_weight is not None:
            raise UnsupportedError(f"sample_weight is not supported for {self.__class__.__name__}")

        self.st = Shapelets(n_shapelets=self.n_shapelets,
                            n_shapelets_for_selection=self.n_shapelets_for_selection,
                            n_ts_for_selection_per_class=self.n_ts_for_selection_per_class,
                            sliding_window=self.sliding_window,
                            selection=self.selection,
                            distance=self.distance,
                            mi_n_neighbors=self.mi_n_neighbors,
                            random_state=random.randint(0, 2**32-1),
                            n_jobs=self.n_jobs
                            )

        X_dist = self.st.fit_transform(X, y)
        actual_n_shapelets = X_dist.shape[1]
        X_bool = np.zeros((X.shape[0], actual_n_shapelets*(actual_n_shapelets-1)), dtype=bool)

        c = 0

        for i in range(actual_n_shapelets):
            for j in range(i+1, actual_n_shapelets):
                X_bool[:, c] = X_dist[:, i] <= X_dist[:, j]
                c += 1

        return super().fit(X_bool, y=y, sample_weight=sample_weight, check_input=check_input)

    def apply(self, X, check_input=False):
        self.y_lims = [min(self.y_lims[0], X.min()), min(self.y_lims[1], X.max())]
        X_dist = self.st.transform(X)
        actual_n_shapelets = X_dist.shape[1]
        X_bool = np.zeros((X.shape[0], actual_n_shapelets * (actual_n_shapelets - 1)), dtype=bool)

        c = 0

        for i in range(actual_n_shapelets):
            for j in range(i + 1, actual_n_shapelets):
                X_bool[:, c] = X_dist[:, i] <= X_dist[:, j]
                c += 1


        return super().apply(X_bool, check_input=check_input)

    def supports(self, data_type):
        return data_type in [DATA_TYPE_TS]


    def get_rule(self, columns_names=None, scaler=None, float_precision: int | None = 3):
        return ProximityTreeStumpClassifier.get_rule(self, columns_names, scaler, float_precision)

    def node_to_dict(self):
        return ProximityTreeStumpClassifier.node_to_dict(self)

    @classmethod
    def dict_to_node(cls, node_dict, X=None):
        self = cls(
            n_shapelets=node_dict["n_shapelets"],
            n_shapelets_for_selection=node_dict["n_shapelets_for_selection"],
            n_ts_for_selection_per_class=node_dict["n_ts_for_selection_per_class"],
            sliding_window=node_dict["sliding_window"],
            selection=node_dict["selection"],
            distance=node_dict["distance"],
            mi_n_neighbors=node_dict["mi_n_neighbors"],
            random_state=node_dict["random_state"],
            n_jobs=node_dict["n_jobs"]
        )

        self.st = Shapelets(
            n_shapelets=node_dict["n_shapelets"],
            n_shapelets_for_selection=node_dict["n_shapelets_for_selection"],
            n_ts_for_selection_per_class=node_dict["n_ts_for_selection_per_class"],
            sliding_window=node_dict["sliding_window"],
            selection=node_dict["selection"],
            distance=node_dict["distance"],
            mi_n_neighbors=node_dict["mi_n_neighbors"],
            random_state=node_dict["random_state"],
            n_jobs=node_dict["n_jobs"]
        )

        self.st.shapelets = np.array(node_dict["shapelets"])

        self.feature_original = np.zeros(3, dtype=int)
        self.threshold_original = np.zeros(3)
        self.n_node_samples = np.zeros(3, dtype=int)

        self.y_lims = node_dict["y_lims"]

        self.feature_original[0] = node_dict["feature_idx"]
        self.threshold_original[0] = node_dict["threshold"]
        self.n_node_samples[0] = node_dict["samples"]
        self.is_categorical = node_dict["is_categorical"]

        args = copy.deepcopy(node_dict["args"])
        self.is_oblique = args.pop("is_oblique")
        self.is_pivotal = args.pop("is_pivotal")
        self.unique_val_enum = args.pop("unique_val_enum")
        self.coefficients = args.pop("coefficients")
        self.kwargs = args

        return self