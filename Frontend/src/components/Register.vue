<template>
    <v-row justify="center">

        <v-dialog v-model="registration_dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
                <v-btn
                        color="primary"
                        dark
                        v-bind="attrs"
                        v-on="on"
                >
                    Register
                </v-btn>
            </template>
            <v-card>
                <v-card-title>
                    <span class="headline">User Profile</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12">
                                <v-text-field label="Username*" prepend-icon="mdi-account" id="username" required></v-text-field>
                            </v-col>
                            <v-col cols="12">
                                <v-text-field label="Email*" prepend-icon="mdi-at" id="email" required></v-text-field>
                            </v-col>
                            <v-col cols="12">
                                <v-text-field label="Password*" type="password" prepend-icon="mdi-lock" id="password" required></v-text-field>
                            </v-col>
                            <v-col cols="12">
                                <v-text-field label="Confirm Password*" type="password" prepend-icon="mdi-lock" id="confirm_password" required></v-text-field>
                            </v-col>
                            <v-col cols="12">
                                <v-text-field label="Canvas API Key*" hint="Find this in your Canvas profile! This is what lets us gather your assignment due dates." prepend-icon="mdi-key-variant" id="api" required></v-text-field>
                            </v-col>
                        </v-row>
                    </v-container>
                    <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="registration_dialog = false">Back</v-btn>
                    <v-btn color="blue darken-1" text @click="post">Submit</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

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
                        Creating your account, please wait
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
    </v-row>


</template>


<script>
    import axios from "axios";

    export default {
        data: () => ({
            registration_dialog: false,
            loading_dialog: false,
        }),

        methods: {

            sleep(ms) {
                return new Promise(resolve => setTimeout(resolve, ms));
            },

            verify_input() {
                let verified = true;
                let username = document.getElementById("username").value;
                let email = document.getElementById("email").value;
                let password = document.getElementById("password").value;
                let confirm_password = document.getElementById("confirm_password").value;

                if(username == "" || password == "") {
                    verified = false;
                    this.$emit('notify', 'Username and password cannot be blank!,error');
                } else if (!(/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))) {
                    verified = false;
                    this.$emit('notify', 'Invalid email!,error');
                } else if (password != confirm_password) {
                    verified = false;
                    this.$emit('notify', 'Passwords do not match!,error');
                }

                return verified;
            },

            post() {

                if(this.verify_input()) {

                    this.loading_dialog = true;
                    console.log("sending post request");
                    axios.post(`http://jsonplaceholder.typicode.com/posts`,
                        {
                            username:   document.getElementById("username").value,
                            email:      document.getElementById("email").value,
                            password:   document.getElementById("password").value,
                            api:        document.getElementById("api").value
                        },
                        {timeout: 15000})
                        .then(async response => {
                            await this.sleep(1000);
                            this.loading_dialog = false;
                            console.log(response);
                            this.registration_dialog = false;
                            this.$emit('notify', 'Registration successful!,success');
                        })
                        .catch(e => {
                            this.errors.push(e)
                            this.loading_dialog = false;
                            this.$emit('notify', 'Registration failed, please try again!,error');
                        })
                }
            }
        },
    }
</script>