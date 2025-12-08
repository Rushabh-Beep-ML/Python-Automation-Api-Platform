document.addEventListener('DOMContentLoaded', function () {
    const rawInput = document.getElementById('rawInput');
    const charCount = document.getElementById('charCount');
    const processBtn = document.getElementById('processBtn');
    const downloadBtn = document.getElementById('downloadBtn');
    const operationCheckboxes = document.querySelectorAll('input[name="operation"]');
    const caseOptions = document.getElementById('caseOptions');
    const resultsSection = document.getElementById('resultsSection');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const errorSection = document.getElementById('errorSection');
    const resultsJson = document.getElementById('resultsJson');
    const totalItemsDisplay = document.getElementById('totalItems');
    const operationsCountDisplay = document.getElementById('operationsCount');
    const errorMessage = document.getElementById('errorMessage');

    let lastResults = null;

    rawInput.addEventListener('input', function () {
        charCount.textContent = this.value.length;
    });

    operationCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            const normalizeCaseCheckbox = Array.from(operationCheckboxes).find(cb => cb.value === 'normalize_case');
            if (normalizeCaseCheckbox && normalizeCaseCheckbox.checked) {
                caseOptions.classList.remove('hidden');
            } else {
                caseOptions.classList.add('hidden');
            }
        });
    });

    processBtn.addEventListener('click', async function () {
        const input = rawInput.value.trim();

        if (!input) {
            showError('Please enter some data to process');
            return;
        }

        const selectedOperations = Array.from(operationCheckboxes)
            .filter(cb => cb.checked)
            .map(cb => cb.value);

        if (selectedOperations.length === 0) {
            showError('Please select at least one processing option');
            return;
        }

        await processData(input, selectedOperations);
    });

    downloadBtn.addEventListener('click', function () {
        if (!lastResults) {
            alert('No data to download');
            return;
        }

        const dataStr = JSON.stringify(lastResults, null, 2);
        const dataBlob = new Blob([dataStr], { type: 'application/json' });
        const url = URL.createObjectURL(dataBlob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `processed_data_${new Date().toISOString().split('T')[0]}.json`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    });

    async function processData(input, operations) {
        showLoading(true);
        hideError();
        resultsSection.classList.add('hidden');

        const payload = {
            raw_input: input,
            operations: operations
        };

        if (operations.includes('normalize_case')) {
            const caseType = document.getElementById('caseType').value;
            payload.case_type = caseType;
        }

        try {
            const response = await fetch('/api/process', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Processing failed');
            }

            const results = await response.json();
            lastResults = results;
            displayResults(results);

        } catch (error) {
            showError(error.message || 'An error occurred during processing');
            console.error('Processing error:', error);
        } finally {
            showLoading(false);
        }
    }

    function displayResults(results) {
        if (results.success) {
            resultsJson.textContent = JSON.stringify(results, null, 2);
            totalItemsDisplay.textContent = results.summary.total_items;
            operationsCountDisplay.textContent = results.summary.operations_applied.length;
            resultsSection.classList.remove('hidden');
        } else {
            showError(results.error || 'Unknown error occurred');
        }
    }

    function showLoading(show) {
        if (show) {
            loadingSpinner.classList.remove('hidden');
            processBtn.disabled = true;
        } else {
            loadingSpinner.classList.add('hidden');
            processBtn.disabled = false;
        }
    }

    function showError(message) {
        errorSection.classList.remove('hidden');
        errorMessage.textContent = message;
    }

    function hideError() {
        errorSection.classList.add('hidden');
    }
});
