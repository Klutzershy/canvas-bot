<template>
    <div>
        <v-dialog v-model="courses_dialog" persistent max-width="525px">
            <template v-slot:activator="{ on }">
                <v-btn
                        color="blue darken-1"
                        text
                        v-on="on"
                >
                    View Upcoming Due Dates
                </v-btn>
            </template>
            <v-card>
                <v-card-title>
                    <span class="headline">Courses</span>
                </v-card-title>
                <v-card-text>
                                <v-treeview
                                        :items="course_info"
                                        open-on-click
                                ></v-treeview>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="printem">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

    </div>
</template>

<script>
    export default {
        name: "Courses",

        data: () => ({
            courses_dialog: false,
        }),

        props: {
            course_info: Array
        },

        methods: {
            printem() {
                console.log(this.course_info);
                this.courses_dialog=false
            }
        }

    }
</script>

<style scoped>

</style>