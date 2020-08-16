<template>
  <v-app id="inspire">
    <v-main>
      <v-container
              class="fill-height"
              fluid
      >
        <v-row
                align="center"
                justify="center"
        >
          <v-col
                  cols="12"
                  sm="8"
                  md="4"
          >
            <v-card class="elevation-12">
              <v-toolbar
                      color="primary"
                      dark
                      flat
              >
                <v-toolbar-title>Canvas-Bot Login</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-tooltip bottom>
                </v-tooltip>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                          label="Login"
                          name="login"
                          prepend-icon="mdi-account"
                          type="text"
                          v-model="username"
                  ></v-text-field>

                  <v-text-field
                          id="password"
                          label="Password"
                          name="password"
                          prepend-icon="mdi-lock"
                          type="password"
                          v-model="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <Preferences :username="username" :password="password" @notify="$emit('notify', $event)" />
                <register @notify="$emit('notify', $event)" />
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  import Register from "./Register";
  import Preferences from "./Preferences";
  export default {
    data: () => ({
      username: "",
      password: "",
    }),
    components: {Preferences, Register},
    props: {
      source: String,
    },
  }
</script>