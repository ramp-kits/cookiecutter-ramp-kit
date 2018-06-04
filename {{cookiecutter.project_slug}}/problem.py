{% set is_classifier = cookiecutter.project_task == 'Classification' %}
{% set is_regressor = cookiecutter.project_task == 'Regression' %}
{% set is_detector = cookiecutter.project_task == 'Detection' %}
"""
problem.py
----------
"""
import rampwf


problem_title = '{{ cookiecutter.project_short_description }}'

# --------------------------------------
# 1) An object implementing the workflow
# --------------------------------------
#   rampwf.workflows.AirPassengers
#   rampwf.workflows.Classifier
#   rampwf.workflows.Clusterer
#   rampwf.workflows.DrugSpectra
#   rampwf.workflows.ElNino
#   rampwf.workflows.FeatureExtractor
#   rampwf.workflows.FeatureExtractorClassifier
#   rampwf.workflows.FeatureExtractorRegressor
#   rampwf.workflows.ImageClassifier
#   rampwf.workflows.SimplifiedImageClassifier
#   rampwf.workflows.ObjectDetector
#   rampwf.workflows.Regressor
#   rampwf.workflows.TimeSeriesFeatureExtractor
#   rampwf.workflows.GridFeatureExtractorClassifier

workflow = ...

# -------------------------------------------------------------------
# 2) A prediction type (class) to create wrapper objects for `y_pred`,
# -------------------------------------------------------------------
#   rampwf.prediction_types.make_clustering
#   rampwf.prediction_types.make_combined
#   rampwf.prediction_types.make_detection
#   rampwf.prediction_types.make_multiclass
#   rampwf.prediction_types.make_regression

Predictions = ...

# ----------------------------------------------------------------
# 3) A list of metrics to test the predictions against (minimum 1)
# ----------------------------------------------------------------
#   rampwf.score_types.Accuracy
#   rampwf.score_types.BalancedAccuracy
#   rampwf.score_types.BaseScoreType
#   rampwf.score_types.BrierScore
#   rampwf.score_types.BrierScoreReliability
#   rampwf.score_types.BrierScoreResolution
#   rampwf.score_types.BrierSkillScore
#   rampwf.score_types.ClassificationError
#   rampwf.score_types.ClusteringEfficiency
#   rampwf.score_types.Combined
#   rampwf.score_types.DetectionPrecision
#   rampwf.score_types.DetectionRecall
#   rampwf.score_types.DetectionAveragePrecision
#   rampwf.score_types.F1Above
#   rampwf.score_types.MacroAveragedRecall
#   rampwf.score_types.MakeCombined
#   rampwf.score_types.MADCenter
#   rampwf.score_types.MADRadius
#   rampwf.score_types.MARE
#   rampwf.score_types.NegativeLogLikelihood
#   rampwf.score_types.NormalizedGini
#   rampwf.score_types.OSPA
#   rampwf.score_types.RelativeRMSE
#   rampwf.score_types.RMSE
#   rampwf.score_types.ROCAUC
#   rampwf.score_types.SCP
#   rampwf.score_types.SoftAccuracy

score_types = [

]

# --------------------------------------------------------------------------
# 4) A cross-validation scheme in the form of a function that returns a list
#    of array indices for the training AND testing data
# --------------------------------------------------------------------------
# This can be done manually, e.g.
#
#   def get_cv(X, y):
#       n = len(X)
#       v = n // 2
#       return [(np.r_[0:v], np.r_[v:n]),
#               (np.r_[v:n], np.r_[0:v])]
#
# or using `scikit-learn` utilities, e.g.
#
#   def get_cv(X, y):
#       from sklearn.model_selection import StratifiedShuffleSplit
#       cv = StratifiedShuffleSplit(n_splits=2, test_size=0.2, random_state=57)
#       return cv.split(X, y)

def get_cv(X, y):
    pass

# ------------------------------------------------------------
# 5) A method that can read both the training and testing data
# ------------------------------------------------------------
#
#   def _read_data(path, dataset):
#       import pandas
#       data = pandas.read_csv(
#           os.path.join(path, 'data', '{}.csv'.format(dataset)))
#       y = data[<target_column_name>].values
#       X = data.drop([<target_column_name>], axis=1).values
#       return X, y
#
# For heavy datesets, a smaller version of the data should be provided
# as `_mini` files e.g. for `train.csv` file, provide a `train_mini.csv`.
# Therefor the `_read_data` method should implement a way to read these
# smaller files using as trigger the environment variable `RAMP_TEST_MODE`.
#
#   def _read_data(path, dataset):
#       import os
#       if os.getenv('RAMP_TEST_MODE', 0):
#           suffix = '_mini'
#       else:
#           suffit = ''
#       data = pandas.read_csv(
#           os.path.join(path, 'data', '{}{}.csv'.format(dataset, suffix)))
#       ...
#       return X, y

def _read_data(path, dataset):
    pass


def get_test_data(path='.'):
    return _read_data(path, 'test')


def get_train_data(path='.'):
    return _read_data(path, 'train')
