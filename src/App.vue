<template>
  <v-app>
    <v-main>
        <!--<HelloWorld v-if="is_authenticated"/>-->
        <!--<LogIn v-if="!is_authenticated" v-on:isAuthenticated="validation"/>-->
        <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
    name: 'App',

    data: () => ({
        is_authenticated: false
    }),

    methods: {
        //validation(value) {
        //    this.is_authenticated = value;
        //}
    }
};

</script>

<style>
    div {
        font-family: 'Victor Mono'
    }

    .logo {
        max-height: 75%;
        max-width: 75%;
    }

    .newline {
        margin-top: 20px;
    }

    .custom-loader {
        animation: loader 1s infinite;
        display: flex;
    }

    .tableHeader {
        font-style: oblique;
    }

    html {
        scroll-behavior: smooth;
    }
</style>