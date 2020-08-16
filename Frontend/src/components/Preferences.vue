<template>
    <v-row justify="center">
        <v-dialog v-model="loading_dialog" persistent max-width="400px">
            <v-container style="height: 200px; background-color: whitesmoke">
                <v-row
                        class="fill-height"
                        align-content="center"
                        justify="center"
                >
                    <v-col
                            class="subtitle-1 text-center"
                            cols="12"
                    >
                        {{ loading_text }}
                    </v-col>
                    <v-col cols="6">
                        <v-progress-linear
                                striped
                                color="primary"
                                indeterminate
                                rounded
                                height="20"
                        ></v-progress-linear>
                    </v-col>
                </v-row>
            </v-container>
        </v-dialog>
        <v-dialog v-model="preferences_dialog" persistent max-width="600px">
            <template v-slot:activator="{  }">
                <v-btn
                        color="primary"
                        dark
                        @click="post"
                >
                    Login
                </v-btn>
            </template>
            <v-card>
                <v-card-title>
                    <span class="headline">User Profile</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12" sm="6">
                                <v-select
                                        :items="['One week before Due Date', 'Five Days Before Due Date', 'Three Days Before Due Date', 'Two Days Before Due Date', 'One Day Before Due Date',
                                                 '12 Hours Before Due Date', '6 Hours Before Due Date', '3 Hours Before Due Date', '1 Hour Before Due Date', 'Unsubscribe']"
                                        label="When To Receive Notifications?"
                                        item-value="string"
                                        @change="map_preferences"
                                        required
                                ></v-select>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <courses :course_info="course_info"/>
                    <v-btn color="blue darken-1" text @click="post">Update Preferences</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>


<script>
    import axios from 'axios';
    import Courses from "./Courses";

    export default {
        components: {Courses},
        data: () => ({
            loading_dialog: false,
            preferences_dialog: false,
            errors: [],
            preference: -1,
            loading_text: "",

            course_info: [
                {
                    id: 1,
                    name: 'Adv. Software Engineering',
                    children: [
                        {id: 2, name: 'Log 5    -   due 4/5/20'},
                        {id: 3, name: 'Log 6    -   due 5/3/20'},
                    ],
                },
                {
                    id: 4,
                    name: 'Adv. Machine Learning',
                    children: [
                        {id: 5, name: 'HW 1     - due 2/2/21'},
                        {id: 6, name: 'Research Topic   -   due 2/4/21'},
                    ],
                },
                {
                    id: 1,
                    name: 'Adv. Software Engineering',
                    children: [
                        {id: 2, name: 'Log 5    -   due 4/5/20'},
                        {id: 3, name: 'Log 6    -   due 5/3/20'},
                    ],
                },
                {
                    id: 4,
                    name: 'Adv. Machine Learning',
                    children: [
                        {id: 5, name: 'HW 1     - due 2/2/21'},
                        {id: 6, name: 'Research Topic   -   due 2/4/21'},
                    ],
                },
                {
                    id: 1,
                    name: 'Adv. Software Engineering',
                    children: [
                        {id: 2, name: 'Log 5    -   due 4/5/20'},
                        {id: 3, name: 'Log 6    -   due 5/3/20'},
                    ],
                },
                {
                    id: 4,
                    name: 'Adv. Machine Learning',
                    children: [
                        {id: 5, name: 'HW 1     - due 2/2/21'},
                        {id: 6, name: 'Research Topic   -   due 2/4/21'},
                    ],
                },
                {
                    id: 1,
                    name: 'Adv. Software Engineering',
                    children: [
                        {id: 2, name: 'Log 5    -   due 4/5/20'},
                        {id: 3, name: 'Log 6    -   due 5/3/20'},
                    ],
                },
                {
                    id: 4,
                    name: 'Adv. Machine Learning',
                    children: [
                        {id: 5, name: 'HW 1     - due 2/2/21'},
                        {id: 6, name: 'Research Topic   -   due 2/4/21'},
                    ],
                },
                {
                    id: 1,
                    name: 'Adv. Software Engineering',
                    children: [
                        {id: 2, name: 'Log 5    -   due 4/5/20'},
                        {id: 3, name: 'Log 6    -   due 5/3/20'},
                    ],
                },
                {
                    id: 4,
                    name: 'Adv. Machine Learning',
                    children: [
                        {id: 5, name: 'HW 1     - due 2/2/21'},
                        {id: 6, name: 'Research Topic   -   due 2/4/21'},
                    ],
                },
            ]
        }),

        props: {
            username: String,
            password: String
        },

        methods: {

            sleep(ms) {
                return new Promise(resolve => setTimeout(resolve, ms));
            },

            map_preferences(selected_preference) {
                console.log("PREFERENCE: " + selected_preference);

                let preference = -1;

                switch (selected_preference) {
                    case 'One week before Due Date':
                        preference = 604800;
                        break;
                    case 'Five Days Before Due Date':
                        preference = 432000;
                        break;
                    case 'Three Days Before Due Date':
                        preference = 259200;
                        break;
                    case 'Two Days Before Due Date':
                        preference = 172800;
                        break;
                    case 'One Day Before Due Date':
                        preference = 86400;
                        break;
                    case '12 Hours Before Due Date':
                        preference = 43200;
                        break;
                    case '6 Hours Before Due Date':
                        preference = 21600;
                        break;
                    case '3 Hours Before Due Date':
                        preference = 10800;
                        break;
                    case '1 Hours Before Due Date':
                        preference = 3600;
                        break;
                }

                console.log("PREFERENCE: " + preference);

                this.preference = preference;
            },

            post() {

                this.loading_dialog=true;
                console.log("sending post request");

                if(!this.preferences_dialog) {
                    this.loading_text = "Logging you in, please wait";
                    axios.post(`http://127.0.0.1:5000/login`,
                        {
                            username: 'username',
                            password: 'password'
                        },
                        {timeout: 15000})
                        .then(async response => {
                            await this.sleep(1000);
                            this.loading_dialog = false;
                            console.log(response);
                            if(!response.data.success) {
                                throw "Login Failed!"
                            } else {
                                this.course_info = response.data.courses;
                                this.preferences_dialog = true;
                                this.$emit('notify', 'Login successful!,success');
                            }
                        })
                        .catch(e => {
                            this.errors.push(e)
                            this.loading_dialog = false;
                            this.$emit('notify', 'Login failed!,error');
                        })
                } else {
                    this.loading_text = "Updating your preferences";
                    axios.post(`http://127.0.0.1:5000/update_preferences`,
                        {
                            username:       'username',
                            password:       'password',
                            preferences:    this.preference
                        },
                        {timeout: 15000})
                        .then(async response => {
                            await this.sleep(1000);
                            this.loading_dialog = false;
                            console.log(response);
                            if(!response.data.success) {
                                throw "Failed to update preferences!!"
                            } else {
                                this.preferences_dialog = false;
                                this.$emit('notify', 'Preferences updated!,success');
                            }
                        })
                        .catch(e => {
                            this.errors.push(e)
                            this.loading_dialog = false;
                            this.$emit('notify', 'An unknown error occurred!,error');
                        })
                }
            }
        },

    }
</script>