# set env variables
export NAMESPACE='nrandriamanana'
export PATH_ANNOTATION_RESULTS='label-studio/annotation-campaign-2024/rev-NAF2025/CG/data-annotated/in-progress'
export DATA_FILE_PATH_LOCAL='data'
export PATH_ANNOTATION_PREPROCESSED='label-studio/annotation-campaign-2024/rev-NAF2025/CG/preprocessed'

# download python script to convert json files to dataframe
#wget https://raw.githubusercontent.com/InseeFrLab/codif-ape-API/main/utils/extract_test_data.py

# Retrieve recursively all annotation data and copy locally
mc ls s3/$NAMESPACE/$PATH_ANNOTATION_RESULTS | awk '{print "s3/'$NAMESPACE'/'$PATH_ANNOTATION_RESULTS'/" $5}' | xargs -I {} mc cp --recursive {} ./$DATA_FILE_PATH_LOCAL

# Transform and save annotation data
python extract_test_data.py $DATA_FILE_PATH_LOCAL $PATH_ANNOTATION_PREPROCESSED
