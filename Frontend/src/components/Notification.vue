<template>
    <div class="text-center ma-2">
        <v-snackbar v-model="notify" :color="color" timeout="2500">
            {{ text }}
        </v-snackbar>
    </div>
</template>

<script>
    export default {
        data: () => ({
            notify: false,
            text: "",
            color: ""
        }),

        methods: {
            show_notification(text, color) {
                this.text = text;
                this.color = color;
                this.notify=true
            }
        }

    }
</script>

<style scoped>

</style>