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
import { defineComponent, ref, computed, onMounted, onBeforeUnmount, nextTick } from 'vue';

export default defineComponent({
    setup() {
        const logContent = ref<string | null>(null);
        const previousLogContent = ref<string | null>(null);
        const logContainerRef = ref<HTMLElement | null>(null);
        let updateIntervalId: NodeJS.Timeout | null = null;

        const fetchLogContent = async () => {
            try {
                const response = await $fetch<{ log_content: string }>('http://localhost:8000/api/logs');
                const newLogContent = response.log_content;
                if (newLogContent !== previousLogContent.value) {
                    logContent.value = newLogContent;
                    previousLogContent.value = newLogContent;
                    scrollToBottom();
                }
            } catch (error) {
                console.error('Failed to fetch log content:', error);
            }
        };

        const scrollToBottom = () => {
            nextTick(() => {
                if (logContainerRef.value) {
                    logContainerRef.value.scrollTop = logContainerRef.value.scrollHeight;
                }
            });
        };

        const handleVisibilityChange = () => {
            if (document.hidden) {
                if (updateIntervalId) clearInterval(updateIntervalId);
            } else {
                updateIntervalId = setInterval(fetchLogContent, 1000);
            }
        };

        const formattedLogContent = computed(() => {
            if (!logContent.value) return '';

            return logContent.value.split('\n').map(line => {
                if (line.includes('ERROR')) {
                    return `<span class="error">${line}</span>`;
                } else if (line.includes('WARNING')) {
                    return `<span class="warning">${line}</span>`;
                } else if (line.includes('INFO')) {
                    return `<span class="info">${line}</span>`;
                } else if (line.includes('DEBUG')) {
                    return `<span class="debug">${line}</span>`;
                } else {
                    return line;
                }
            }).join('\n');
        });

        onMounted(() => {
            fetchLogContent();
            document.addEventListener('visibilitychange', handleVisibilityChange);
            updateIntervalId = setInterval(fetchLogContent, 1000);
        });

        onBeforeUnmount(() => {
            if (updateIntervalId) clearInterval(updateIntervalId);
            document.removeEventListener('visibilitychange', handleVisibilityChange);
        });

        return {
            logContent,
            formattedLogContent,
            logContainerRef,
        };
    }
});
</script>