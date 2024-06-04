#!/bin/bash
#set -x

. ./labeling_pipeline_s3.sh 
. ./batch_AGRI.sh 
. ./batch_CG.sh 
. ./batch_PSA.sh 
. ./batch_RSV.sh 
. ./batch_SOCET.sh 
. ./batch_SSP.sh 

# Move the treated batch data to the archive
mc mv "$SOURCE_PATH$filename" "$ARCHIVE_PATH"