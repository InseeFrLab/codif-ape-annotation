#!/bin/bash
#set -x

# install packages
pip install -r requirements.txt

# launch scripts
. ./labeling_pipeline_s3.sh 
. ./batch_AGRI.sh 
. ./batch_CG.sh 
. ./batch_PSA.sh 
#. ./batch_RSV.sh 
. ./batch_SOCET.sh 
. ./batch_SSP.sh 