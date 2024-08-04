document.addEventListener('DOMContentLoaded', function () {
    const initForm = document.getElementById('init-form');
    const addFileForm = document.getElementById('add-file-form');
    const commitForm = document.getElementById('commit-form');

    // Handler for Initialize Repository form
    initForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(initForm);
        fetch('/', {
            method: 'POST',
            body: formData
        })
            .then(response => response.text())
            .then(data => {
                alert('Repository Initialized: ' + data);
                initForm.reset();
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

    // Handler for Add File form
    addFileForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(addFileForm);
        fetch('/add_file', {
            method: 'POST',
            body: formData
        })
            .then(response => response.text())
            .then(data => {
                alert('File Added: ' + data);
                addFileForm.reset();
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

    // Handler for Commit Changes form
    commitForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(commitForm);
        fetch('/commit', {
            method: 'POST',
            body: formData
        })
            .then(response => response.text())
            .then(data => {
                alert('Changes Committed: ' + data);
                commitForm.reset();
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});
