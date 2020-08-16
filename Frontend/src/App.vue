<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="./assets/Canvas-Logo.png"
          transition="scale-transition"
          width="40"
        />

      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
      </v-btn>
    </v-app-bar>

    <v-main>
      <Login @notify="notify($event)" />
      <Notification ref="notification"/>
    </v-main>
  </v-app>
</template>

<script>
import Login from './components/Login';
import Notification from "./components/Notification";

export default {
  name: 'App',

  components: {
    Notification,
    Login,
  },

  data: () => ({
    //
  }),

  methods: {
    notify(event) {
      const args = event.split(",");
      this.$refs.notification.show_notification(args[0], args[1]);
    }
  }

};
</script>
