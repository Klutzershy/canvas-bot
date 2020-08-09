<template>
    <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
                <v-btn
                        color="primary"
                        dark
                        v-bind="attrs"
                        v-on="on"
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
                                        required
                                ></v-select>
                            </v-col>
                        </v-row>
                    </v-container>
                    <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="dialog = false">Update Preferences</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>


<script>
    export default {
        data: () => ({
            dialog: false,
        }),
    }
</script>