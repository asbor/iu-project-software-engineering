<template>
    <div>
        <h1>Log Viewer</h1>
        <div class="log-container" ref="logContainer">
            <pre v-html="formattedLogContent"></pre>
        </div>
    </div>
</template>

<style>
.log-container {
    height: 800px;
    overflow-y: auto;
}

.log-container pre {
    white-space: pre-wrap;
}

.error {
    color: red;
}

.warning {
    color: orange;
}

.info {
    color: blue;
}

.debug {
    color: green;
}
</style>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
    data() {
        return {
            logContent: null,
            previousLogContent: null,
            updateIntervalId: null,
        };
    },
    computed: {
        formattedLogContent() {
            if (!this.logContent) return '';

            // Split log content into lines
            const lines = this.logContent.split('\n');

            // Map each line and format based on levelname
            const formattedLines = lines.map(line => {
                if (line.includes('ERROR')) {
                    return `<span class="error">${line}</span>`;
                } else if (line.includes('WARNING')) {
                    return `<span class="warning">${line}</span>`;
                } else if (line.includes('INFO')) {
                    return `<span class="info">${line}</span>`;
                } else if (line.includes('DEBUG')) {
                    return `<span class="debug">${line}</span>`;
                } else {
                    return line; // Default formatting
                }
            });

            // Join the formatted lines back into a single string
            return formattedLines.join('\n');
        }
    },
    mounted() {
        this.fetchLogContent();
        // Start periodic updates when the page is active
        document.addEventListener('visibilitychange', this.handleVisibilityChange);
        this.updateIntervalId = setInterval(this.fetchLogContent, 1000);
    },
    beforeUnmount() {
        // Clear the update interval when the component is unmounted
        clearInterval(this.updateIntervalId);
        document.removeEventListener('visibilitychange', this.handleVisibilityChange);
    },
    methods: {
        async fetchLogContent() {
            try {
                const response = await axios.get('http://localhost:8000/api/logs');
                const newLogContent = response.data.log_content;
                if (newLogContent !== this.previousLogContent) {
                    // Update log content and scroll to bottom only if there are changes
                    this.logContent = newLogContent;
                    this.scrollToBottom();
                    // Update previous log content for comparison
                    this.previousLogContent = newLogContent;
                }
            } catch (error) {
                console.error('Failed to fetch log content:', error);
            }
        },
        scrollToBottom() {
            // Scroll to the bottom of the log container after updating content
            this.$nextTick(() => {
                this.$refs.logContainer.scrollTop = this.$refs.logContainer.scrollHeight;
            });
        },
        handleVisibilityChange() {
            // Pause updates when the page becomes inactive
            if (document.hidden) {
                clearInterval(this.updateIntervalId);
            } else {
                // Resume updates when the page becomes active
                this.updateIntervalId = setInterval(this.fetchLogContent, 1000);
            }
        },
    },
});
</script>
