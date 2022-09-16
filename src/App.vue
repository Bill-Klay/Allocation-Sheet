<template>
  <v-app>
    <v-main>
        <HelloWorld v-if="is_authenticated"/>
        <LogIn v-if="!is_authenticated" v-on:isAuthenticated="validation"/>
    </v-main>
  </v-app>
</template>

<script>
    import HelloWorld from './components/HelloWorld';
    import LogIn from './components/LogIn';

export default {
    name: 'App',

    components: {
        HelloWorld,
        LogIn
    },

    data: () => ({
        is_authenticated: false
    }),
    methods: {
        validation(value) {
            this.is_authenticated = value;
        }
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