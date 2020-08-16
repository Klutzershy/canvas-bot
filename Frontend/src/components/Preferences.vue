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
                    <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="post">Update Preferences</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>


<script>
    import axios from 'axios';

    export default {
        data: () => ({
            loading_dialog: false,
            preferences_dialog: false,
            errors: [],
            preference: -1,
            loading_text: ""
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
                    axios.post(`http://jsonplaceholder.typicode.com/posts`,
                        {
                            username: 'username',
                            password: 'password'
                        },
                        {timeout: 15000})
                        .then(async response => {
                            await this.sleep(1000);
                            this.loading_dialog = false;
                            console.log(response);
                            this.preferences_dialog = true;
                            this.$emit('notify', 'Login successful!,success');
                        })
                        .catch(e => {
                            this.errors.push(e)
                            this.loading_dialog = false;
                            this.$emit('notify', 'Login failed!,error');
                        })
                } else {
                    this.loading_text = "Updating your preferences";
                    axios.post(`http://jsonplaceholder.typicode.com/posts`,
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
                            this.preferences_dialog = false;
                            this.$emit('notify', 'Preferences updated!,success');
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