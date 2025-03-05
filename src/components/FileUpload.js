import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

function FileUpload() {
  // Function to handle file drop
  const onDrop = useCallback((acceptedFiles) => {
    const formData = new FormData();
    formData.append('file', acceptedFiles[0]); // Appending the file to FormData

    // POST request to the backend to upload the file
    axios.post('http://localhost:5000/upload', formData)
      .then(response => {
        alert(response.data.message); // Show success message
      })
      .catch(error => {
        console.error('There was an error uploading the file!', error);
      });
  }, []);

  // React Dropzone hooks
  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div {...getRootProps()} className="dropzone" style={dropzoneStyle}>
      <input {...getInputProps()} />
      <p>Drag and drop some files here, or click to select files</p>
    </div>
  );
}

// Basic styling for the dropzone
const dropzoneStyle = {
  border: '2px dashed #007bff',
  padding: '20px',
  textAlign: 'center',
  cursor: 'pointer'
};

export default FileUpload;
