#-----------------------------------------------------------------
# Configuration file automatically generated at 2017-12-29
#-----------------------------------------------------------------

#REQUIRED ARGUMENTS:

#Database and protocol:
databases_list = ['oulu-npu']
protocols_list = ['grandtest']

#Feature extraction:
from bob.chapter.hobpad2.facepadprotocols import IqmFeaturesExtractor
feature_extractor = IqmFeaturesExtractor()

#Pipeline:
from bob.gradiant.pipelines import Pipeline, AverageScoreFusion
pipeline = Pipeline('gradiant_from_scores_pretrained',[AverageScoreFusion()])

#Result base path:
result_path = 'result/gradiant_from_scores_pretrained'

#Framerate and time parameters:
framerate_list = [5, 10, 15, 20, 25]
total_time_acquisition_list = [500, 1000, 1500, 2000]

#-----------------------------------------------------------------

#OPTIONAL ARGUMENTS:

#Verbose (only True/False are valid):
verbose = True

#Number of threads for parallelizing the features extraction:
number_threads = 1

#Data augmentation:
use_data_augmentation = False

#Features extraction: you can skip extraction stage if, for example, you have already extracted your features
skip_features_extraction = True
dict_extracted_features_paths = {'oulu-npu' : None}

#Training: you can skip training stage
skip_training = True

#Scores prediction: you can skip scores prediction if you have already available the scores
#	 * if you set skip_scores_prediction to True, you must set the dict_scores_paths
#	 * dict_scores_paths = {'name-database', <path-to-scores>}
skip_scores_prediction = True
scores_database = 'oulu-npu'
dict_scores_prediction = { scores_database : {'ACE' : 'scores/{}/gradiant_scores_constrained_pretrained'.format(scores_database)}}

#Recreate: If it is true, features extraction will be done overwriting previous files
recreate = False
#-----------------------------------------------------------------

#END-TO-END ARGUMENTS:

#Face-PAD (Presentation Attack Detector): 
#	 * You can define your own facePad object as long as it met the bob.gradiant.core.FacePad interface
#	 Example:
#	 from bob.gradiant.pad.evaluator import DummyFacePad
#	 face_pad = DummyFacePad()
face_pad = None
#Framerate, Fr (end-to-end): optimum value obtained (int) from Algorithmic Constrained Evaluation Protocol
framerate_end_to_end = None

#Total time of acquisition, Ta (end-to-end): optimum value (int) obtained from Algorithmic Constrained Evaluation Protocol
total_time_acquisition_end_to_end = None

#Threshold, Th (end-to-end): optimum value (float) obtained from Algorithmic Constrained Evaluation Protocol
threshold_end_to_end = None
#-----------------------------------------------------------------
