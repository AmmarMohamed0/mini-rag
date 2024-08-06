from enum import Enum

class ResponseSignal(Enum):
    
    
    FILE_VALIDATE_SUCCESS = "file validate success"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDS = "file size exceeded"
    FILE_UPLOAD_SUCCESS = "file upload success"
    FILE_UPLOAD_FAILED = "file upload failed"
    PROCESSING_FAILED = "processing failed"
    PROCESSING_SUCCESS = "processing success"
    NO_FILES_ERROR = "not found files"
    FILE_ID_ERROR = "no file found with this id"