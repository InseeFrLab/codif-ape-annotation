#!/bin/bash
#set -x

export SITE="SOCET"
export LABEL_STUDIO_SERVICE_ENDPOINT=$LABEL_STUDIO_SERVICE_ENDPOINT_REV_NAF2025_SOCET
export LABEL_STUDIO_TOKEN=$LABEL_STUDIO_TOKEN_REV_NAF2025_AGRI
export S3_BUCKET_PREFIX_DEPOT_MANUEL="$S3_BUCKET_PREFIX_ANNOTATION_NACE_REV/$SITE/data-samples/queue/"
export S3_BUCKET_PREFIX_ARCHIVE_DEPOT_MANUEL="$S3_BUCKET_PREFIX_ANNOTATION_NACE_REV/$SITE/data-samples/archive/"
export S3_BUCKET_PREFIX_ANNOTATION_TARGET="$S3_BUCKET_PREFIX_ANNOTATION_NACE_REV/$SITE/data-annotated"

chmod +x labeling_pipeline_s3.sh 
./labeling_pipeline_s3.sh 
