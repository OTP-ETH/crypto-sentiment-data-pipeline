variable "bucket_name" {
    type        = string
    description = "Name of the bucket to create"
    default     = "raw-crypto-market-data"
}

variable "dataset_name" {
    type        = string
    description = "Name of the dataset to create"
    default     = "crypto-market-data"
}

variable "location" {
    type        = string
    description = "Location of the bucket and dataset"
    default     = "US"
}