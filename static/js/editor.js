document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.querySelector('textarea[name="content"]');
    if (textarea) {
        // Auto-grow function
        function autoGrow(elem) {
            elem.style.height = 'auto';
            elem.style.height = (elem.scrollHeight) + 'px';
        }

        // Add input listener
        textarea.addEventListener('input', function() {
            autoGrow(textarea);
        });

        // Initialize on load
        autoGrow(textarea);
    }
}); 