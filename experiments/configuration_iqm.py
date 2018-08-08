#-----------------------------------------------------------------
# Configuration file automatically generated at 2017-12-29
#-----------------------------------------------------------------


#REQUIRED ARGUMENTS:

#Database and protocol:
#	 * registered databases are: ['all-pad-databases', 'replay-attack', 'replay-attack-lite', 'replay-mobile', 'replay-mobile-lite', 'msu-mfsd', 'oulu-npu', 'holyface']
#	 * registered protocols are multiples and you need to check each database, here we leave some common examples: ['grandtest', 'print', 'replay']
#	 * note that you can select several databases or protocols to fill the list out (e.g databases_list = ['replay-mobile', 'oulu-npu']; protocols_list = ['grandtest'])
#	 * you can define your own database object as long as it met the bob.gradiant.core.Database interface
#	 * you can use on the same list labels (e.g 'replay-attack', 'replay-mobile', etc) and bob.gradiant.core.Database classes. e.g databases_list = [ MyDatabase('path/to/database'), 'replay-mobile']
#	 * databases paths must be defined as a environment variables. (REPLAY_ATTACK_PATH, REPLAY_MOBILE_PATH, MSU_MFSD_PATH, OULU_NPU_PATH) 
#os.environ['REPLAY_ATTACK_PATH'] = '<path-to-database>' (if not defined)
#os.environ['REPLAY_MOBILE_PATH'] = '<path-to-database>' (if not defined)
#os.environ['MSU_MFSD_PATH'] = '<path-to-database>' (if not defined)
#os.environ['OULU_NPU_PATH'] = '<path-to-database>' (if not defined)
databases_list = ['oulu-npu']
protocols_list = ['grandtest']

#Feature extraction:
from bob.chapter.hobpad2.facepadprotocols import IqmFeaturesExtractor
feature_extractor = IqmFeaturesExtractor()

#Pipeline:
from bob.gradiant.pipelines import Pipeline, AverageScoreFusion
pipeline = Pipeline('iqm',[AverageScoreFusion()])

#Result base path:
result_path = 'result/iqm'

#Framerate and time parameters:
#	 * Ignore these if you are not benchmarking your system with ACE (Algorithmic Contrained Evaluation)
#	 * framerate_list : framerates list to evaluate (e.g [5, 10, 15, 20, 25] in FPS)
#	 * total_time_acquisition_list : framerates list to evaluate (e.g [500, 1000, 1500, 2000] in milliseconds)
#	 * The ACE protocol combines both lists
framerate_list = [5, 10, 15, 20, 25]
total_time_acquisition_list = [500, 1000, 1500, 2000]

#-----------------------------------------------------------------

#OPTIONAL ARGUMENTS:

#Verbose (only True/False are valid):
verbose = True

#Number of threads for parallelizing the features extraction:
number_threads = 4

#Data augmentation:
use_data_augmentation = False

#Features extraction: you can skip extraction stage if, for example, you have already extracted your features
#	 * if you set skip_features_extraction to True, you must set the dict_extracted_features_paths
#	 * dict_extracted_features_paths = {'name-database', <path-to-features>}
skip_features_extraction = False
#dict_extracted_features_paths = ''

#Training: you can skip training stage
skip_training = False

#Scores prediction: you can skip scores prediction if you have already available the scores
#	 * if you set skip_scores_prediction to True, you must set the dict_scores_paths
#	 * dict_scores_paths = {'name-database', <path-to-scores>}
skip_scores_prediction = False

#Recreate: If it is true, features extraction will be done overwriting previous files
recreate = False
#-----------------------------------------------------------------

#END-TO-END ARGUMENTS:

#Face-PAD (Presentation Attack Detector): 
from bob.chapter.hobpad2.facepadprotocols import IqmFacePad
face_pad = IqmFacePad(threshold = -0.975393)
#Framerate, Fr (end-to-end): optimum value obtained (int) from Algorithmic Constrained Evaluation Protocol
framerate_end_to_end = 25

#Total time of acquisition, Ta (end-to-end): optimum value (int) obtained from Algorithmic Constrained Evaluation Protocol
total_time_acquisition_end_to_end = 2000

#Threshold, Th (end-to-end): optimum value (float) obtained from Algorithmic Constrained Evaluation Protocol
threshold_end_to_end = -0.975393 # (Given by Fr = 25 and Ta = 2000
#-----------------------------------------------------------------
